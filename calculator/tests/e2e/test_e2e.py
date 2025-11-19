from playwright.sync_api import sync_playwright
import time
import os

def test_frontend_e2e():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Caminho correto para funcionar no Windows e no GitHub Actions (Linux)
        caminho = os.path.abspath("calculator/frontend/index.html")
        page.goto(f"file:///{caminho.replace(os.sep, '/')}")

        # Clicar usando os atributos onclick
        page.click("button[onclick='appendNumber(2)']")
        page.click("button[onclick=\"setOperation('+')\"]")
        page.click("button[onclick='appendNumber(3)']")
        page.click("button[onclick='calculateResult()']")

        time.sleep(0.3)

        result = page.inner_text("#display").strip()

        assert result == "5"

        browser.close()
