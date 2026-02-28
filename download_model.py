import gdown
import os

url = "https://drive.google.com/uc?id=1CEkCi5qeukG1LeCay-pGkf-A87XGk2rw"
output = "models/model.h5"

if not os.path.exists("models"):
    os.makedirs("models")

if not os.path.exists(output):
    print("Downloading model...")
    gdown.download(url, output, quiet=False)
    print("Download complete.")