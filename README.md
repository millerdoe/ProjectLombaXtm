# ProjectLombaXtm

🎥 **Demo Video**: https://youtu.be/ST8h6KwmlTw

## 🚀 Cara Menjalankan Project

### 1. Buka Terminal

```bash
mkdir demo
cd demo
```

---

### 2. Buat Virtual Environment

#### 🪟 Windows

```bash
python -m venv nama_virtual_env
call nama_virtual_env/Scripts/activate
```

#### 🐧 Linux / macOS

```bash
python3 -m venv nama_virtual_env
source nama_virtual_env/bin/activate
```

---

### 3. Download & Install Project

```bash
git clone https://github.com/millerdoe/ProjectLombaXtm.git
cd ProjectLombaXtm
pip install -r requirements.txt
cd project
```

---

### 4. Jalankan Server

#### 🪟 Windows

```bash
python server.py
```

#### 🐧 Linux / macOS

```bash
python3 server.py
```

Buka di browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### ⚙️ Opsional: Tambahkan API Key untuk `ai.html`

1. Buka [https://openrouter.ai/deepseek/deepseek-r1-distill-qwen-32b:free/api](https://openrouter.ai/deepseek/deepseek-r1-distill-qwen-32b:free/api)
2. Klik **"Create API Key"** untuk mendapatkan API gratis
3. Copy key-nya dan paste ke file `key/.env`:

```
OPENAI_API_KEY=masukkan_api_key_anda_di_sini
```

