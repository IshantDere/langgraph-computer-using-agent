from playwright.async_api import async_playwright

class BrowserTool:
    def __init__(self):
        self.browser = None
        self.page = None
        self.playwright = None

    async def start(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.page = await self.browser.new_page()

    async def search_google(self, query: str):
        await self.page.goto("https://www.google.com")
        await self.page.fill("textarea[name='q']", query)
        await self.page.keyboard.press("Enter")
        await self.page.wait_for_timeout(3000)

    async def screenshot(self, path="screen.png"):
        await self.page.screenshot(path=path)
        return path

    async def close(self):
        await self.browser.close()
        await self.playwright.stop()