import speedtest

wifi = speedtest.Speedtest()

print("Download:", round(wifi.download() / 1000000,2), "Mbps")
print("Upload:", round(wifi.upload() / 1000000,2), "Mbps")

wifi.get_servers([])
print("Ping:", wifi.results.ping)
