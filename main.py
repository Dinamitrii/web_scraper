import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup


def scrape():
    url = url_entry.get()
    tag_name = tag_entry.get()


    if not url:
        messagebox.showerror("Input error", "Please enter a URL")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        titles = soup.find_all(tag_name)

        output_text.delete("1.0", tk.END)
        for i, title in enumerate(titles, 1):
            output_text.insert(tk.END, f"{i}. {title.get_text(strip=True)}\n")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network error", f"Failed to fetch the webpage: {e}")



root = tk.Tk()
root.title("Scrape")
root.option_add("*Font", ("Arial", 16))

url_label = tk.Label(root, text="Website URL:")
url_label.grid(column=0, row=0, padx=10, pady=10, sticky="w")

url_entry = tk.Entry(root, width=50)
url_entry.grid(column=1, row=0, padx=10, pady=10, sticky="w")

tag_label = tk.Label(root, text="Tag:")
tag_label.grid(column=2, row=0, padx=10, pady=10, sticky="w")

tag_entry = tk.Entry(root, width=25)
tag_entry.grid(column=3, row=0, padx=10, pady=10, sticky="w")

scrape_button = tk.Button(root, text="Scrape", command=scrape)
scrape_button.grid(column=4, row=0, padx=10, pady=10)

output_text = tk.Text(root, wrap=tk.WORD, height=25, width=70)
output_text.grid(column=0, row=1, columnspan=5, padx=10, pady=10, sticky="w")

root.mainloop()
