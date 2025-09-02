import psutil
import socket
import speedtest

def get_network_details():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    # Assume first active interface
    wifi_stats = psutil.net_if_stats()
    network_id = None
    for iface, stats in wifi_stats.items():
        if stats.isup:
            network_id = iface
            break

    # Speed test
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download = round(st.download() / 1_000_000, 2)
        upload = round(st.upload() / 1_000_000, 2)
        ping = round(st.results.ping, 2)
    except:
        download, upload, ping = None, None, None

    network_info = {
        "ip_address": ip_address,
        "network_id": network_id or "Unknown",
        "speed": {
            "download_mbps": download,
            "upload_mbps": upload,
            "ping_ms": ping
        },
        "signal_strength": "100%"  # Windows API/WMI required for actual Wi-Fi strength
    }
    return network_info
