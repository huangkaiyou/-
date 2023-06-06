bool brush_condition = 0;
int wait = 10;      //avoid instant unstable signal
int threshold = 1;  //lower represent has hit
String var = "0";
String var_brush = "0";

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
    //   put your main code here, to run repeatedly:
    var = Serial.readStringUntil('*');
    var.trim();
    if (var = "brush_con") {
      var_brush = Serial.readStringUntil('*');
      var_brush.trim();
    }
  }

    if (var_brush == "enable") {
      brush_condition = 1;
    }

    else if (var_brush == "disable") {
      brush_condition = 0;
    }

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

      int voltage[] = { vol1, vol2, vol3, vol4, vol5, vol6 };
      // a~f is No.1~6 for brush, abc is colume; def is row
      bool a = voltage[0] < threshold;
      bool b = voltage[1] < threshold;
      bool c = voltage[2] < threshold;
      bool d = voltage[3] < threshold;
      bool e = voltage[4] < threshold;
      bool f = voltage[5] < threshold;

      //block for exam code
      // Serial.print(a);
      // Serial.print(b);
      // Serial.print(c);
      // Serial.print(d);
      // Serial.print(e);
      // Serial.println(f);
      // delay(50);

      char *number_board[] = { "1", "2", "3", "4", "5", "6", "7", "8", "9" };
      String hit;
      hit = "0";
      // Serial.println(voltage[3]);
      // delay(10);
      if (a == 1) {
        if (d == 1) {
          delay(wait);
          vol4 = analogRead(A3);
          // Serial.println(vol4);
          vol4 *= (5.0 / 1023.0);
          d = vol4 < threshold;
          if (d == 1) {
            hit = number_board[0];
          }
        }

        else if (e == 1) {
          delay(wait);
          vol5 = analogRead(A4);
          vol5 *= (5.0 / 1023.0);
          e = vol5 < threshold;
          if (e == 1) {
            hit = number_board[3];
          }
        } else if (f == 1)

        {
          delay(wait);
          vol6 = analogRead(A5);
          vol6 *= (5.0 / 1023.0);
          f = vol6 < threshold;
          if (f == 1) {
            hit = number_board[6];
          }
        }

      }

      else if (b == 1) {
        if (d == 1) {
          delay(wait);
          vol4 = analogRead(A3);
          vol4 *= (5.0 / 1023.0);
          d = vol4 < threshold;

          if (d == 1) {
            hit = number_board[1];
          }
        }

        else if (e == 1) {
          delay(wait);
          vol5 = analogRead(A4);
          vol5 *= (5.0 / 1023.0);
          f = vol5 < threshold;
          if (e == 1) {
            hit = number_board[4];
          }
        } else if (f == 1)

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

      else if (c == 1) {
        if (d == 1) {
          delay(wait);
          vol4 = analogRead(A3);
          vol4 *= (5.0 / 1023.0);
          d = vol4 < threshold;
          if (d == 1) {
            hit = number_board[2];
          }
        }

        if (e == 1) {
          delay(wait);
          vol5 = analogRead(A4);
          vol5 *= (5.0 / 1023.0);
          e = vol5 < threshold;
          if (e == 1) {
            hit = number_board[5];
          }
        }
        if (f == 1) {
          delay(wait);
          vol6 = analogRead(A5);
          vol6 *= (5.0 / 1023.0);
          f = vol6 < threshold;
          if (f == 1) {
            hit = number_board[8];
          }
        }
      }
      if (hit != "0") {
        Serial.println(hit);
        delay(1000);
      }
    
    }

}
