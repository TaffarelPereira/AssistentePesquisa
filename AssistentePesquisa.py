# -*- coding: utf-8 -*-
"""AssistentePesquisa.py

Script Python para um assistente de pesquisa científica com Google Gemini.
"""

# Instalar SDK do Google se necessário
# !pip install -q -U google-generativeai

# Importar bibliotecas
import google.generativeai as genai
from google.colab import userdata

# Configurar API Key (substitua pelo seu valor)
GOOGLE_API_KEY = "GOOGLE_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# Configurar modelo Gemini
generation_config = {
    "candidate_count": 1,
    "temperature": 0.7,  # Ajustar a criatividade do modelo
}
safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}
model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

def pesquisar_tema(tema):
    """
    Pesquisa um tema científico usando o Gemini e retorna informações relevantes.
    """
    prompt = f"Eu sou um pesquisador interessado em {tema}. Por favor, forneça um resumo do tema, incluindo conceitos principais, descobertas recentes e áreas de pesquisa em aberto. Sugira também artigos científicos relevantes e especialistas no campo."
    response = model.generate_content(prompt)
    return response.text

# Loop principal
while True:
    tema = input("Digite um tema de pesquisa (ou 'sair' para encerrar): ")
    if tema.lower() == "sair":
        break

    resultado = pesquisar_tema(tema)
    print("\n--- Resultados da Pesquisa ---\n")
    print(resultado)
    print("\n-----------------------------\n")
