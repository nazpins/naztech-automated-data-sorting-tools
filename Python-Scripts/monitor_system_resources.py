import psutil
import time

def monitor_system_resources(interval=1):
    while True:
        cpu_percent = psutil.cpu_percent()
        mem_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent
        print(f"CPU Usage: {cpu_percent}%, Memory Usage: {mem_percent}%, Disk Usage: {disk_percent}%")
        time.sleep(interval)

if __name__ == '__main__':
    interval = int(input("Enter the monitoring interval (in seconds): "))
    monitor_system_resources(interval)