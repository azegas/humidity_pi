# humidity_pi

```sh
arvypi@raspberrypi:~ $ cat /proc/cpuinfo | grep Model
Model           : Raspberry Pi 3 Model B Rev 1.2
```

Pin info - https://i.pinimg.com/736x/bf/e5/02/bfe502b80a3248ed48fb125182235c32.jpg

-----------------

## Humidity sensor

```sh
source venv
pip3 install adafruit-circuitpython-dht
```

I have humidity sensor and I want to read the humidity from it and print it to the console.

I want to do this every second. my sensor is DHT22 - https://www.anodas.lt/dht22-temperaturos-ir-dregmes-jutiklis-su-pcb

```
Temperature: 25.5°C, Humidity: 67.2%
Temperature: 25.5°C, Humidity: 67.1%
Temperature: 25.5°C, Humidity: 67.1%
Temperature: 25.5°C, Humidity: 67.2%
Temperature: 25.5°C, Humidity: 67.2%
Temperature: 25.5°C, Humidity: 66.9%
Temperature: 25.5°C, Humidity: 66.9%
Temperature: 25.5°C, Humidity: 67.6%
Temperature: 25.5°C, Humidity: 67.6%
```

## motion sensor

I have such motion sensor - https://www.anodas.lt/hc-sr501-pir-judesio-daviklis?search=PIR

its pins - https://images.theengineeringprojects.com/image/main/2019/01/Introduction-to-HC-SR501.jpg

- TODO try to control delay
- TODO try to control sensitivity