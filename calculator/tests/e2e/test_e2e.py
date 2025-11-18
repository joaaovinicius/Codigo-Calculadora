from playwright.sync_api import sync_playwright

def test_frontend_e2e():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("C:/Projetos/TC-JOGO/Codigo-Calculadora/calculator/frontend/index.html")

        page.fill("#val1", "2")
        page.fill("#val2", "3")
        page.select_option("#op", "+")
        page.click("#btn")

        result = page.inner_text("#result")
        assert result == "5"

        browser.close()
