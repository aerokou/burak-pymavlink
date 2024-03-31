from pymavlink import mavutil
import time

# Sim bağlantısı
address = "udp:127.0.0.1:14550"

# Gerçek bağlantı
# address = "/dev/ttyACM0"

vehicle=mavutil.mavlink_connection(address , baud=57600, autoreconnect=True)
print("Baglantı olustu")
vehicle.wait_heartbeat()
print("Drone geri sinyal verdi ")


def takeoff(alt):
    vehicle.set_mode("GUIDED")

    vehicle.arducopter_arm()

    print("Arm edildi")

    vehicle.mav.command_long_send(vehicle.target_system, vehicle.target_component, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0,0,0,0,0,0,alt)

    print ("8 metre yukseliyor ve en az 10 saniye bekleyecek")

    time.sleep(15)

    print("RTL mode geciyor")
    
    vehicle.set_mode("RTL")

takeoff(8)





