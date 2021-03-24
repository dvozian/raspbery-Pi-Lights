#Raspberry Pi Final Project

## Project Objective
Controlling LED lights attached to pins on Raspberry Pi using mobile WEB interface

![Uploading image.png…]()


## Technological stack
- Raspberry Pi board with WiFi module
- Docker
- NGINX container
- PHP fpm container
- HTML, PHP, Javascript, Ajax

## Controlling interface
Web interface controlling three pins include three cases:
- All Pins On button
- All pins OFF button
- Running Lights

## Installing and operating
Required:
 - Raspberry Pi Zero W with WiFi module
 - Git
 - Docker
 - Docker compose
 - Python3
 - RPi.GPIO
 
 1. Install operating system on Raspberry Pi
 2. Connect three LED lights to pins 36, 38, and 40
 2. VNC into the board by it's IP address
   - Use ifconfig to find out the IP address
   - Use VNC to connect to the board and work with it
 3. Install Docker and Docker Compose on the raspberry pi
 4. Clone this repo
 5. cd into the directory and run:
   - docker-compose build
   - docker-compose up -d
 6. Once the containers start up, try to hit the localhost at 8080
   - http://localhost:8080/index.html
 7. Push `Lights ON` button on the page to turn all three LEDs ON
 8. Push `Lights OFF` button on the page to turn all three LEDs OFF
 9. Push `Running lights` button on the page to make the lights run in order for 60 seconds

[install-docker]: https://docs.docker.com/engine/installation
[install-docker-compose]: https://docs.docker.com/compose/install
