from playwright.sync_api import sync_playwright
import time

def test_frontend_e2e():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("file:///C:/Projetos/TC-JOGO/Codigo-Calculadora/calculator/frontend/index.html")

        # Clicar usando o atributo onclick (mais seguro)
        page.click("button[onclick='appendNumber(2)']")
        page.click("button[onclick=\"setOperation('+')\"]")
        page.click("button[onclick='appendNumber(3)']")
        page.click("button[onclick='calculateResult()']")

        time.sleep(0.3)

        result = page.inner_text("#display").strip()

        assert result == "5"

        browser.close()
