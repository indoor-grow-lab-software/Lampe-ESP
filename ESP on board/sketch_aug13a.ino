#include <Wire.h> //i2C
#include <Adafruit_PWMServoDriver.h>  //PWM
#include "ESP_MICRO.h"

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();  //KLasse pwm in PWM lib.


void setup(){
  pwm.begin();
  pwm.setPWMFreq(100); //max 1600Hz
  Serial.begin(115200);
  
  start("EPS2",""); // Wifi details connec to
}

void loop(){
  waitUntilNewReq();  //Waits until a new request from python come

  if (getPath()=="/OPEN_LED"){
      for (int i=0;i<16;i++){pwm.setPin(i,2000);}  // reset all pins to zero
  }
  if (getPath()=="/CLOSE_LED"){
      for (int i=0;i<16;i++){pwm.setPin(i,0);}  // reset all pins to zero
  }
}
