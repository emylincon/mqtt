# Working with MQTT in Linux and Python3

### To install Mosquitto server and client on your Linux Host
* apt install mosquitto mosquitto-clients -y

#### Testing if it works
* mosquitto_sub -h localhost -t test
* mosquitto_pub -h localhost -t test -m "Hello World"
* mosquitto_sub -h localhost -t test

`Default Port : 1883`

+++++++++++++++++++++++++++++++++++

### Enabling Password on your Mosquito server
* sudo mosquitto_passwd -c /etc/mosquitto/passwd admin
* sudo nano /etc/mosquitto/conf.d/default.conf
* copy these lines to the file
* `allow_anonymous false`
* `password_file /etc/mosquitto/passwd`
3. sudo systemctl restart mosquitto

#### Testing if  password works
1. mosquitto_sub -h localhost -t test -u "admin" -P "password"
2. mosquitto_pub -h localhost -t "test" -m "Hello World" -u "admin" -P "password"

### installing mqtt in python3
* pip3 install paho-mqtt
* apt install python3-paho-mqtt -y
