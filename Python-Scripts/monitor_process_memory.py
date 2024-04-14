import psutil
import time

def monitor_process_memory(process_name, interval=1):
    while True:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == process_name:
                mem_usage = proc.memory_info().rss / (1024 * 1024)
                print(f"{process_name} memory usage: {mem_usage:.2f} MB")
        time.sleep(interval)

if __name__ == '__main__':
    process_name = input("Enter the process name to monitor: ")
    interval = int(input("Enter the monitoring interval (in seconds): "))
    monitor_process_memory(process_name, interval)