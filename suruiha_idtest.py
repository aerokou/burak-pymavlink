from pymavlink import mavutil

# Sim bağlantısı
# address = "udp:127.0.0.1:14550"

# Gerçek bağlantı
address = "/dev/ttyACM0"
print("address onaylandı")
vehicle=mavutil.mavlink_connection(address , baud=57600, autoreconnect=True)
print("baglantı olustu")
vehicle.wait_heartbeat()
print(" drone geri sinyal verdi ")

#Burada sistem idsini test edip kenara not alıyoruz

message= vehicle.recv_match(type="HEARTBEAT" , blocking=True)

print("Drone idsi: ", message.get_srcSystem())
print("Sistem tipi:" , message.get_type())
