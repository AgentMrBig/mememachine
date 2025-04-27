# meme_machine.py
# Python ≥ 3.9
# Generates a meme from a template, feeds it to DALL·E 3 for a remix,
# overlays captions, and saves the result to an "output" folder.

import io
import os
import random
import requests
from pathlib import Path
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
OUTPUT_DIR = "output"          # finished memes land here
PNG_SIZE = (1024, 1024)        # required by create_variation
FONT_FILE = "Anton.ttf"        # put the TTF beside this script
TOP_MARGIN_RATIO = 0.10        # 10 % of image height
BOTTOM_MARGIN_RATIO = 0.12     # 12 % of image height

# ------------------------------------------------------------------
# STEP 1 – DOWNLOAD TEMPLATE
# ------------------------------------------------------------------
img_bytes = requests.get(TEMPLATE_URL).content
template = Image.open(io.BytesIO(img_bytes)).convert("RGB")

# ------------------------------------------------------------------
# STEP 2 – REMIX WITH DALL·E 3 (PNG ≤ 4 MB)
# ------------------------------------------------------------------
png_buffer = io.BytesIO()
template.thumbnail(PNG_SIZE)            # resize to 1024×1024
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
w, h = remix_img.size
dynamic_font_size = int(h * 0.06)  # text at ~6 % of image height

# build absolute path to font file
font_path = Path(__file__).parent / FONT_FILE
try:
    font = ImageFont.truetype(str(font_path), dynamic_font_size)
except OSError:
    print("Custom font not found; using default Pillow font.")
    font = ImageFont.load_default()

draw = ImageDraw.Draw(remix_img)

# top caption
y_top = int(h * TOP_MARGIN_RATIO)
draw.text(
    (w // 2, y_top),
    CAPTIONS[0],
    font=font,
    fill="white",
    stroke_width=3,
    stroke_fill="black",
    anchor="ms",
)

# bottom caption
y_bottom = h - int(h * BOTTOM_MARGIN_RATIO)
draw.text(
    (w // 2, y_bottom),
    CAPTIONS[1],
    font=font,
    fill="white",
    stroke_width=3,
    stroke_fill="black",
    anchor="ms",
)

# ------------------------------------------------------------------
# STEP 4 – SAVE OUTPUT
# ------------------------------------------------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)
filename = f"meme_{random.randint(1000, 9999)}.jpg"
full_path = os.path.join(OUTPUT_DIR, filename)
remix_img.save(full_path, format="JPEG")

print("Saved to:", os.path.abspath(full_path))
