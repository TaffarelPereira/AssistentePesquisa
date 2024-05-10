{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN0ANHXx5JrX4XLWMxDZq1H"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "JfepI7P5ycdO"
      },
      "outputs": [],
      "source": [
        "# -*- coding: utf-8 -*-\n",
        "\"\"\"AssistentePesquisa.py\n",
        "\n",
        "Script Python para um assistente de pesquisa científica com Google Gemini.\n",
        "\"\"\"\n",
        "\n",
        "# Instalar SDK do Google se necessário\n",
        "# !pip install -q -U google-generativeai\n",
        "\n",
        "# Importar bibliotecas\n",
        "import google.generativeai as genai\n",
        "from google.colab import userdata\n",
        "\n",
        "# Configurar API Key (substitua pelo seu valor)\n",
        "GOOGLE_API_KEY = \"GOOGLE_API_KEY\"\n",
        "genai.configure(api_key=GOOGLE_API_KEY)\n",
        "\n",
        "# Configurar modelo Gemini\n",
        "generation_config = {\n",
        "    \"candidate_count\": 1,\n",
        "    \"temperature\": 0.7,  # Ajustar a criatividade do modelo\n",
        "}\n",
        "safety_settings = {\n",
        "    \"HARASSMENT\": \"BLOCK_NONE\",\n",
        "    \"HATE\": \"BLOCK_NONE\",\n",
        "    \"SEXUAL\": \"BLOCK_NONE\",\n",
        "    \"DANGEROUS\": \"BLOCK_NONE\",\n",
        "}\n",
        "model = genai.GenerativeModel(\n",
        "    model_name=\"gemini-1.0-pro\",\n",
        "    generation_config=generation_config,\n",
        "    safety_settings=safety_settings,\n",
        ")\n",
        "\n",
        "def pesquisar_tema(tema):\n",
        "    \"\"\"\n",
        "    Pesquisa um tema científico usando o Gemini e retorna informações relevantes.\n",
        "    \"\"\"\n",
        "    prompt = f\"Eu sou um pesquisador interessado em {tema}. Por favor, forneça um resumo do tema, incluindo conceitos principais, descobertas recentes e áreas de pesquisa em aberto. Sugira também artigos científicos relevantes e especialistas no campo.\"\n",
        "    response = model.generate_content(prompt)\n",
        "    return response.text\n",
        "\n",
        "# Loop principal\n",
        "while True:\n",
        "    tema = input(\"Digite um tema de pesquisa (ou 'sair' para encerrar): \")\n",
        "    if tema.lower() == \"sair\":\n",
        "        break\n",
        "\n",
        "    resultado = pesquisar_tema(tema)\n",
        "    print(\"\\n--- Resultados da Pesquisa ---\\n\")\n",
        "    print(resultado)\n",
        "    print(\"\\n-----------------------------\\n\")"
      ]
    }
  ]
}
