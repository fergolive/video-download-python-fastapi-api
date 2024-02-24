from pytube import YouTube

def descargar_video(url):
    try:
        yt = YouTube(url)
        print("Descargando:", yt.title)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("¡Descarga completada!")
    except Exception as e:
        print("Ocurrió un error:", str(e))

def main():
    url = input("Por favor, introduce la URL del video de YouTube que deseas descargar: ")
    descargar_video(url)

if __name__ == "__main__":
    main()