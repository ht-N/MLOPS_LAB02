from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import numpy as np
import os

app = FastAPI()

# Load the trained model
def load_model(model_path):
    model = models.resnet50(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, 10)
    checkpoint = torch.load(model_path, map_location=torch.device('cpu'))
    
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()
    return model

# Preprocess input image
def preprocess_image(image):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
    ])
    return transform(image).unsqueeze(0)

# Class names for CIFAR-10
CLASSES = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file selected")

    try:
        # Read and preprocess the image
        image = Image.open(file.file).convert('RGB')
        image = preprocess_image(image)

        # Make prediction
        with torch.no_grad():
            output = model(image)
            _, predicted = torch.max(output, 1)
            predicted_class = CLASSES[predicted.item()]

        return JSONResponse(content={"class": predicted_class})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Load model when starting the app
model_path = './checkpoints/best_model_logging_demo.pth'
model = load_model(model_path) 