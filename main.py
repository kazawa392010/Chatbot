import network
import time
from machine import Pin
from umqtt.simple import MQTTClient

# 1. Cấu hình thông tin kết nối
WIFI_SSID = "Khang Phat"
WIFI_PASS = "khangphat2010"
MQTT_BROKER = "test.mosquitto.org"
TOPIC_NHAN = b"nhacuatui/den_led"       # Web gửi lệnh vào đây
TOPIC_GUI = b"nhacuatui/trangthaiden"  # ESP32 gửi phản hồi vào đây

# 2. Cấu hình chân LED (Chân số 2 là LED xanh mặc định trên ESP32)
led = Pin(2, Pin.OUT)

# 3. Hàm kết nối Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Đang kết nối Wi-Fi...')
        wlan.connect(WIFI_SSID, WIFI_PASS)
        
        # Thử kết nối trong 10 giây
        timeout = 10
        start_time = time.time()
        while not wlan.isconnected():
            if time.time() - start_time > timeout:
                print("Kết nối Wi-Fi thất bại! Dừng chương trình.")
                return False
            time.sleep(0.5)
            
    print('Đã kết nối Wi-Fi:', wlan.ifconfig())
    return True

# 4. Hàm xử lý khi nhận được tin nhắn từ Web
def callback_tin_nhan(topic, msg):
    lenh = msg.decode('utf-8')
    print("Nhận được lệnh:", lenh)
    
    if lenh == "ON":
        led.value(1) # Bật LED
        phan_hoi = "Đèn đang BẬT"
    elif lenh == "OFF":
        led.value(0) # Tắt LED
        phan_hoi = "Đèn đang TẮT"
    else:
        phan_hoi = "Lệnh không hợp lệ"

    # Gửi phản hồi ngược lại Web để hiển thị lên thẻ <p>
    client.publish(TOPIC_GUI, phan_hoi)

# 5. Chương trình chính
if connect_wifi():
    client = MQTTClient("ESP32_Kazawa", MQTT_BROKER)
    client.set_callback(callback_tin_nhan)
    
    try:
        client.connect()
        client.subscribe(TOPIC_NHAN)
        print("Đã kết nối MQTT và đợi lệnh...")
        
        # Gửi thông báo chào mừng lên Web khi mới kết nối
        client.publish(TOPIC_GUI, "ESP32 đã sẵn sàng!")

        while True:
            # Kiểm tra xem có tin nhắn mới từ Web không
            client.check_msg()
            time.sleep(0.1) # Tránh treo chip
            
    except Exception as e:
        print("Lỗi kết nối:", e)
else:
    # Nếu không có wifi, dừng hẳn chương trình
    print("Dừng hệ thống do lỗi mạng.")