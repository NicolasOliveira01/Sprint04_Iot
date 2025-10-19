import cv2
import face_recognition
import json
import os
import numpy as np

JSON_FILE = "banco.json"

# ---- Funções de banco de dados ----
def carregar_banco():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    return []

def salvar_banco(banco):
    with open(JSON_FILE, "w") as f:
        json.dump(banco, f, indent=4)

# ---- Funções de embeddings ----
def gerar_embedding(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb_frame)
    if encodings:
        emb = encodings[0]
        # Normaliza
        norm = np.linalg.norm(emb)
        if norm == 0:
            return emb
        return emb / norm
    return None

# ---- Cadastro ----
def capturar_rosto(caption="Pressione 's' para capturar"):
    cap = cv2.VideoCapture(0)
    print(f"Ajuste o rosto na frente da webcam e pressione 's' para capturar...")
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imshow(caption, frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return frame

def cadastrar():
    banco = carregar_banco()
    frame = capturar_rosto()
    embedding = gerar_embedding(frame)
    if embedding is not None:
        banco.append({"embedding": embedding.tolist()})
        salvar_banco(banco)
        print("Cadastro realizado com sucesso!")
    else:
        print("Não foi possível detectar o rosto.")

# ---- Validação ----
def validar():
    banco = carregar_banco()
    if not banco:
        print("Nenhum usuário cadastrado.")
        return

    frame = capturar_rosto("Validação facial")
    novo_embedding = gerar_embedding(frame)
    if novo_embedding is None:
        print("Não foi possível detectar o rosto.")
        return

    reconhecido = False
    for registro in banco:
        emb_salvo = np.array(registro["embedding"])
        distancia = np.linalg.norm(emb_salvo - novo_embedding)
        if distancia < 0.4:  # threshold típico de face_recognition
            reconhecido = True
            break

    if reconhecido:
        print("pessoa autorizada")
    else:
        print("pessoa não autorizada")

# ---- Menu ----
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar novo rosto")
        print("2 - Validar rosto")
        print("0 - Sair")
        opcao = input("Opção: ")
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            validar()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
