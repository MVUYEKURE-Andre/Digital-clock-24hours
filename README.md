# Digital-clock-24hours
digital clock project using python

🕒 24-Hour Digital Clock (Tkinter)

<img width="1919" height="908" alt="andre clock" src="https://github.com/user-attachments/assets/9122250c-b01f-4a43-b6f7-8641bc66dc60" />


A clean, interactive 24-hour digital clock built with Python’s Tkinter framework.
This app simulates a real digital clock with the ability to manually set hours, minutes, and seconds — great for learning GUI programming and time handling in Python.

<img width="1838" height="917" alt="Andre&#39;s clock python project" src="https://github.com/user-attachments/assets/ccd6ffc2-6cdc-49da-a3df-d4eafff9d2fb" />


🌟 Features
Feature	Description
⏱ Real-time Clock	Updates every second, showing HH:MM:SS in 24-hour format
🔄 Auto Rollover	Seconds → Minutes → Hours rollover implemented
🔧 Manual Time Setting	Set Hour, Minute, or Second through popup dialog
🎨 LED Digital Look	Green DS-Digital style font on dark UI
🧱 Pure Tkinter	No external libraries required
🪶 Lightweight	Under 150 lines of simple, readable Python
🧩 Project Structure
Digital-clock-24hours/
│── clock.py        # Main Tkinter application
│── group.png       # Screenshot preview
│── README.md       # Documentation

🚀 Installation & Running
1️⃣ Clone the repository
git clone https://github.com/your-username/Digital-clock-24hours.git

2️⃣ Navigate into the project
cd Digital-clock-24hours

3️⃣ Run the app
python clock.py


The 24-hour digital clock window will open.
<img width="1919" height="908" alt="andre clock" src="https://github.com/user-attachments/assets/263725c9-70c8-4495-8972-ab916b2d7aed" />


🛠 Code Breakdown
🔹 Time Update Logic

Keeps your display updating every second:

time_label.config(text=f"{hour:02d}:{minute:02d}:{second:02d}")
window.after(1000, update_clock)

🔹 Second → Minute → Hour Rollover
if second == 60:
    second = 0
    minute += 1

🔹 Manual Time Setter
if unit == "hour" and 0 <= value < 24:
    hour = value


Popup dialogs make it easy to update the clock.

🧠 Learning Objectives

This project helps beginners understand:

Tkinter GUI basics

Using after() for timed events

Handling global state

Input validation

Creating popup windows with Toplevel()

📌 Future Enhancements

You can continue improving the project by adding:

⏰ Alarm system

📅 Date display

🌓 Light/Dark mode toggle

🔊 Sound on alarm

🎛 Settings menu

🎨 Digital font embedding (DS-Digital.ttf)

🤝 Contributing

Contributions are welcome!
To contribute:

Fork the repo

Create a new branch

Add your improvements

Open a Pull Request

<img width="1864" height="969" alt="andre clocks" src="https://github.com/user-attachments/assets/25c7570d-60e1-4a15-ae38-50372685b9a5" />

