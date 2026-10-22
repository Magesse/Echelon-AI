import requests
from bs4 import BeautifulSoup

SCRAPE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
REQUEST_TIMEOUT = 15

def fetch_html(url: str) -> BeautifulSoup | None:
    """URL'yi getirir, BeautifulSoup nesnesi döner. Hata olursa None döner."""
    try:
        resp = requests.get(url, headers=SCRAPE_HEADERS, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return BeautifulSoup(resp.text, "html.parser")
    except requests.RequestException as e:
        print(f"  [uyarı] Sayfa çekilemedi: {url} — {e}")
        return None

def extract_text(soup: BeautifulSoup, selector: str, default: str = "N/A") -> str:
    """CSS seçici ile eleman bulur, metnini döner."""
    el = soup.select_one(selector)
    return el.get_text(strip=True) if el else default

def extract_all_text(soup: BeautifulSoup, selector: str) -> list[str]:
    """CSS seçici ile tüm eşleşen elemanların metinlerini döner."""
    return [el.get_text(strip=True) for el in soup.select(selector)]