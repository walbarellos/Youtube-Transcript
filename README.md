# 📖 Leia-me - Transcrição do YouTube com destaque e exportação

## 📝 Objetivo

Este script Python captura as legendas de um vídeo do YouTube usando a API de transcrição automática, agrupa as legendas em frases mais legíveis, destaca palavras-chave com cores no terminal e exporta a transcrição para um arquivo `.txt` formatado.

## 🛠 Pré-requisitos

Antes de rodar o programa, você precisará de:

* **Python 3.x instalado.** (Certifique-se de ter a versão mais recente do Python instalada no seu sistema).
* **Dependências do projeto:**
* `youtube-transcript-api` (para acessar as transcrições dos vídeos do YouTube)

Para instalar as dependências, execute:

```bash
pip install youtube-transcript-api
```

Execute o script:

Após instalar as dependências, basta rodar o script com o seguinte comando no terminal:

```bash
python transcript.py
```

Forneça a URL do vídeo do YouTube:

Após rodar o script, será solicitado para que você cole a URL do vídeo do YouTube, algo como:

```bash
Cole a URL do vídeo do YouTube: https://www.youtube.com/watch?v=example
```


⚠ Limitações

    O script depende das legendas automáticas do YouTube, o que significa que a qualidade da transcrição pode variar.

    O script não realiza correções automáticas nas transcrições (como remoção de palavras erradas ou não capturadas).

    Caso o vídeo não tenha legendas, o programa exibirá uma mensagem de erro.


💡 Possíveis Melhorias Futuras
    
    Suporte para múltiplos idiomas.

    Resumo automático das transcrições.

    Integração com sistemas de recomendação para vídeos baseados em palavras-chave.

