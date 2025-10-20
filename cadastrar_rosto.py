import cv2, json, os, numpy as np, face_recognition

JSON_FILE = "banco.json"

def carregar_banco():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    return []

def salvar_banco(banco):
    with open(JSON_FILE, "w") as f:
        json.dump(banco, f, indent=4)

def gerar_embedding(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb_frame)
    return encodings[0] if encodings else None

def capturar_rosto():
    cap = cv2.VideoCapture(0)
    print("Ajuste o rosto e pressione 's' para capturar.")
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imshow("Cadastro Facial", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return frame

if __name__ == "__main__":
    frame = capturar_rosto()
    embedding = gerar_embedding(frame)
    if embedding is None:
        print("Rosto não detectado!")
    else:
        banco = carregar_banco()
        banco.append({"embedding": embedding.tolist()})
        salvar_banco(banco)
        print(f"Usuário cadastrado com sucesso!")
