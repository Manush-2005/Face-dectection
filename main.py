from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from deepface import DeepFace
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class ImageURLs(BaseModel):
    image1_url: str
    image2_url: str

@app.post("/verify")
def verify_faces(image_urls: ImageURLs):
    try:
        resp = DeepFace.verify(img1_path=image_urls.image1_url, img2_path=image_urls.image2_url, model_name="Facenet")
        return resp
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
