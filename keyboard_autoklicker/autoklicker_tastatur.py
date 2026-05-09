import tkinter as tk
from tkinter import messagebox
import threading
import time

# Benötigte Bibliothek:
# pip install keyboard
import keyboard

running = False


def auto_press():
    global running

    while running:
        keys = entry_keys.get().strip()
        interval = entry_interval.get().strip()

        if not keys:
            messagebox.showerror("Fehler", "Bitte mindestens eine Taste eingeben.")
            running = False
            return

        try:
            delay = float(interval)
        except ValueError:
            messagebox.showerror("Fehler", "Ungültiges Intervall.")
            running = False
            return

        key_list = keys.split(",")

        for key in key_list:
            if not running:
                break

            key = key.strip()

            try:
                keyboard.press_and_release(key)
            except:
                print(f"Ungültige Taste: {key}")

        time.sleep(delay)


def start_clicking():
    global running

    if running:
        return

    running = True

    thread = threading.Thread(target=auto_press)
    thread.daemon = True
    thread.start()

    status_label.config(text="Status: Läuft")


def stop_clicking():
    global running

    running = False
    status_label.config(text="Status: Gestoppt")


def toggle_clicking():
    global running

    if running:
        stop_clicking()
    else:
        start_clicking()


# Hotkey registrieren
keyboard.add_hotkey("F5", toggle_clicking)

# Fenster erstellen
root = tk.Tk()
root.title("Auto Key Clicker")
root.geometry("350x250")
root.resizable(False, False)

# Überschrift
title_label = tk.Label(
    root,
    text="Auto Tastendrücker",
    font=("Arial", 14, "bold")
)
title_label.pack(pady=10)

# Tasten Eingabe
label_keys = tk.Label(root, text="Tasten (mit Komma trennen):")
label_keys.pack()

entry_keys = tk.Entry(root, width=35)
entry_keys.pack(pady=5)
entry_keys.insert(0, "a,b,space")

# Intervall Eingabe
label_interval = tk.Label(root, text="Intervall in Sekunden:")
label_interval.pack()

entry_interval = tk.Entry(root, width=10)
entry_interval.pack(pady=5)
entry_interval.insert(0, "1")

# Buttons
btn_start = tk.Button(
    root,
    text="Start",
    width=15,
    command=start_clicking
)
btn_start.pack(pady=5)

btn_stop = tk.Button(
    root,
    text="Stop",
    width=15,
    command=stop_clicking
)
btn_stop.pack(pady=5)

# Statusanzeige
status_label = tk.Label(
    root,
    text="Status: Gestoppt",
    fg="red"
)
status_label.pack(pady=10)

# Info
info_label = tk.Label(
    root,
    text="F5 = Start / Stop",
    font=("Arial", 9)
)
info_label.pack()

# Fenster starten
root.mainloop()