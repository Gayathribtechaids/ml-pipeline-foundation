from pathlib import Path
from PIL import Image
import sys


output_folder = Path("data/raw")
output_folder.mkdir(parents=True, exist_ok=True)

number_of_images = int(sys.argv[1])

for i in range(number_of_images):
    image = Image.new("RGB", (100, 100), "white")
    image.save(output_folder / f"image_{i}.jpg")
    
print(f"{number_of_images} test images created.")