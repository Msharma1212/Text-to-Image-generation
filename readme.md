# 🎨 Realistic Vision AI - Text-to-Image Generator

Generate stunning, high-quality AI images from text prompts using **Realistic Vision v6.0 (HyperVAE)** powered by **Stable Diffusion** — completely offline and without any API keys.

Perfect for developers, AI enthusiasts, artists, and researchers who want full control over image generation on their own machine.

---

## ✨ Features

* 🖼️ **Text-to-Image Generation (txt2img)**
* 🎭 **Image-to-Image Generation (img2img)**
* ⚡ Powered by **Realistic Vision v6.0 HyperVAE**
* 🖥️ **Desktop GUI (Tkinter)**
* 🌐 **Web Interface (Flask)**
* 🚀 GPU Acceleration (CUDA Supported)
* 📂 Automatic Image Saving
* 👀 Instant Image Preview
* 💾 Download Generated Images
* 🔓 No API Keys Required
* 🌐 Fully Offline After Setup
* 🛠️ Open Source & Customizable
* 🚫 Safety Checker Disabled for Maximum Creative Freedom

---

## 📸 Example Use Cases

* AI Art Creation
* Character Design
* Concept Art
* Fantasy Illustrations
* Product Mockups
* Digital Marketing Assets
* Wallpaper Generation
* Game Development Assets
* Creative Experimentation

---

## 🛠️ Tech Stack

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core Development          |
| Diffusers    | Stable Diffusion Pipeline |
| PyTorch      | Deep Learning Framework   |
| Transformers | Model Support             |
| Flask        | Web Interface             |
| Tkinter      | Desktop GUI               |
| Pillow       | Image Processing          |
| Safetensors  | Model Loading             |

---

## 📋 System Requirements

### Minimum

* Python 3.10.x
* 8 GB RAM
* 10 GB Free Storage

### Recommended

* Python 3.10.x
* 16 GB+ RAM
* NVIDIA GPU with CUDA Support
* SSD Storage

### Supported Platforms

* Windows
* Linux
* macOS

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Msharma1212/Text-to-Image-generation.git 

cd realistic-vision-generator
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

Create a file named:

```text
requirements.txt
```

Add:

```text
torch
torchvision
diffusers
transformers
safetensors
pillow
flask
```

Install all packages:

```bash
pip install -r requirements.txt
```

---

## 🤖 Download the Model

Download:

**Realistic Vision v6.0 HyperVAE**

File:

```text
realisticVisionV60B1_v51HyperVAE.safetensors
```

Place the downloaded model file in the project root directory.

Example:

```text
project/
│
├── app.py
├── gui.py
├── realisticVisionV60B1_v51HyperVAE.safetensors
├── outputs/
└── requirements.txt
```

---

## 🚀 Running the Application

### Web Version (Flask)

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

### Desktop Version (Tkinter)

```bash
python gui.py
```

---

## 📂 Project Structure

```text
Realistic-Vision-Generator/
│
├── app.py
├── gui.py
├── requirements.txt
├── outputs/
│   └── generated_images
│
├── static/
├── templates/
│
└── realisticVisionV60B1_v51HyperVAE.safetensors
```

---

## 🖼️ Output

Generated images are automatically saved inside:

```text
outputs/
```

Features:

* Automatic File Naming
* PNG Export
* Easy Download
* Local Storage
* Instant Preview

---

## 🔥 Performance Tips

### Faster Generation

* Use CUDA-enabled GPU
* Close unnecessary applications
* Use SSD storage
* Generate images at 512×512 resolution

### Better Quality Prompts

Example:

```text
masterpiece, ultra realistic portrait, cinematic lighting,
highly detailed face, 8k, sharp focus, professional photography
```

---

## ⚠️ Disclaimer

This project uses an unfiltered AI model.

Generated content may include:

* NSFW imagery
* Biased outputs
* Unexpected generations

Users are responsible for the prompts they provide and the content they generate.

This project is intended for:

* Educational Use
* Research Purposes
* Personal Projects

Please use responsibly and ethically.

---

## 🗺️ Roadmap

Future improvements:

* [ ] Negative Prompt Support
* [ ] Batch Image Generation
* [ ] Prompt History
* [ ] Image Upscaling
* [ ] Multiple Model Support
* [ ] Docker Deployment
* [ ] Dark Theme UI
* [ ] REST API Support
* [ ] LoRA Integration
* [ ] ControlNet Support

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## ⭐ Support

If you find this project useful:

⭐ Star the repository

🍴 Fork the project

🛠️ Contribute improvements

📢 Share it with others

---

# 👨‍💻 Author

## Mayank Sharma

AI Engineer | Full-Stack Developer | Enterprise Software Builder

Dedicated to developing intelligent, scalable, and production-ready software solutions that bridge Artificial Intelligence with modern enterprise applications.

Thank you for exploring this project. Your feedback, contributions, and support are always appreciated.

---

# 📄 License

Licensed under the **MIT License**.

You are welcome to use, modify, and distribute this project in accordance with the terms of the MIT License.

See the **LICENSE** file for more information.
