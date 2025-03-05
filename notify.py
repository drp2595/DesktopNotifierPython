import csv
import time
import datetime
import subprocess

def send_notification(title, message):
    subprocess.run(["notify-send", title, message])

def wait_until(target_time):
    while True:
        now = datetime.datetime.now()
        if now >= target_time:
            break
        time.sleep(10)

def read_csv_and_schedule(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            for row in reader:
                if len(row) != 4:
                    continue

                title, message, event_time, before_minutes = row
                
                try:
                    event_time = datetime.datetime.strptime(event_time, "%H:%M")
                    before_minutes = int(before_minutes)
                    
                    now = datetime.datetime.now()
                    event_datetime = now.replace(hour=event_time.hour, minute=event_time.minute, second=0, microsecond=0)

                    notify_time = event_datetime - datetime.timedelta(minutes=before_minutes)
                    if notify_time < now:
                        print(f"Skipping past notification: {title} at {notify_time.strftime('%H:%M')}")
                        continue
                    
                    print(f"Scheduled notification: {title} at {notify_time.strftime('%H:%M')}")
                    wait_until(notify_time)
                    send_notification(title, message)

                except ValueError:
                    print(f"Invalid time format in row: {row}")

    except FileNotFoundError:
        print("CSV file not found!")

if __name__ == "__main__":
    read_csv_and_schedule("data.csv")