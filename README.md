# 🧠 Computer Use Agent (LangGraph + OpenAI + Scrapybara)

An AI-powered Computer Use Agent built using LangGraph, OpenAI GPT-4.1, and Scrapybara VM infrastructure.  
The agent can control a virtual machine browser and perform real-world tasks like searching, clicking, navigating websites, and interacting with web UI.

---

## 🚀 Features

- LLM-driven decision making using OpenAI GPT-4.1 / GPT-4.1-mini  
- Virtual machine execution using Scrapybara  
- Browser automation (Google search, clicking, scrolling, navigation)  
- LangGraph stateful workflow  
- Screenshot-based reasoning (computer-use loop)  
- Fully containerized using Docker  

---

## 🏗️ Architecture

User Prompt → LangGraph Agent → OpenAI GPT-4.1 → Computer Use Tool (VM) → Browser Actions → Screenshot feedback loop → repeat

---

## 📦 Tech Stack

Python 3.11  
LangGraph  
LangChain OpenAI  
OpenAI API  
Scrapybara VM  
FastAPI  
Uvicorn  
Docker  
Docker Compose  

---

## ⚙️ Setup Instructions

### 1. Clone repository
git clone https://github.com/IshantDere/langgraph-computer-using-agent.git
cd langgraph-computer-using-agent

---

### 2. Create .env file
OPENAI_API_KEY=your_openai_api_key
SCRAPYBARA_API_KEY=your_scrapybara_api_key

---

### 3. Build and run
docker compose up -d --build

---

### 4. Run API
If using FastAPI:

http://localhost:8000/

Run agent task:

http://localhost:8000/run-task

---

### 5. View logs
docker logs -f cua-agent

---

## 💡 Example Task

Open Google and search LangGraph

---

## 🧠 How it works

call_model → LLM reasoning step  
create_vm_instance → starts VM browser  
take_computer_action → performs browser actions  
loop continues until task completes  

---

## 📁 Project Structure

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

## ⚠️ Requirements

- OpenAI API key (GPT-4.1 access required)
- Scrapybara API key
- Docker installed (recommended 6GB+ RAM)

---

## ❗ Important Notes

- Gemini / Groq are NOT supported
- Only OpenAI tool-calling models work correctly
- VM is required for computer-use actions
- Ensure billing is enabled for OpenAI API

---

## 📌 Future Improvements

- Playwright fallback mode (no VM required)
- Multi-agent planning system
- Memory + task history
- Live browser view UI

---

## 👨‍💻 Author

Built using LangGraph + OpenAI + Scrapybara

---

## ⭐ Support

If you like this project, give it a star ⭐ and contribute 🚀