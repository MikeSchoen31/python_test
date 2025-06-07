import datetime
import requests
import tkinter as tk
from tkinter import messagebox

API_URL = "https://api.tradingeconomics.com/calendar/country/united%20states"
API_AUTH = "guest:guest"


def fetch_high_impact_news():
    today = datetime.date.today().isoformat()
    params = {
        "c": API_AUTH,
        "d1": today,
        "d2": today,
        "format": "json",
    }
    try:
        resp = requests.get(API_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as exc:
        messagebox.showerror("Network error", f"Could not fetch news: {exc}")
        return []

    filtered = []
    for item in data:
        importance = item.get("Importance")
        if importance in ("High", "3", 3):
            filtered.append(item)
    return filtered


def display_news(news_items):
    root = tk.Tk()
    root.title("News US - 3 étoiles")
    if not news_items:
        label = tk.Label(root, text="Aucune news 3 étoiles trouvée.")
        label.pack(padx=10, pady=10)
    else:
        for item in news_items:
            date = item.get("Date", "")
            event = item.get("Event", "")
            tk.Label(root, text=f"{date} - {event}").pack(anchor="w")
    root.mainloop()


def main():
    news = fetch_high_impact_news()
    display_news(news)


if __name__ == "__main__":
    main()
