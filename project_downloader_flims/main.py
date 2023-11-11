import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import webbrowser
import re
import itertools
import moudel
import downloader

def link():
    proxies = {
        "http": "85.114.120.177:9999"
    }
    url = downloader.correct_link(film_entry.get())
    if requests.get(url).status_code != 200:
        messagebox.showerror("Error", "this film not exist")

    if not film_entry.get():
        messagebox.showerror("Error", "You must enter a film name.")
        return

    req = requests.get(url, proxies=proxies)
    src = req.content
    html = BeautifulSoup(src, "lxml")
    
    lista = []
    ul_elements = html.find_all('ul', class_='List--Download--Wecima--Single')

    for ul_element in ul_elements:
        links = ul_element.find_all('a', class_='hoverable activable')

        for x in links:
            if "1080p" in str(x):
                link2 = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(x))
            elif "720p" in str(x):
                link2 = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(x))
                lista.append(link2)
            elif "480p" in str(x):
                link2 = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(x))
                lista.append(link2)
            elif "360p" in str(x):
                link2 = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(x))
                lista.append(link2)
            elif "240p" in str(x):
                link2 = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(x))
                lista.append(link2)

    flattened_list = list(itertools.chain.from_iterable(lista))

    modified_lista = []
    for jo in flattened_list:
        modified_link = moudel.delate_part_of_linK(jo)
        modified_lista.append(modified_link)
    
    film_name = str(film_entry.get())
    quality_selection = quality_listbox.curselection()
    
    if not quality_selection:
        messagebox.showerror("Error", "You must select a quality.")
    elif not film_name:
        messagebox.showerror("Error", "You must enter a film name.")
    elif not quality_selection and not film_name:
        messagebox.showerror("Error", "You must enter a film name and choose quality.")
    else:
        quality_index = quality_selection[0]
        if quality_index == 0:
            webbrowser.open(modified_lista[0])
        elif quality_index == 1:
            webbrowser.open(modified_lista[1])
        elif quality_index == 2:
            webbrowser.open(modified_lista[2])
        else:
            messagebox.showerror("Error", "This quality does not exist. Choose another quality.")

window = tk.Tk()
window.geometry("700x500")
window.configure(background="Navy blue")
window.title("Film Downloader")

film_label = tk.Label(window, text="Enter the name of a film", pady=10, padx=40, bg="Navy blue", fg="Gray", font=("Helvtica", 15), borderwidth=1)
film_label.pack(pady=10)

film_entry = tk.Entry(window, width=30, font=("Helvtica", 20), bg="Gray", fg="Fuchsia")
film_entry.pack()

label_lista = tk.Label(window, text="Choose quality for download", pady=10, padx=40, bg="Navy blue", fg="Gray", font=("Helvtica", 15), borderwidth=1)
label_lista.pack(padx=10, pady=20)

quality_listbox = tk.Listbox(window, height=3, width=38, bg="Navy blue", fg="Gray", font=("Helvtica", 15), borderwidth=1)
quality_listbox.config(highlightbackground="Navy blue", highlightcolor="Navy blue")
quality_listbox.insert(1, 'High quality')
quality_listbox.insert(2, 'Average quality')
quality_listbox.insert(3, 'Low quality')
quality_listbox.pack()

download_button = tk.Button(window, text="Download", command=link, width=25, bg="Navy blue", fg="Gray", font=("Helvtica", 20), borderwidth=1)
download_button.pack(pady=20)

window.mainloop()