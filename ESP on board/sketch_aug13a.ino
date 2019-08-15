#include <Wire.h> //i2C
#include <Adafruit_PWMServoDriver.h>  //PWM
#include "ESP_MICRO.h"

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();  //KLasse pwm in PWM lib.


void setup() {
  pwm.begin();
  pwm.setPWMFreq(100); //max 1600Hz
  Serial.begin(115200);

  start("EPS2", ""); // Wifi details connec to
}

void loop() {
  waitUntilNewReq();  //Waits until a new request from python come
  magnitude, value = strtok(getPath(),"_")
  if (magnitude == "/FRQ") {
    pwm.setPWMFreq(int(value))  // reset all pins to 2000
  }
  elif (magnitude == "/HEL") {
    for (int i = 0; i < 16; i++) {
      pwm.setPin(i, int(value)); // reset all pins to 2000
    }
  }
  if (magnitude == "/SET") {
    for (int i = 0; i < 16; i++) {
      pwm.setPin(i, int(value)); // reset all pins to zero
    }
  }
}
