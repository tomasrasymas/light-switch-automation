import network
import machine

class Wifi:
    WIFI_SSID = 'XXXXXXX'
    WIFI_PASSWORD = 'YYYYYYYY'
    
    @staticmethod
    def connect(wifi_ssid=None, wifi_password=None):
        wifi_ssid = wifi_ssid or Wifi.WIFI_SSID
        wifi_password = wifi_password or Wifi.WIFI_PASSWORD
        
        print('Connecting...')
        wifi = network.WLAN(network.STA_IF)
        
        if wifi.isconnected():
            print('Already connected...')
            return
            
        print('Activating network interface...')
        wifi.active(True)
        
        print('Scanning avalable wifi networks...')
        wifis = wifi.scan()
            
        my_wifi_exists = [i for i in wifis if str(i[0].decode('UTF-8')) == wifi_ssid]
        
        print(f'My wifi network is available: {my_wifi_exists}')
        
        if my_wifi_exists:
            print('Connecting...')
            wifi.connect(wifi_ssid, wifi_password)
            
            print('Waiting while connects...')
            while not wifi.isconnected():
                machine.idle()
            
            print('Connected!')
        
        @staticmethod
        def is_connected():
            wifi = network.WLAN(network.STA_IF)
            return wifi.isconnected()
