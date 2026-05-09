import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# File for storage
JSON_FILE = "data.json"

# Data structure
data = []


def update_summary():
    # Sum all "per_day" values
    total_msups = sum(entry["per_day"] for entry in data)

    # Calculate salvage costs
    salvage_costs = total_msups * 7.5

    # Update labels
    label_total_value.config(text=str(int(total_msups)))
    label_costs_value.config(text=str(int(salvage_costs)))


def load_data():
    global data

    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Fill table
            for entry in data:
                tree.insert(
                    "",
                    tk.END,
                    values=(
                        entry["key"],
                        entry["value"],
                        entry["per_day"],
                        entry["three_days"]
                    )
                )

            update_summary()

        except Exception as e:
            messagebox.showerror("Error", f"Error while loading:\n{e}")


def save_data():
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    except Exception as e:
        messagebox.showerror("Error", f"Error while saving:\n{e}")


def add_entry():
    key = entry_key.get().strip()
    value = entry_value.get().strip()

    if not key:
        messagebox.showwarning("Warning", "Please enter a description.")
        return

    if not value:
        messagebox.showwarning("Warning", "Please enter a Msups Amount.")
        return

    try:
        value = int(value)
    except ValueError:
        messagebox.showwarning("Warning", "The second input must be a number.")
        return

    # Calculations
    per_day = value * 24
    three_days = per_day * 3

    # Create dataset
    entry = {
        "key": key,
        "value": value,
        "per_day": per_day,
        "three_days": three_days
    }

    # Add to list
    data.append(entry)

    # Update table
    tree.insert(
        "",
        tk.END,
        values=(
            key,
            value,
            per_day,
            three_days
        )
    )

    # Save JSON
    save_data()

    # Update labels
    update_summary()

    # Clear input fields
    entry_key.delete(0, tk.END)
    entry_value.delete(0, tk.END)

    # Focus back to first field
    entry_key.focus()


# Create window
root = tk.Tk()
root.title("Data Entry")
root.geometry("850x500")

# =========================
# INPUT AREA
# =========================

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

# Description
label_key = tk.Label(frame_input, text="Description:")
label_key.grid(row=0, column=0, padx=5, pady=5)

entry_key = tk.Entry(frame_input, width=25)
entry_key.grid(row=0, column=1, padx=5, pady=5)

# Number
label_value = tk.Label(frame_input, text="Number:")
label_value.grid(row=0, column=2, padx=5, pady=5)

entry_value = tk.Entry(frame_input, width=25)
entry_value.grid(row=0, column=3, padx=5, pady=5)

# Button
button_add = tk.Button(
    frame_input,
    text="Submit",
    command=add_entry
)
button_add.grid(row=0, column=4, padx=10)

# =========================
# SUMMARY AREA
# =========================

frame_summary = tk.Frame(root)
frame_summary.pack(pady=10)

# Label 1
label_total_text = tk.Label(
    frame_summary,
    text="Total Msups Consumption:"
)
label_total_text.grid(row=0, column=0, padx=10, sticky="e")

# Label 2
label_total_value = tk.Label(
    frame_summary,
    text="0",
    width=15,
    anchor="w"
)
label_total_value.grid(row=0, column=1, padx=10, sticky="w")

# Label 3
label_costs_text = tk.Label(
    frame_summary,
    text="Costs in Salvage:"
)
label_costs_text.grid(row=0, column=2, padx=10, sticky="e")

# Label 4
label_costs_value = tk.Label(
    frame_summary,
    text="0",
    width=15,
    anchor="w"
)
label_costs_value.grid(row=0, column=3, padx=10, sticky="w")

# =========================
# TABLE AREA
# =========================

frame_table = tk.Frame(root)
frame_table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Columns
columns = ("key", "value", "per_day", "three_days")

tree = ttk.Treeview(frame_table, columns=columns, show="headings")

# Headings
tree.heading("key", text="Description")
tree.heading("value", text="Msups per Hour")
tree.heading("per_day", text="Per Day")
tree.heading("three_days", text="3 Days")

# Column widths
tree.column("key", width=250)
tree.column("value", width=150)
tree.column("per_day", width=150)
tree.column("three_days", width=150)

tree.pack(fill=tk.BOTH, expand=True)

# Bind Enter key to input function
root.bind("<Return>", lambda event: add_entry())

# Load existing data
load_data()

# Start GUI
root.mainloop()