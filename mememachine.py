# meme_machine.py
# Python ≥ 3.9
# Generates a meme from a template, feeds it to DALL·E 3 for a remix,
# overlays captions, and saves the result to an "output" folder.

import io
import os
import random
import requests
from PIL import Image, ImageDraw, ImageFont
from openai import OpenAI

# ------------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------------
TEMPLATE_URL = "https://i.imgflip.com/1ur9b0.jpg"  # Distracted Boyfriend
CAPTIONS = [
    "When AI writes your code",
    "99 problems but a bug ain't one",
]
OUTPUT_DIR = "output"  # all memes will be saved here
PNG_SIZE = (1024, 1024)  # required by create_variation

# ------------------------------------------------------------------
# STEP 1 – DOWNLOAD TEMPLATE
# ------------------------------------------------------------------
img_bytes = requests.get(TEMPLATE_URL).content
template = Image.open(io.BytesIO(img_bytes)).convert("RGB")

# ------------------------------------------------------------------
# STEP 2 – REMIX WITH DALL·E 3 (PNG ≤ 4 MB)
# ------------------------------------------------------------------
png_buffer = io.BytesIO()
template.thumbnail(PNG_SIZE)            # resize in-place to 1024×1024
template.save(png_buffer, format="PNG")  # convert to PNG
png_bytes = png_buffer.getvalue()

client = OpenAI()

remix_url = client.images.create_variation(
    image=png_bytes,
    n=1,
    size="1024x1024",
).data[0].url

remix_img = Image.open(
    io.BytesIO(requests.get(remix_url).content)
).convert("RGB")

# ------------------------------------------------------------------
# STEP 3 – ADD CAPTIONS WITH PILLOW
# ------------------------------------------------------------------
draw = ImageDraw.Draw(remix_img)
font = ImageFont.truetype("Anton.ttf", 80)
w, h = remix_img.size

y = 40  # initial Y for top text
for caption in CAPTIONS:               # top then bottom
    draw.text(
        (w // 2, y),
        caption,
        font=font,
        fill="white",
        stroke_width=3,
        stroke_fill="black",
        anchor="ms",                   # middle-center anchor
    )
    y = h - 120                        # move to bottom for second line

# ------------------------------------------------------------------
# STEP 4 – SAVE OUTPUT
# ------------------------------------------------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)
filename = f"meme_{random.randint(1000, 9999)}.jpg"
full_path = os.path.join(OUTPUT_DIR, filename)
remix_img.save(full_path, format="JPEG")

print("Saved to:", os.path.abspath(full_path))
