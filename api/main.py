from fastapi import FastAPI
import asyncio

from cua.graph import graph  # or create_cua depending on your project

app = FastAPI()

@app.get("/")
def health():
    return {"status": "running"}

@app.get("/run-task")
async def run_task():
    """
    Runs a sample computer-use agent task:
    Open Google and search LangGraph
    """

    task = "Open Google and search LangGraph"

    result = await graph.ainvoke(
        {
            "messages": [
                ("user", task)
            ]
        }
    )

    return {
        "task": task,
        "result": result
    }


# optional: run automatically on startup (for testing)
@app.on_event("startup")
async def startup_event():
    print("Starting agent...")

    task = "Open Google and search LangGraph"

    try:
        result = await graph.ainvoke(
            {
                "messages": [
                    ("user", task)
                ]
            }
        )
        print("Initial run result:", result)
    except Exception as e:
        print("Startup task failed:", e)