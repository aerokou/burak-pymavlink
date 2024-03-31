from pymavlink import mavutil

# Sim bağlantısı
address = "udp:127.0.0.1:14550"

# Gerçek bağlantı
# address = "/dev/ttyACM0"
print("address onaylandı")
vehicle=mavutil.mavlink_connection(address , baud=57600, autoreconnect=True)
print("baglantı olustu")
vehicle.wait_heartbeat()
print(" drone geri sinyal verdi ")


message= vehicle.recv_match(type="BATTERY_STATUS" , blocking=True)
print(f"Batarya yuzdesi bu kanks  : {message.battery_remaining}")


message= vehicle.recv_match(type="HEARTBEAT" , blocking=True)

mode = mavutil.mode_string_v10(message)
print(f"Anlık mod :{mode}")
