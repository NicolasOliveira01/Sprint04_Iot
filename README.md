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

## Scripts do projeto 

### cadastrar_rosto.py
Ao ser executado, ele ativa a webcam e exibe uma janela pedindo para o usuário ajustar o rosto e pressionar a tecla ‘s’ quando estiver pronto para capturar a imagem. Após a captura, a imagem é processada pela biblioteca face_recognition, que gera um embedding facial — um vetor numérico que representa as principais características do rosto.

Em seguida, o script carrega o arquivo banco.json, que funciona como um banco de dados local. Caso o arquivo ainda não exista, um novo será criado. O embedding gerado é então adicionado à lista de rostos cadastrados e o banco é salvo novamente no arquivo JSON.

Dessa forma, cada execução do script registra um novo rosto, permitindo que o sistema construa um banco facial para futuras verificações de identidade.

### script.py
implementa um servidor Flask para reconhecimento facial em tempo real, utilizando um banco de rostos previamente cadastrados.

Quando o servidor é iniciado, ele fica disponível para receber requisições HTTP no endpoint /reconhecer. Ao acessar esse endpoint (por exemplo, via aplicativo ou navegador), o sistema executa o processo de validação facial.

Primeiro, o script carrega os embeddings salvos no arquivo banco.json, que funciona como o banco de dados local contendo os rostos cadastrados. Em seguida, ativa a webcam e solicita que o usuário ajuste o rosto e pressione ‘s’ para capturar uma imagem.

A imagem é então processada para gerar um novo embedding facial, representando o rosto atual. O sistema compara esse embedding com todos os salvos no banco, calculando a distância entre eles — quanto menor a distância, mais semelhante o rosto é.

  
