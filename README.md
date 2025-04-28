# Meme Machine 🖼️⚡

Generate endless custom memes in **under 10 minutes** with Python 3 and DALL·E 3.

This tiny script:

1. Downloads the classic **Distracted Boyfriend** template  
2. Converts it to a 1024 × 1024 PNG (required by the DALL·E variation endpoint)  
3. Sends it to `images.create_variation` for an AI remix  
4. Overlays your own captions with Pillow  
5. Saves the finished JPEG in an **output/** folder  

---

## Demo

    $ python meme_machine.py
    Saved to: C:\…\output\meme_4721.jpg

*(Open the file and enjoy your auto-generated masterpiece.)*

---

## Prerequisites

| Tool | Why you need it | Quick install |
|------|-----------------|---------------|
| **Git Bash** | Consistent Bash terminal on Win/macOS/Linux | https://gitforwindows.org (Win)&nbsp;&nbsp;·&nbsp;&nbsp;`brew install git` (mac) |
| **Python 3.9 +** | Runs the script | https://python.org |
| **OpenAI API key** | Talks to DALL·E 3 | https://platform.openai.com |

> **Font** — download `Anton.ttf` from Google Fonts and place it next to `meme_machine.py`.  
> If the font is missing, the script falls back to Pillow’s default font.

---

## Setup (once)

    # 1 Clone or unzip the project
    cd "C:/Users/YourName/Desktop/meme_machine"

    # 2 Install dependencies
    pip install openai pillow requests

    # 3 Set your OpenAI key for this session
    export OPENAI_API_KEY="sk-YOUR-KEY"

*(On Windows Cmd use `set` instead of `export`; in PowerShell use `$Env:OPENAI_API_KEY`.)*

---

## Usage

    python meme_machine.py

A file like **meme_1234.jpg** appears in **output/**.

### Custom captions

Edit the `CAPTIONS` list near the top of the script:

    CAPTIONS = [
        "Top line goes here",
        "Bottom line goes here",
    ]

—or switch to interactive prompts:

    top    = input("Top text: ")
    bottom = input("Bottom text: ")
    CAPTIONS = [top, bottom]

### Batch generation

    CAPTION_PAIRS = [
        ["Debugging all day", "But it was a semicolon"],
        ["When GPT fixes it", "On the first try"],
    ]

    for top, bottom in CAPTION_PAIRS:
        CAPTIONS = [top, bottom]
        # call the remix-and-save block (wrap it in a function for clarity)

---

## How it works

1. **Requests** pulls the JPG template.  
2. **Pillow** resizes it to 1024 × 1024 and converts to PNG (< 4 MB).  
3. **OpenAI** returns a remix URL via `create_variation`.  
4. **Pillow** draws captions  
   · font size = image_height × 0.06  
   · top margin = 10 % of height  
   · bottom margin = 12 % of height  
5. The meme saves as `output/meme_XXXX.jpg`.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `invalid_image_format` | Keep alternate templates square and < 4 MB—the default code already resizes the example. |
| `cannot open resource` (font error) | Ensure `Anton.ttf` sits beside the script or change `FONT_FILE` to another TTF. |
| JPG saved somewhere unexpected | The meme saves to your *current working directory*—run `pwd` in Git Bash or hard-code `OUTPUT_DIR`. |

---

## License

MIT — use it, remix it, have fun; just don’t claim you wrote all the memes yourself. 😉

Tag **@ScriptForgeAI** (https://youtube.com/@ScriptForgeAI) when you share your creations—we’d love to see them!
