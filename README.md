# Transcrição do YouTube

Script Python para extrair legendas de vídeos do YouTube, agrupar em frases legíveis e exportar para `.txt`.

## Uso

```bash
source .venv/bin/activate
python transcript.py
```

Cole a URL do vídeo quando solicitado.

## Dependências

```bash
pip install youtube-transcript-api
```

## Formato de Saída

- Frases agrupadas por pontuação
- Keywords destacadas em cores no terminal
- Arquivo `.txt` salvo com o ID do vídeo