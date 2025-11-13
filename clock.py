# from tkinter import *
# import time
#
# from numpy.random import laplace
#
# window=Tk()
# window.title("My 24-Hour Digital Clock")
# window.configure(bg="#1a1a1a")
# window.geometry("500x500")
# label=Label(text="my label",height=20,width=40)
# label.pack()
#
#
#
#
#
#
#
# window.mainloop()


from tkinter import *
import time

# Step 1: Create main window


# window = Tk()
# window.title("24-Hour Digital Clock (Independent)")
# window.configure(bg="#1a1a1a")
# window.geometry("500x300")
# window.resizable(False, False)
#
# # Step 2: Create display label
# label = Label(window,
#               text="00:00:00",
#               font=("DS-Digital", 60, "bold"),
#               fg="cyan",
#               bg="#1a1a1a")
# label.pack(pady=80)
#
# # Step 3: Initialize time counter (in seconds)
# seconds = 0
#
# # Step 4: Define update function
# def update_clock():
#     global seconds
#     # Convert total seconds → hours, minutes, seconds
#     hours = (seconds // 3600) % 24
#     minutes = (seconds % 3600) // 60
#     secs = seconds % 60
#
#     # Format time nicely
#     time_display = f"{hours:02d}:{minutes:02d}:{secs:02d}"
#     label.config(text=time_display)
#
#     # Step 5: Increase time
#     seconds += 1
#     if seconds >= 86400:  # 24 hours * 3600 seconds = 86400
#         seconds = 0  # Reset to 0 after 24 hours
#
#     # Step 6: Repeat every second
#     window.after(1000, update_clock)
#
# # Start clock
# update_clock()
#
# window.mainloop()


from tkinter import *
import time

# Create window
window = Tk()
window.title("24-Hour Digital Clock")
window.configure(bg="#1a1a1a")
window.geometry("400x300")

# Global variables for time
hour = 0
minute = 0
second = 0

# Label to show the clock
time_label = Label(window, text="", font=("DS-Digital", 48), fg="lime", bg="#1a1a1a")
time_label.pack(pady=20)


# Function to update clock display
def update_clock():
    global hour, minute, second

    # Increment seconds
    second_inc()
    # Display formatted time
    time_label.config(text=f"{hour:02d}:{minute:02d}:{second:02d}")

    # Call this function again after 1000 ms
    window.after(1000, update_clock)


# Function to handle second increment with rollover
def second_inc():
    global hour, minute, second
    second += 1
    if second == 60:
        second = 0
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour == 24:
                hour = 0


# Function to set a new time value (hour, minute, or second)
def set_time(unit):
    def apply_new_time():
        global hour, minute, second
        new_value = entry.get()
        if new_value.isdigit():
            value = int(new_value)
            if unit == "hour" and 0 <= value < 24:
                hour = value
            elif unit == "minute" and 0 <= value < 60:
                minute = value
            elif unit == "second" and 0 <= value < 60:
                second = value
            top.destroy()
        else:
            entry.delete(0, END)
            entry.insert(0, "Invalid")

    # Popup window to input new time
    top = Toplevel(window)
    top.title(f"Set {unit}")
    Label(top, text=f"Enter new {unit}:", font=("Arial", 12)).pack(pady=5)
    entry = Entry(top)
    entry.pack(pady=5)
    Button(top, text="Apply", command=apply_new_time).pack(pady=5)


# Create buttons
button_frame = Frame(window, bg="#1a1a1a")
button_frame.pack(pady=20)

Button(button_frame, text="Set Hour", command=lambda: set_time("hour"), bg="gray", fg="white").grid(row=0, column=0,
                                                                                                    padx=10)
Button(button_frame, text="Set Minute", command=lambda: set_time("minute"), bg="gray", fg="white").grid(row=0, column=1,
                                                                                                        padx=10)
Button(button_frame, text="Set Second", command=lambda: set_time("second"), bg="gray", fg="white").grid(row=0, column=2,
                                                                                                        padx=10)

# Start clock
update_clock()

window.mainloop()

