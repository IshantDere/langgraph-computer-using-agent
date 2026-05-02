from tools.browser import BrowserTool

browser = BrowserTool()

async def execute_action(state):
    task = state["task"]

    if "google" in task.lower():
        await browser.start()
        await browser.search_google(task)
        path = await browser.screenshot()

        return {
            "messages": f"Executed search, screenshot saved: {path}",
            "step": "done"
        }

    return state