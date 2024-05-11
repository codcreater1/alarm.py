import tkinter as tk
import time
import winsound

class AlarmClockApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Alarm Clock")
        self.geometry("300x300")

        self.alarms = []

        self.create_widgets()

    def create_widgets(self):
        self.current_time_label = tk.Label(self, text="")
        self.current_time_label.pack()

        self.alarms_label = tk.Label(self, text="Alarms:")
        self.alarms_label.pack()

        self.alarms_listbox = tk.Listbox(self)
        self.alarms_listbox.pack()

        self.hour_label = tk.Label(self, text="Hour:")
        self.hour_label.pack()

        self.hour_entry = tk.Entry(self)
        self.hour_entry.pack()

        self.minute_label = tk.Label(self, text="Minute:")
        self.minute_label.pack()

        self.minute_entry = tk.Entry(self)
        self.minute_entry.pack()

        self.set_alarm_button = tk.Button(self, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack()

        self.remove_alarm_button = tk.Button(self, text="Remove Alarm", command=self.remove_alarm)
        self.remove_alarm_button.pack()

        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.current_time_label.config(text=f"Current time: {current_time}")
        self.after(1000, self.update_time)

    def set_alarm(self):
        hour = self.hour_entry.get()
        minute = self.minute_entry.get()
        if hour.isdigit() and minute.isdigit():
            self.alarms.append((int(hour), int(minute)))
            self.update_alarms()

    def remove_alarm(self):
        selection = self.alarms_listbox.curselection()
        if selection:
            index = selection[0]
            del self.alarms[index]
            self.update_alarms()

    def update_alarms(self):
        self.alarms_listbox.delete(0, tk.END)
        for alarm in self.alarms:
            self.alarms_listbox.insert(tk.END, f"{alarm[0]:02d}:{alarm[1]:02d}")

def main():
    app = AlarmClockApp()
    app.mainloop()

if __name__ == "__main__":
    main()
