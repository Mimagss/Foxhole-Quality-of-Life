    # README

## Overview

This application is a simple desktop tool written in Python using Tkinter.
It allows users to enter named MSUPS values, automatically calculate daily and 3-day totals, display all entries in a table, and persist the data in a JSON file.

The application also provides live summary statistics:

* Total MSUPS consumption per day
* Salvage costs based on the total daily consumption

---

## Features

* Tkinter-based graphical user interface
* Add entries consisting of:

  * Description
  * MSUPS per Hour
* Automatic calculations:

  * Per Day (`value * 24`)
  * 3 Days (`per_day * 3`)
* Automatic summary calculations:

  * Total MSUPS Consumption
  * Costs in Salvage (`total_per_day * 7.5`)
* Persistent JSON storage
* Automatic loading of saved data on startup
* Enter key support for fast input

---

## Data Structure

Each entry is stored in the following format:

```json
[
    {
        "key": "Example",
        "value": 10,
        "per_day": 240,
        "three_days": 720
    }
]
```

The summary values are calculated dynamically and are not stored in the JSON file.

---

## Requirements

* Python 3.x

Tkinter is included in most Python installations.

---

## Run the Application

Execute the Python file:

```bash
python msups_gui.py
```

Replace `main.py` with the actual filename if different.

---

## File Storage

The application automatically creates and updates:

```text
data.json
```

This file stores all table entries persistently.

---

## User Interface

### Input Area

* Description field
* Number input field
* Submit button

### Summary Area

Displays:

* Total Msups Consumption
* Costs in Salvage

### Table Area

Displays all entries with the following columns:

| Column         | Description          |
| -------------- | -------------------- |
| Description    | User-defined label   |
| Msups per Hour | Original input value |
| Per Day        | Hourly value × 24    |
| 3 Days         | Daily value × 3      |

---

## Behavior

* Every new entry is:

  * Added to the table
  * Stored in memory
  * Written to `data.json`
* Summary values update automatically after each input
* Existing data is restored automatically when the application starts

---

## Technologies Used

* Python
* Tkinter
* JSON
