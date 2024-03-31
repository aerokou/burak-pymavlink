from pymavlink import mavutil
import time
# Sim bağlantısı
address = "udp:127.0.0.1:14550"

# Gerçek bağlantı
# address = "/dev/ttyACM0"
print("address onaylandı")
vehicle=mavutil.mavlink_connection(address , baud=57600, autoreconnect=True)
print("baglantı olustu")
vehicle.wait_heartbeat()
print(" drone geri sinyal verdi ")

#Buldugumuz drone idye gore istedigimiz drone u fonksiyona atıcaz

def takeoff(alt , droneid):
    vehicle.set_mode("GUIDED")

    vehicle.arducopter_arm()

    print("Arm edildi")

    vehicle.mav.command_long_send(droneid,mavutil.mavlink.MAV_COMP_ID_SYSTEM_CONTROL,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0,0,0,0,0,0,alt)

    print ("8 metre yukseliyor ve en az 10 saniye bekleyecek")

    time.sleep(15)

    print("RTL mode geciyor")
    
    vehicle.set_mode("RTL")

takeoff(8,1)





