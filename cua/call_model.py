from typing import Dict, Any
from langchain_openai import ChatOpenAI
from .types import CUAState

async def call_model(state: CUAState, config) -> Dict[str, Any]:
    messages = state.get("messages", [])

    llm = ChatOpenAI(
        model="gpt-4.1-mini"
    )

    response = await llm.ainvoke(messages)

    return {"messages": response}