#include "U8glib.h"
U8GLIB_ST7920_128X64 u8g(13, 11,10, U8G_PIN_NONE);

// messenge variable
String var = "0";
String var_brush = "0";
String var_game = "0";
String var_time = "0";
String var_ball = "0";
String var_score = "0";
String var_aim = "0";
String var_hit = "0";

//for lcd
bool con1= 1;
bool con2= 1;
bool con3= 1;
bool con4= 1;
bool con5= 1;
bool con6= 1;
bool con7= 1;
bool con8= 1;
bool con9= 1;


void draw() {
  // graphic commands to redraw the complete screen should be placed here  
  u8g.setFont(u8g_font_unifont);
  //u8g.setFont(u8g_font_osb21);
  u8g.drawStr( 0, 15, "Single");
  
  var= Serial.readStringUntil('*');
  var.trim();
  if (var=="hit_con")
  {
    var_hit= Serial.readStringUntil('*');
    var.trim();

      if (var_hit== "1")
    {
      con1=0;
    }
    else if (var_hit== "2")
    {
      con2=0;
    }
    else if (var_hit== "3")
    {
      con3=0;
    }
    else if (var_hit== "4")
    {
      con4=0;
    }
    else if (var_hit== "5")
    {
      con5=0;
    }
    else if (var_hit== "6")
    {
      con6=0;
    }
    else if (var_hit== "7")
    {
      con7=0;
    }
    else if (var_hit== "8")
    {
      con8=0;
    }
    else if (var_hit== "9")
    {
      con9=0;
    }
  }


  if (con1==1)
  {
    u8g.drawStr( 0, 30, "1");
  }
  if (con2==1)
  { 
  u8g.drawStr( 15, 30, "2");
  }
  if (con3==1)
  { 
  u8g.drawStr( 30, 30, "3");}
  if (con4==1)
  { 
  u8g.drawStr( 0, 45, "4");}
  if (con5==1)
  { 
  u8g.drawStr( 15, 45, "5");}
  if (con6==1)
  { 
  u8g.drawStr( 30, 45, "6");}
  if (con7==1)
  { 
  u8g.drawStr( 0, 62, "7");}
  if (con8==1)
  { 
  u8g.drawStr( 15, 62, "8");}
  if (con9==1)
  { 
  u8g.drawStr( 30, 62, "9");}
  // u8g.drawStr( 30, 62, "X");

  u8g.drawStr( 60, 15, "time:");
  u8g.drawStr( 50, 30, "score:");
  u8g.drawStr( 50, 45, "aim  :");
  u8g.drawStr( 50, 60, "ball :");

  if (var== "ball_con")
  {
    var_ball = Serial.readStringUntil('*');
  }
  u8g.setPrintPos(97, 60); 
  u8g.print(var_ball);

  if (var== "score_con")
  {
    var_score = Serial.readStringUntil('*');
  }
  u8g.setPrintPos(97, 30); 
  u8g.print(var_score);

  if (var== "aim_con")
  {
    var_aim = Serial.readStringUntil('*');
  }
  u8g.setPrintPos(97, 45);
  u8g.print(var_aim);

  if (var== "time_con")
  {
    var_time = Serial.readStringUntil('*');
  }
  u8g.setPrintPos(102, 15); 
  u8g.print(var_time);
  // delay(400);
  
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);  // max duration for reading
}

void loop() 
{
  //block for reading messenge
  if (Serial.available()>0) 
  {
    var = Serial.readStringUntil('*'); //hint for type of messenge
    var.trim();


    else if (var = "game_con") {
      var_game = Serial.readStringUntil('*');
      var_brush.trim();
    }

    else if (var = "time_con") {
      var_time = Serial.readStringUntil('*');
      var_brush.trim();
    }

    else if (var = "score_con") {
      var_score = Serial.readStringUntil('*');
      var_brush.trim();
    }

    else if (var = "ball_con") {
      var_ball = Serial.readStringUntil('*');
      var_brush.trim();
    }

    else if (var = "aim_con") {
      var_aim = Serial.readStringUntil('*');
      var_brush.trim();
    }
  
  }
  //main block for brush
  

  u8g.firstPage();
  do {
    draw();
// Serial.println("next");
  } while( u8g.nextPage() );
  // delay(10);
// } //end for brush function


  //   clearLED(); 
} 
