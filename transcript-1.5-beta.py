from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import re

def get_video_id(url):
    query = urlparse(url)
    if query.hostname in ('www.youtube.com', 'm.youtube.com', 'youtube.com'):
        if 'v' in parse_qs(query.query):
            return parse_qs(query.query)['v'][0]
        else:
            return query.path.split('/')[-1]
    elif query.hostname in ('youtu.be', 'ww.youtube.com/watch?v=vhtij8Aci6I', 'https://www.youtube.com/watch?v=vhtij8Aci6I'):
        return query.path[1:]
    raise ValueError("URL inválida do YouTube")

def get_transcript(video_url):
    try:
        video_id = get_video_id(video_url)
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_generated_transcript(['pt', 'pt-BR', 'en'])
        fetched_transcript = transcript.fetch()

        print("\n\033[1;35m--- Inspeção do objeto fetched_transcript (primeiro item) ---\033[0m")
        if fetched_transcript:
            print(type(fetched_transcript[0]))
            print(fetched_transcript[0])
        else:
            print("\033[1;31mfetched_transcript está vazio.\033[0m")
            return None, None
        print("\033[1;35m--- Fim da inspeção ---\033[0m\n")

        # Tentar acessar o texto de forma mais robusta
        transcript_text = []
        for item in fetched_transcript:
            if hasattr(item, 'text'):
                transcript_text.append(item.text)
            elif isinstance(item, dict) and 'text' in item:
                transcript_text.append(item['text'])
            else:
                print(f"\033[1;33mAviso: Item sem atributo ou chave 'text' encontrado: {item}\033[0m")

        return transcript_text, video_id
    except Exception as e:
        print(f"\033[1;31mErro ao buscar legendas: {e}\033[0m")
        return None, None

def agrupar_por_frase(transcript):
    texto = " ".join(transcript)
    frases = re.split(r'(?<=[.!?]) +', texto)
    return [frase.strip() for frase in frases if frase.strip()]

def destacar_keywords(texto, keywords):
    for palavra in keywords:
        texto = re.sub(r'\b(' + re.escape(palavra) + r')\b', r'\033[1;36m\1\033[0m', texto, flags=re.IGNORECASE)
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
    transcript_data, video_id = get_transcript(url)

    if transcript_data:
        frases = agrupar_por_frase(transcript_data)

        # Palavras a destacar (adicione ou remova conforme necessário)
        palavras_chave = ["mencionar", "exemplo", "importante", "atenção", "análise"]

        print("\n\033[1;34mTranscrição (frases agrupadas e destacadas):\033[0m\n")
        print_frases_coloridas(frases[:20], palavras_chave) # Mostra as 20 primeiras frases

        salvar_txt_limpo(frases, video_id)
    else:
        print("\n\033[1;31mNão foi possível obter a transcrição.\033[0m")
