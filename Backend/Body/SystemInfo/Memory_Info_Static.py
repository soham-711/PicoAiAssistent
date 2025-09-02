import psutil
import platform
import socket
import datetime
import os

def get_system_info():
    # System
    uname = platform.uname()
    hostname = socket.gethostname()

    # CPU
    try:
        freq = psutil.cpu_freq()
        base_speed = round(freq.min / 1000, 2) if freq else None
        current_speed = round(freq.current / 1000, 2) if freq else None
    except:
        base_speed, current_speed = None, None

    cpu_info = {
        "usage_percent": psutil.cpu_percent(interval=1),
        "cores": psutil.cpu_count(logical=False),
        "threads": psutil.cpu_count(logical=True),
        "base_speed_ghz": base_speed,
        "current_speed_ghz": current_speed,
        "temperature_c": None  # psutil doesn't give temps on Windows easily
    }

    # RAM
    svmem = psutil.virtual_memory()
    ram_info = {
        "total_gb": round(svmem.total / (1024**3), 1),
        "used_gb": round(svmem.used / (1024**3), 1),
        "available_gb": round(svmem.available / (1024**3), 1),
        "percent": svmem.percent
    }

    # Disks
    disks = {}
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            disks[part.device] = {
                "total_gb": round(usage.total / (1024**3), 1),
                "used_gb": round(usage.used / (1024**3), 1),
                "percent": usage.percent
            }
        except PermissionError:
            continue

    # Network
    net_io = psutil.net_io_counters()
    try:
        local_ip = socket.gethostbyname(hostname)
    except:
        local_ip = "Unknown"

    # Public IP (optional, needs internet)
    try:
        import requests
        public_ip = requests.get("https://api.ipify.org").text
    except:
        public_ip = "Unknown"

    interfaces = list(psutil.net_if_addrs().keys())
    network_info = {
        "local_ip": local_ip,
        "public_ip": public_ip,
        "bytes_sent_mb": round(net_io.bytes_sent / (1024**2), 1),
        "bytes_recv_mb": round(net_io.bytes_recv / (1024**2), 1),
        "interfaces": interfaces
    }

    # Battery
    battery = psutil.sensors_battery()
    if battery:
        battery_info = {
            "percent": battery.percent,
            "charging": battery.power_plugged,
            "time_remaining_min": round(battery.secsleft / 60, 1) if battery.secsleft > 0 else None
        }
    else:
        battery_info = {"percent": None, "charging": None, "time_remaining_min": None}

    # Timeline
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    timeline_info = {
        "boot_time": boot_time.strftime("%Y-%m-%d %H:%M:%S"),
        "uptime_hours": round(uptime.total_seconds() / 3600, 1),
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Top Processes
    processes = []
    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    top_processes = sorted(processes, key=lambda p: p["cpu_percent"], reverse=True)[:5]

    return {
        "system": {
            "os": uname.system,
            "os_version": uname.version,
            "architecture": uname.machine,
            "processor": uname.processor,
            "hostname": hostname
        },
        "cpu": cpu_info,
        "ram": ram_info,
        "disks": disks,
        "network": network_info,
        "battery": battery_info,
        "timeline": timeline_info,
        "top_processes": top_processes
    }
