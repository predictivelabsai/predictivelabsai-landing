"""
Boots the FastHTML app in a subprocess, visits each route with Playwright
(sync API), writes a full-page screenshot into screenshots/, and asserts the
expected h1 is present. Independent of the Claude MCP Playwright runner.

Run:
    pip install playwright pytest
    python -m playwright install chromium
    python -m pytest tests/test_pages.py -v
"""

import subprocess
import time
import socket
from pathlib import Path

import pytest

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    pytest.skip("playwright not installed", allow_module_level=True)


ROOT = Path(__file__).parent.parent
SCREENSHOTS = ROOT / "screenshots"
SCREENSHOTS.mkdir(exist_ok=True)

HOST = "127.0.0.1"
PORT = 5011  # different from dev server (5001) to avoid clashes

ROUTES = [
    ("/", "home", "public good"),
    ("/platform", "platform", "platform"),
    ("/solutions/defense", "solutions-defense", "operational"),
    ("/solutions/healthcare", "solutions-healthcare", "evidence"),
    ("/solutions/public", "solutions-public", "operational insight"),
    ("/solutions/financial", "solutions-financial", "selectively"),
    ("/case-studies", "case-studies", "Engagements"),
    ("/signal", "signal", "Public-sector data"),
    ("/open-source", "open-source", "commons"),
    ("/partners", "partners", "Specialists"),
    ("/team", "team", "small group"),
    ("/contact", "contact", "programme"),
]


def _wait_for_port(host: str, port: int, timeout: float = 15.0):
    start = time.time()
    while time.time() - start < timeout:
        with socket.socket() as s:
            try:
                s.connect((host, port))
                return
            except OSError:
                time.sleep(0.2)
    raise TimeoutError(f"server on {host}:{port} did not come up")


@pytest.fixture(scope="session")
def server():
    env_cmd = [
        ".venv/bin/python", "-m", "uvicorn", "app:app",
        "--host", HOST, "--port", str(PORT),
    ]
    proc = subprocess.Popen(
        env_cmd,
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    try:
        _wait_for_port(HOST, PORT)
        yield f"http://{HOST}:{PORT}"
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


@pytest.mark.parametrize("path,slug,expected", ROUTES)
def test_route(server, path, slug, expected):
    url = f"{server}{path}"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        page = ctx.new_page()
        page.goto(url, wait_until="networkidle")

        if path == "/signal":
            # wait for plotly to render at least one chart
            page.wait_for_selector(".plotly-graph-div svg", timeout=5000)

        h1_text = page.locator("h1").first.inner_text()
        assert expected.lower() in h1_text.lower(), f"{path}: h1 '{h1_text}' does not contain '{expected}'"

        page.screenshot(path=str(SCREENSHOTS / f"test-{slug}.png"), full_page=True)
        browser.close()


def test_partners_page_lists_five_external_partners(server):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(server + "/partners", wait_until="networkidle")

        cards = page.locator("main article")
        assert cards.count() == 5
        assert cards.filter(has_text="Predictive Labs").count() == 0
        assert page.locator("nav ul").first.get_by_role("link", name="Partners").count() == 1
        assert cards.filter(has_text="SAASPASS").get_by_role("link", name="Visit website").get_attribute("href") == "https://saaspass.com/"
        assert cards.filter(has_text="Manmouna Technologies").get_by_role("link", name="Visit website").get_attribute("href") == "https://manmouna.tech/"

        browser.close()


def test_footer_groups_six_predictive_labs_entities_by_region(server):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(server + "/contact", wait_until="networkidle")

        footer = page.locator("footer")
        assert footer.get_by_role("table").count() == 3

        emea = footer.get_by_role("table", name="Predictive Labs legal entities — EMEA")
        americas = footer.get_by_role("table", name="Predictive Labs legal entities — Americas")
        apac = footer.get_by_role("table", name="Predictive Labs legal entities — APAC")
        assert emea.locator("tbody tr").count() == 3
        assert americas.locator("tbody tr").count() == 2
        assert apac.locator("tbody tr").count() == 1
        assert footer.get_by_text("Manmouna", exact=False).count() == 0
        assert emea.get_by_text("Predictive Labs OÜ · Registry 12061679", exact=True).count() == 1
        assert emea.get_by_text("Ravala 6, Tallinn", exact=True).count() == 1
        assert apac.get_by_text("Predictive Labs Limited · Co. 9448513 · NZBN 9429053855695", exact=True).count() == 1
        assert page.locator("main").get_by_text("Manmouna", exact=False).count() == 0
        assert page.locator("main").get_by_text("Ravala 6, Tallinn", exact=True).count() == 1
        assert page.locator("main").get_by_text("New Zealand", exact=True).count() == 1

        browser.close()
