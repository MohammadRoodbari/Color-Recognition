from fastapi import FastAPI, File, UploadFile
from PIL import Image
from app.model.model import get_colors

app = FastAPI()

@app.get("/")
def home():
    return {"health_check": "OK"}

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    file.filename = "test.jpg"
    try:
        contents = await file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception as e:
        return {"message": f"Error uploading or processing image: {str(e)}"}
    finally:
        file.file.close()

    return {"filename": file.filename}

@app.get("/predict")
def predict():

    file_path = "test.jpg"
    with Image.open(file_path) as img:
        color = get_colors(img)

    return {"message": f" Color: {color}"}
