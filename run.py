import asyncio
from cua.graph import graph

async def main():
    result = await graph.ainvoke({
        "messages": [],
        "task": "Open Google and search LangGraph",
        "step": "start"
    })

    print(result)

if __name__ == "__main__":
    asyncio.run(main())