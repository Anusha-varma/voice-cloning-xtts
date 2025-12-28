# 🎤 Voice Cloning using XTTS v2

This project implements **zero-shot voice cloning** using **XTTS v2**.  
Given a short **reference audio file (.wav)** and an input **text**, the system generates speech that preserves the speaker’s voice.

This project is developed for **academic / non-commercial use**.

---

## 🚀 Features
- Text → cloned voice
- Uses short reference `.wav` file
- No training required (zero-shot)
- Works on CPU (GPU optional)

---

## 🛠 Tech Stack
- Python 3.10
- Coqui TTS (XTTS v2)
- PyTorch 2.1.2
- Transformers 4.36.2

---

## 📂 Project Structure
voice-cloning-xtts/
├── clone_voice.py
├── requirements.txt
├── README.md
├── .gitignore

---

## ✅ Prerequisites
- Python **3.10.x**  
  https://www.python.org/downloads/release/python-31011/
- Git  
  https://git-scm.com/downloads
- Windows OS (tested)

---

## 🔽 Step 1: Clone the Repository
git clone https://github.com/Anusha-varma/voice-cloning-xtts.git  
cd voice-cloning-xtts

---

## 🧪 Step 2: Create Virtual Environment
python -m venv venv

Activate it (PowerShell):
.\venv\Scripts\Activate.ps1

You should see `(venv)`.

---

## 📦 Step 3: Install Dependencies
pip install --upgrade pip  
pip install -r requirements.txt

---

## 🧱 Step 4: Install C++ Build Tools (Windows only)
Install:
https://visualstudio.microsoft.com/visual-cpp-build-tools/

During installation, select:
- Desktop development with C++
- MSVC v143
- Windows 10/11 SDK

Restart your PC after installation.

---

## 🎧 Step 5: Add Reference Voice
Place a clean voice sample in the project folder:

voice.wav

Recommended:
- 10–30 seconds
- Single speaker
- Minimal background noise

---

## ▶️ Step 6: Run Voice Cloning
python clone_voice.py

On first run:
- Type `y` to accept non-commercial license
- Model will download automatically

---

## 📁 Output
After successful run:

output.wav

This file contains the cloned voice output.

---

## ✏️ Change Input Text
Edit this line in `clone_voice.py`:

text = "I am always with you. You are not alone."

Run again to generate new output.

---

## 📜 License
XTTS v2 is used under the **CPML non-commercial license**.  
This project is intended for **academic / research use only**.

---

## 🙋‍♀️ Author
**Anusha Kucharlapati**  
Final Year Project – Emotional AI Agent (Voice Cloning Module)
