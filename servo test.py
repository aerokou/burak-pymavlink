from pymavlink import mavutil
import time


connection = mavutil.mavlink_connection('/dev/ttyACM0')

# Servo hareketi için fonksiyon
def move_servo(channel, pwm_value):
    msg = connection.mav.command_long_encode(
        1,                      # Sistem numarası
        1,                      # Bileşen numarası
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO, # Komut
        0,                      # Confirmation
        channel,                # Kanal numarası
        pwm_value,              # PWM değeri
        0, 0, 0, 0, 0)          # Parametreler
    connection.mav.send(msg)

try:
    while True:
        
        move_servo(0, 1500)  
        time.sleep(1)        
        move_servo(0, 2000)  
        time.sleep(1)        

except KeyboardInterrupt:
    pass
