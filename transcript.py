from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import re

def get_video_id(url):
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        return parse_qs(query.query)['v'][0]
    raise ValueError("URL inválida do YouTube")

def get_transcript(video_url):
    video_id = get_video_id(video_url)
    try:
        return YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'pt-BR', 'en']), video_id
    except Exception as e:
        print(f"\033[1;31mErro ao buscar legendas: {e}\033[0m")
        return None, None

def agrupar_por_frase(transcript):
    texto = " ".join(line['text'] for line in transcript)
    frases = re.split(r'(?<=[.!?]) +', texto)
    return frases

def destacar_keywords(texto, keywords):
    for palavra in keywords:
        texto = re.sub(f"\\b({palavra})\\b", r"\033[1;36m\1\033[0m", texto, flags=re.IGNORECASE)
    return texto

def print_frases_coloridas(frases, keywords):
    for i, frase in enumerate(frases, 1):
        frase_colorida = destacar_keywords(frase, keywords)
        print(f"\033[1;32m[{i:03}]\033[0m {frase_colorida}\n")

def salvar_txt_limpo(frases, video_id):
    filename = f"transcricao_{video_id}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        for i, frase in enumerate(frases, 1):
            f.write(f"[{i:03}] {frase}\n\n")
    print(f"\n\033[1;33mTranscrição salva em: {filename}\033[0m")

if __name__ == "__main__":
    url = input("Cole a URL do vídeo do YouTube: ")
    transcript, video_id = get_transcript(url)

    if transcript:
        frases = agrupar_por_frase(transcript)

        # Palavras a destacar (adicione outras conforme necessário)
        palavras_chave = ["Deus", "Jesus", "Messias", "Israel", "profecia", "tempo", "salvação", "verdade"]

        print("\n\033[1;34mTranscrição (frases agrupadas):\033[0m\n")
        print_frases_coloridas(frases[:10], palavras_chave)  # Mostra 10 primeiras para não explodir o terminal
        salvar_txt_limpo(frases, video_id)
