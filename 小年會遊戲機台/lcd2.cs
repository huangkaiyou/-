/*

  HelloWorld.pde
  
  "Hello World!" example code.
  
  >>> Before compiling: Please remove comment from the constructor of the 
  >>> connected graphics display (see below).
  
  Universal 8bit Graphics Library, https://github.com/olikraus/u8glib/
  
  Copyright (c) 2012, olikraus@gmail.com
  All rights reserved.

  Redistribution and use in source and binary forms, with or without modification, 
  are permitted provided that the following conditions are met:

  * Redistributions of source code must retain the above copyright notice, this list 
    of conditions and the following disclaimer.
    
  * Redistributions in binary form must reproduce the above copyright notice, this 
    list of conditions and the following disclaimer in the documentation and/or other 
    materials provided with the distribution.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND 
  CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
  INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF 
  MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT 
  NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
  STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
  ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.  
  
*/


#include "U8glib.h"
U8GLIB_ST7920_128X64 u8g(13, 11,10, U8G_PIN_NONE);

String var = "0";
String score = "0";
int i= 0;
// char *list[]= {"ouo", "yoyo", "chichi", "haha"};

void draw() {
  // graphic commands to redraw the complete screen should be placed here  
  u8g.setFont(u8g_font_unifont);
  //u8g.setFont(u8g_font_osb21);
  u8g.drawStr( 0, 15, "Mode:   Single");
  // u8g.drawStr( 0, 30, list[i]);
  // u8g.drawStr( 0, 45, list[i]);
  // u8g.drawStr( 0, 60, list[i]);
  if (Serial.available()>0) 
  {
    // String ignor = Serial.readStringUntil('\n');
    var= Serial.readStringUntil('*');
    var.trim();
  }
  u8g.drawStr( 0, 30, "1");
  u8g.drawStr( 15, 30, "2");
  u8g.drawStr( 30, 30, "3");
  u8g.drawStr( 0, 45, "4");
  u8g.drawStr( 15, 45, "5");
  u8g.drawStr( 30, 45, "6");
  u8g.drawStr( 0, 62, "7");
  u8g.drawStr( 15, 62, "8");
  u8g.drawStr( 30, 62, "9");
  // u8g.drawStr( 30, 62, "X");

  u8g.drawStr( 50, 30, "score:");
  u8g.drawStr( 50, 45, "aim  :");
  u8g.drawStr( 50, 60, "hit  :");

  // while (Serial.available()==0){} 
    // String ignor = Serial.readStringUntil('\n');
  var= Serial.readStringUntil('*');
  var.trim();

  if (var== "score")
  {
    score = Serial.readStringUntil('*');
  }
  // var= "10";
  u8g.setPrintPos(97, 30); 
  u8g.print(score);
  Serial.println(score);
  // u8g.drawStr( 97, 30, var);

  u8g.drawStr( 97, 45, "1");
  u8g.drawStr( 97, 60, "5");
  // Serial.println(list[i]);
  
  // delay(10);
}

// void clearLED(){
// u8g.firstPage();
// do {
// } while( u8g.nextPage() );
// }



void setup(void) {
  Serial.begin(9600);
  Serial.setTimeout(200); // set new value to 100 milliseconds
  
  // flip screen, if required
  // u8g.setRot180();
  
  // set SPI backup if required
  //u8g.setHardwareBackup(u8g_backup_avr_spi);

  // assign default color value
  if ( u8g.getMode() == U8G_MODE_R3G3B2 ) {
    u8g.setColorIndex(255);     // white
  }
  else if ( u8g.getMode() == U8G_MODE_GRAY2BIT ) {
    u8g.setColorIndex(3);         // max intensity
  }
  else if ( u8g.getMode() == U8G_MODE_BW ) {
    u8g.setColorIndex(1);         // pixel on
  }
  else if ( u8g.getMode() == U8G_MODE_HICOLOR ) {
    u8g.setHiColorByRGB(255,255,255);
  }
  
  pinMode(8, OUTPUT);
  Serial.println("begin");
}

void loop(void) {
  // picture loop
  u8g.firstPage();
  do {
    draw();

    // Serial.println("next");
  } while( u8g.nextPage() );

  // i+=1;
  // if (i==4)
  // {
  //   i=0;
  //   clearLED();
  //   delay(1000);
  // }
  
  
  // rebuild the picture after some delay
  // delay(2000);
}

