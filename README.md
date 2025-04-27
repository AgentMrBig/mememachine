# Meme Machine 🖼️⚡

Generate endless custom memes in **under 10 minutes** with Python and DALL·E 3.
This tiny script  

1. downloads a classic meme template  
2. sends it to OpenAI’s *create variation* endpoint for an AI remix  
3. slaps on your captions with Pillow  
4. saves the finished meme to an `output/` folder  

---

## Demo

```bash
$ python meme_machine.py
Saved to: C:\…\output\meme_4721.jpg
```

*(Open the file & enjoy your auto-generated masterpiece.)*

---

## Prerequisites

| Tool | Why you need it | Quick install |
|------|-----------------|---------------|
| **Git Bash** | Consistent Bash terminal on Windows/macOS/Linux | <https://gitforwindows.org> (Win) or `brew install git` (macOS) |
| **Python 3.9+** | Runs the script | <https://python.org> |
| **OpenAI API key** | Access DALL·E 3 | <https://platform.openai.com> |

> **Font:** Drop `Impact.ttf` (or Google’s `Anton-Regular.ttf`) in the same folder as the script for proper meme text styling.

---

## Setup (once)

```bash
# 1  Clone or unzip the project
cd "C:/Users/YourName/Desktop/meme_machine"

# 2  Install dependencies
pip install openai pillow requests

# 3  Set your OpenAI key for the current session
export OPENAI_API_KEY="sk-YOUR-KEY"
```

---

## Usage

```bash
python meme_machine.py
```

*Output files appear in `output/` with names like `meme_1234.jpg`.*

### Custom captions

Edit the `CAPTIONS` list near the top of **meme_machine.py**:

```python
CAPTIONS = [
    "Top line goes here",
    "Bottom line goes here",
]
```

Or switch to interactive mode:

```python
top = input("Top text: ")
bottom = input("Bottom text: ")
CAPTIONS = [top, bottom]
```

### Batch generation

Replace `CAPTIONS` with a list of lists and loop:

```python
CAPTION_PAIRS = [
    ["Debugging all day", "But it was a semicolon"],
    ["When GPT fixes it", "On the first try"],
]

for caps in CAPTION_PAIRS:
    CAPTIONS = caps
    # run remix / save block
```

---

## How it works

1. **Requests** grabs the original JPG template.  
2. Pillow converts it to a 1024 × 1024 PNG (DALL·E requirement).  
3. OpenAI `images.create_variation` returns a remix URL.  
4. Pillow overlays captions in Impact-style font.  
5. The finished meme is saved as JPEG in `output/`.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `invalid_image_format` | Keep templates square & under 4 MB — the default code already converts the example. |
| `cannot open resource` (font error) | Ensure the TTF sits beside the script, or update `FONT_PATH`. |
| No output image found | Check your current directory (`pwd`) or hard-code `OUTPUT_DIR` in the script. |

---

## License

MIT — do whatever you like, just don’t claim you wrote the memes yourself 😉

Tag **[@ScriptForgeAI](https://youtube.com/@ScriptForgeAI)** when you post your creations — we’d love to see them!
