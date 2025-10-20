from flask import Flask, jsonify
import cv2
import json
import os
import numpy as np
import face_recognition

app = Flask(__name__)

JSON_FILE = "banco.json"

# ---------- Funções auxiliares ----------
def carregar_banco():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    return []

def gerar_embedding(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb_frame)
    if encodings:
        emb = encodings[0]
        # Normaliza o vetor para evitar distorções
        norm = np.linalg.norm(emb)
        return emb / norm if norm != 0 else emb
    return None

def capturar_rosto():
    cap = cv2.VideoCapture(0)
    print("Ajuste o rosto e pressione 's' para capturar.")
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imshow("Reconhecimento Facial", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return frame

def validar():
    banco = carregar_banco()
    if not banco:
        return "Nenhum usuário cadastrado."

    frame = capturar_rosto()
    novo_embedding = gerar_embedding(frame)
    if novo_embedding is None:
        return "Não foi possível detectar o rosto."

    for registro in banco:
        emb_salvo = np.array(registro["embedding"])
        distancia = np.linalg.norm(emb_salvo - novo_embedding)
        if distancia < 0.5:
            return f"autorizado"
    return "não autorizado"

# ---------- Rota do servidor ----------
@app.route("/reconhecer", methods=["GET"])
def reconhecer():
    print("📸 Iniciando reconhecimento facial...")
    resultado = validar()
    print(f"Resultado: {resultado}")
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
