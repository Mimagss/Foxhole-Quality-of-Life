````md id="f63u2m"
# Auto Key Clicker

A simple Auto Key Clicker built with Python and Tkinter.

This application automatically presses keyboard keys at a configurable interval and can be started or stopped using the `F5` hotkey.

---

# Features

- Automates keyboard key presses
- Supports multiple keys
- Adjustable interval
- Start and stop via GUI
- Global hotkey support (`F5`)
- Simple Tkinter interface

---

# Requirements

- Python 3

Required library:

```bash
pip install keyboard
````

---

# Run the Program

```bash id="ef2lqs"
python main.py
```

---

# Usage

## Enter Keys

Separate multiple keys with commas.

Examples:

```text id="e6p40j"
r
```

```text id="5d5wio"
r,v
```

```text id="93m2dg"
space,enter
```

```text id="hk1mwy"
w,a,s,d
```

---

## Set the Interval

The interval is specified in seconds.

Examples:

| Value | Meaning         |
| ----- | --------------- |
| 1     | every second    |
| 0.5   | every 500 ms    |
| 2     | every 2 seconds |

---

# Controls

| Key / Button | Function                |
| ------------ | ----------------------- |
| F5           | Start / Stop            |
| Start Button | Starts the auto clicker |
| Stop Button  | Stops the auto clicker  |

---

# Supported Keys

Examples:

* a-z
* 0-9
* enter
* space
* shift
* ctrl
* alt
* up
* down
* left
* right

---

# Notes

* The application uses global keyboard hooks.
* Some games may not accept simulated keyboard input.

---

# Project Structure

```text id="pq4b4g"
project/
│
├── main.py
└── README.md
```

---