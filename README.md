# 🧠 Computer Use Agent (LangGraph + OpenAI + Scrapybara)

An autonomous AI agent that uses a virtual machine browser to perform real-world tasks like searching, clicking, navigating websites, and interacting with web UI.

Built using:
- LangGraph (agent workflow)
- OpenAI GPT-4.1 (reasoning)
- Scrapybara (VM + browser automation)
- FastAPI (API layer)
- Docker (containerized execution)

---

# 🚀 Features

- Autonomous browser control using AI
- Multi-step reasoning with LangGraph
- VM-based execution (Scrapybara)
- Screenshot-based feedback loop
- REST API for triggering tasks
- Fully Dockerized

---

# 🏗️ Architecture

User Request  
→ FastAPI  
→ LangGraph Agent  
→ OpenAI LLM  
→ Computer Use Tools  
→ VM Browser (Scrapybara)  
→ Screenshot feedback loop  
→ Final result

---

# 📦 Project Structure

cua/
  graph.py
  call_model.py
  types.py
  utils.py

api/
  main.py

nodes/
  executor.py

tools/
  browser.py

run.py
Dockerfile
docker-compose.yml
requirements.txt
.env.example

---

# ⚙️ Setup Instructions

## 1. Clone repo
git clone https://github.com/IshantDere/langgraph-computer-using-agent.git
cd langgraph-computer-using-agent

---

## 2. Setup environment
Copy `.env.example` → `.env`

OPENAI_API_KEY=your_key
SCRAPYBARA_API_KEY=your_key

---

## 3. Build Docker
docker compose up -d --build

---

## 4. Run API
http://localhost:8000/

Run agent task:
http://localhost:8000/run-task

---

# 💡 Example Task

Open Google and search LangGraph

---

# 🧠 How it works

1. User sends task
2. LLM interprets instructions
3. VM browser launches
4. Actions executed step-by-step
5. Screenshots validate progress
6. Loop continues until completion

---

# 📡 API Endpoints

GET /
→ Health check

GET /run-task
→ Runs sample agent task

---

# 🐳 Docker Support

Build:
docker compose up -d --build

Logs:
docker logs -f cua-agent

---

# ⚠️ Requirements

- OpenAI API key (GPT-4.1 access)
- Scrapybara API key
- Docker installed (6GB+ RAM recommended)

---

# ❗ Important Notes

- Gemini / Groq are NOT supported in this setup
- Only OpenAI tool-calling models work correctly
- VM is required for browser automation
- Ensure billing is enabled for API usage

---

# 📌 Future Improvements

- Playwright fallback (no VM dependency)
- Multi-agent planning system
- Live browser streaming UI
- Memory-based agent reasoning

---

# 👨‍💻 Author

Built using LangGraph + OpenAI + Scrapybara

---

# ⭐ Support

If you like this project, give it a star ⭐ and contribute 🚀