from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
import os
import io
from pytube import YouTube
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/download/")
async def download_video(url:str):
    try:
        yt = YouTube(url)
        print("Descargando:", yt.title)
        stream = yt.streams.get_highest_resolution()
        # video=stream.download() 

        video = io.BytesIO()
        stream.stream_to_buffer(video)
        video.seek(0)
        
        print("¡Descarga completada!")
        return StreamingResponse(video, media_type='video/mp4')
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
