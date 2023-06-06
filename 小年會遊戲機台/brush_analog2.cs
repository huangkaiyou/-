bool brush_condition = 0;
int wait = 10;      //avoid instant unstable signal
String hit;
float threshold = 1.0;  //lower means board is hit
// messenge variable
String var = "0";
String var_brush = "0";
String var_game = "0";
String var_time = "0";
String var_ball = "0";
String var_score = "0";
String var_aim = "0";

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

    if (var = "brush_con") {
      var_brush = Serial.readStringUntil('*');
      var_brush.trim();
    }

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
      if (hit== "0")
      {
        if (d == 1) {
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
      if (hit== "0")
      {
        if (d == 1) {
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
  } //end for brush function

}
