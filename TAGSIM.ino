#include <Wire.h> //i2C
#include <Adafruit_PWMServoDriver.h>  //PWM
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();  //KLasse pwm in PWM lib.

void setup() {
  pwm.begin();
  pwm.setPWMFreq(100); //max 1600Hz
  Serial.begin(115200);
  for (int i=0;i<16;i++){pwm.setPin(i,0);}  // reset all pins to zero
}



// pin array def
int rotpin[]  = {0,3,7,12,15};
int blaupin[] = {1,2,4,8,14};
int weißpin[] = {4,10,13};
int uvpin[]   = {9};
int irpin[]   = {5};
int gruenpin[]= {11};

//hell def
int rothell  = 0;
int blauhell = 0;
int weißhell = 0;
int uvhell = 0;
int irhell = 0;
int gruenhell = 0;

//soll hell def

int sollrothell = 0;
int sollblauhell = 0;
int sollweißhell = 0;
int solluvhell = 0;
int sollirhell = 0;

//def Variablen
int fade = 2;       //je kleiner desdo schneller, minimal 1!
long LV=0;  //Laufvariable 

void loop() {
setHelligkeit();  //Helligkeitsupdate ->immer benötigt
simulation();     //eigentliche Verlaufssimulation


LV++;             //LV counter
Serial.println(LV);
delay(1);
}

void simulation(){  // Verlaufssimulation = 1 m = 60000 ms
  
  if(LV==0){        // Zum ZeitPunkt LV=0 -> 0ms
    sollrothell = 1024;
//    Serial.println("sollrothell1");
//    Serial.println(sollrothell);
//    Serial.println(rothell);
  }
  if(LV==3000){     // Zum ZeitPunkt LV=0 -> ~5000ms
  sollrothell = 0;
//  Serial.println("sollrothell0");
//  Serial.println(sollrothell);
//  Serial.println(rothell);
  }
  if(LV==6000){LV=-1;};// Zum ZeitPunkt ~10000ms repeat!
}




void setHelligkeit(){  //setzt Helligkeit der Pins!
  if(rothell<sollrothell && LV%fade == 0){ // fade if zu dunkel
    rothell++;
    Serial.println("++"); 
    }
  if(rothell>sollrothell && LV%fade == 0){ // fade if zu hell
    rothell--;
    Serial.print("--   ");  
    Serial.println(rothell);
    }
  setColor(rotpin,rothell);   //setzt Helligkeit der rotPins
}

void setColor(int *arr, int value){   //setzt alle Elemente aus array auf value!
int i = 0;
  while(i<=sizeof(arr)){
    pwm.setPin(arr[i],value);
    i++;
  }
}
