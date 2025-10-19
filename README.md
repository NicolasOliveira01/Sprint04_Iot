# Reconhecimento Facial com OpenCV, Face_recognition e Numpy

## 📌 Objetivo
Este projeto implementa um sistema local de **cadastro e validação facial** utilizando `Numpy`, `OpenCV`, `Face_recognition`, `json`e `os`. 
Este projeto foi integrado em um **aplicativo mobile em React Native**, permitindo que usuários se cadastrem por reconhecimento facial.

---

## ⚙️ Como executar
1. Clone este repositório  
    ```bash
    git clone https://github.com/NicolasOliveira01/Sprint03_Iot
    ```
2. Instale as dependências
    ```bash
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. Execute o script principal:
   ```bash
   python main.py
   ```
---

## Como funciona

- Cada rosto é transformado em um **embedding** (vetor numérico) usando DeepFace.  
- Para validar um usuário, calculamos a **distância euclidiana** entre o embedding capturado e os embeddings salvos no banco.  
- O threshold define o limite máximo dessa distância para considerar que os rostos são da mesma pessoa.  

--- 

## 📦 Dependências e versões recomendadas

### **face_recognition (`face_recognition`)**
- Detecta rostos em imagens e vídeos.
- Gera embeddings (vetores numéricos) que representam características únicas do rosto.
- Permite comparar rostos calculando a distância entre embeddings para verificar se são da mesma pessoa.
- Facilita autenticação facial sem necessidade de treinar modelos complexos manualmente.

### **OpenCV (`cv2`)**
- Captura vídeo da webcam.
- Exibe imagens em janelas.
- Converte imagens entre formatos BGR/RGB.

### **JSON (`json`)**
- Salva e carrega embeddings faciais no arquivo `banco.json`.
- Permite persistência dos dados sem necessidade de banco de dados complexo.

### **OS (`os`)**
- Verifica se o arquivo `banco.json` existe antes de carregá-lo.

### **NumPy (`numpy`)**
- Manipula arrays de embeddings.
- Calcula distância euclidiana entre embeddings para validação do usuário.
- Converte embeddings para listas antes de salvar no JSON.

---

## Funções principais

### **carregar_banco()**
- Carrega os embeddings faciais salvos no arquivo `banco.json`. Retorna uma lista vazia se o arquivo não existir.

### **salvar_banco(banco)**
- Salva os embeddings faciais no arquivo `banco.json` para persistência dos dados.

### **gerar_embedding(frame)**
- Recebe uma imagem (frame), detecta o rosto e gera um embedding normalizado usando `face_recognition`. Retorna None se não detectar rosto.

### **capturar_rosto(caption)**
- Abre a webcam, mostra a imagem em tempo real e captura um frame quando o usuário pressiona 's'.

### **cadastrar()**
- Captura o rosto do usuário, gera o embedding e salva no banco (banco.json). Exibe mensagens de sucesso ou falha.

### **validar()**
- Captura o rosto do usuário, gera o embedding e compara com os embeddings cadastrados. Retorna no console `"autorizada"` ou `"não autorizada"`.

### **main()**
- Menu interativo para o usuário escolher entre cadastrar um novo rosto, validar um rosto ou sair do programa.

---


