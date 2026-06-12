Text-to-Image Generator using Python + Realistic Vision
========================================================

Generate high-quality images from text prompts using the latest
Realistic Vision v6.0 (HyperVAE) model, fully offline using Python.

No API keys. No internet required after setup. GPU acceleration supported.

--------------------------------------------------------
Features:
--------------------------------------------------------
- Text-to-Image generation (txt2img)
- Image-to-Image generation (img2img, optional input image)
- Based on Stable Diffusion Pipeline
- Tkinter GUI and Flask Web UI (choose any)
- Transparent PNG output (512x512)
- Output folder + preview + download
- Unfiltered: no safety checker (for full creative control)

--------------------------------------------------------
System Requirements:
--------------------------------------------------------
- OS: Windows / Linux / macOS
- Python: 3.10.x (strictly recommended)
- RAM: 8GB minimum (16GB+ recommended)
- CUDA GPU (optional but strongly recommended)

--------------------------------------------------------
Installation:
--------------------------------------------------------

1. Create Virtual Environment (optional but recommended)
--------------------------------------------------------
    python -m venv venv

    # Activate it:
    - On Windows:
        venv\Scripts\activate
    - On macOS/Linux:
        source venv/bin/activate

2. Install Requirements
--------------------------------------------------------
Create a file named requirements.txt and paste:

    torch
    torchvision
    diffusers
    transformers
    safetensors
    pillow
    flask

Then install with:
    pip install -r requirements.txt

3. Download the Model File
--------------------------------------------------------
Model: realisticVisionV60B1_v51HyperVAE.safetensors  
Source: https://civitai.com/models/4201/realistic-vision-v60

Place this file in the same directory as `app.py` or `gui.py`

4. Run the Application
--------------------------------------------------------

- To run the web app (Flask):
    python app.py
    → open http://127.0.0.1:5000/ in browser

- To run the desktop GUI (Tkinter):
    python gui.py

--------------------------------------------------------
⚠️ Important Note:
--------------------------------------------------------
This app uses an unfiltered AI model.
NSFW, biased, or inappropriate results are possible depending on the prompt.

This tool is for **educational and personal use only**. Use responsibly.

--------------------------------------------------------
Credits:
--------------------------------------------------------
Developed & published by: Mayank Sharma


--------------------------------------------------------
