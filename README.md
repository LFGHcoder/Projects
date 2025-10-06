# 🤖 Instagram Engagement Bot

A lightweight automation tool built with **FastAPI** that can **like** and **comment** on Instagram posts intelligently — great for marketers, creators, and growth hackers who want to boost engagement safely.  

> ⚡ Designed for safe, rate-limited operations using Instagram Graph API and scheduler jobs.

---

## ✨ Features

- ❤️ Auto-like recent posts from target accounts  
- 💬 Auto-comment intelligently on selected posts  
- 🔐 Secure API endpoints with auth middleware  
- 🕓 Background job scheduling for steady activity  
- 🧰 Modular structure for easy feature extension  

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/LFGHcoder/Projects.git
cd Projects
### 2) Create a virtualenv & install
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3) Create your .env from template
cp .env.example .env   # Windows: copy .env.example .env

# 4) Run the API
uvicorn src.app:app --reload
# then open http://127.0.0.1:8000/health
