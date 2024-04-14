import psutil
import time

def monitor_network_traffic(interval=1):
    prev_sent = psutil.net_io_counters().bytes_sent
    prev_recv = psutil.net_io_counters().bytes_recv
    while True:
        time.sleep(interval)
        sent = psutil.net_io_counters().bytes_sent
        recv = psutil.net_io_counters().bytes_recv
        sent_speed = (sent - prev_sent) / interval
        recv_speed = (recv - prev_recv) / interval
        print(f"Sent: {sent_speed / 1024:.2f} KB/s, Received: {recv_speed / 1024:.2f} KB/s")
        prev_sent = sent
        prev_recv = recv

if __name__ == '__main__':
    interval = int(input("Enter the monitoring interval (in seconds): "))
    monitor_network_traffic(interval)