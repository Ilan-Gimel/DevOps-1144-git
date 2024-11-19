#              Logging Internet Speed              #
import speedtest
import datetime
import os
def speedrun():
# Create a Speedtest object
    steelpath = speedtest.Speedtest()

# Get the best server based on ping
    steelpath.get_best_server()

# Perform the speed test for download, upload, and ping
    download_speed = steelpath.download()  # in bits per second
    upload_speed = steelpath.upload()      # in bits per second
    ping = steelpath.results.ping          # in ms

# Convert from bits to megabits (1 Mbps = 1 million bits)
    download_speed_mbps = download_speed / 1_000_000
    upload_speed_mbps = upload_speed / 1_000_000
    return download_speed_mbps,upload_speed_mbps,ping

def speed_test():
    date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    downsp,upsp,ping=speedrun()
    file_path='/Users/ilangimelfarb/Documents/GitHub/DevOps-1144-git/Python/SpeedTest.csv'
    # Check if File exists if not then create 
    if os.path.exists(file_path)==False:
        file=open(file_path, 'x')
        file.close()
    # Check if file is empty (no header),If empty write header
    file=open(file_path, 'r')
    if file.read(1)=='':
        file.close()
        file=open(file_path, 'w')
        file.write(f'Timestamp, Download Speed (Mbps), Upload Speed (Mbps), Ping (ms)\n')
        file.close()
    #Write Time stamps and data of the speed test
    file=open(file_path, 'a')
    file.write(f'{date}, {downsp}, {upsp}, {ping}\n')
    file.close()
    


speed_test()













