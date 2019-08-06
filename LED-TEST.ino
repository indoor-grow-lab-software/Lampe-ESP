#include <Wire.h> //i2C
#include <Adafruit_PWMServoDriver.h>  //PWM
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();  //KLasse pwm in PWM lib.

void setup() {
  pwm.begin();
  pwm.setPWMFreq(100); //max 1600Hz
  Serial.begin(115200);
  for (int i=0;i<16;i++){pwm.setPin(i,0);}  // reset all pins to zero
}


void loop() {
  // put your main code here, to run repeatedly:
durchlauf();

}


int i=0;
void durchlauf(){     // steuert jede LED nacheinander an 
  pwm.setPin(i,1100); // 0-4096 HELLIGKEIT
  Serial.println(i);
  delay(1000);
  pwm.setPin(i,0); // 0-4096
  if(i>16){i=0;}
  i++;
}
