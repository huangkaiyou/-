bool brush_condition = 1;
int wait = 10;      //avoid instant unstable signal
String hit;
float threshold = 1;  //lower means board is hit
// messenge variable
String var = "0";
String var_brush = "0";
String var_game = "0";
String game_con = "0";
String player_con = "0";

int pushButton= 2; //button for start
int pushButton1= 4; //button for single
int pushButton2= 5; //button for double


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);  // max duration for reading

  pinMode(pushButton, INPUT);
}

void loop() 
{
  while (game_con=="0")
  {
    int buttonState = digitalRead(pushButton);
    // print out the state of the button:
    if (buttonState==1)
    {
      delay(5);
      if (buttonState==1)
      {
        Serial.println("start");
        delay(500);
        game_con=="1";
      }
    }
  }

  while (player_con=="0")
  {
    int buttonState1 = digitalRead(pushButton1);
    int buttonState2 = digitalRead(pushButton2);
    // print out the state of the button:
    if (buttonState1==1)
    {
      delay(5);
      if (buttonState1==1)
      {
        Serial.println("single");
        delay(500);
        player_con=="1";
    
    else if (buttonState2==1)
    {
      delay(5);
      if (buttonState2==1)
      {
        Serial.println("double");
        delay(500);
        player_con=="1";
        
  //block for reading messenge
  if (Serial.available()>0) 
  {
    var = Serial.readStringUntil('*'); //hint for type of messenge
    var.trim();

    if (var = "brush_con") {
      var_brush = Serial.readStringUntil('*');
      var_brush.trim();
    }
  }


    //block to turn on\off brush
  if (var_brush == "enable") {
    brush_condition = 1;
  }

  else if (var_brush == "disable") {
    brush_condition = 0;
  }

  //main block for brush
  if (brush_condition == 1) {

    // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
    int vol1 = analogRead(A0);
    int vol2 = analogRead(A1);
    int vol3 = analogRead(A2);
    int vol4 = analogRead(A3);
    int vol5 = analogRead(A4);
    int vol6 = analogRead(A5);

    vol1 *= (5.0 / 1023.0);
    vol2 *= (5.0 / 1023.0);
    vol3 *= (5.0 / 1023.0);
    vol4 *= (5.0 / 1023.0);
    vol5 *= (5.0 / 1023.0);
    vol6 *= (5.0 / 1023.0);

    // Serial.println(vol5);
    // delay(50);

    // a~f is No.1~6 for brush, abc is colume; def is row
    bool a = vol1 < threshold;
    bool b = vol2 < threshold;
    bool c = vol3 < threshold;
    bool d = vol4 < threshold;
    bool e = vol5 < threshold;
    bool f = vol6 < threshold;

    char *number_board[] = { "1", "2", "3", "4", "5", "6", "7", "8", "9" };

    hit = "0"; //reset to unhit

    if (a == 1) {
      if (d == 1) {
        delay(wait);
        vol4 = analogRead(A3);
        vol4 *= (5.0 / 1023.0);
        d = vol4 < threshold;
        if (d == 1) {
          hit = number_board[0];
        }
      }

      if (e == 1) 
      {
        if (hit== "0")
        {
          delay(wait);
          vol5 = analogRead(A4);
          vol5 *= (5.0 / 1023.0);
          e = vol5 < threshold;
          if (e == 1) 
          {
            hit = number_board[3];
          }
        } 
      }
      
      if (f == 1)
      {
        if (hit== "0")
        {
        delay(wait);
        vol6 = analogRead(A5);
        vol6 *= (5.0 / 1023.0);
        f = vol6 < threshold;
        if (f == 1) 
          {
            hit = number_board[6];
          }
        }
      }

    }

    if (b == 1) {
        if (d == 1) {
          if (hit== "0")
          {
            delay(wait);
            vol4 = analogRead(A3);
            vol4 *= (5.0 / 1023.0);
            d = vol4 < threshold;

            if (d == 1) {
              hit = number_board[1];
            }
          }
      }

      if (e == 1) 
      {
        if (hit== "0")
        {
          delay(wait);
          vol5 = analogRead(A4);
          vol5 *= (5.0 / 1023.0);
          f = vol5 < threshold;
          if (e == 1) {
            hit = number_board[4];
          }
        }
      } 
      
      if (f == 1)
      {
        if (hit== "0")
        {
          delay(wait);
          vol6 = analogRead(A5);
          vol6 *= (5.0 / 1023.0);
          f = vol6 < threshold;
          if (f == 1) {
            hit = number_board[7];
          }
        }
      }

    }

    if (c == 1) {
        if (d == 1) {
          if (hit== "0")
          {
            delay(wait);
            vol4 = analogRead(A3);
            vol4 *= (5.0 / 1023.0);
            d = vol4 < threshold;
            if (d == 1) {
              hit = number_board[2];
            }
          }
      }

      if (e == 1) {
        if (hit== "0")
        {
          delay(wait);
          vol5 = analogRead(A4);
          vol5 *= (5.0 / 1023.0);
          e = vol5 < threshold;
          if (e == 1) {
            hit = number_board[5];
          }
        }
      }

      if (f == 1) 
      {
        if (hit== "0")
          {
          delay(wait);
          vol6 = analogRead(A5);
          vol6 *= (5.0 / 1023.0);
          f = vol6 < threshold;
          if (f == 1) 
            {
              hit = number_board[8];
            }
          }
      }
    }
    if (hit != "0") {
      Serial.println(hit);
      delay(1000);
    }

  } 
}