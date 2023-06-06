void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  int brush[]= {2,4,7,8,12,13};
  for (int i=0; i<6; i++)
  {
      pinMode(brush[i],INPUT);
  }
}

void loop() {
//   put your main code here, to run repeatedly:
  int wait= 500; //avoid instant unstable signal
  int threshold= 1; //lower represent has hit
  int brush[]= {2,4,7,8,12,13};
  int vol1=digitalRead(brush[0]);
  int vol2=digitalRead(brush[1]);
  int vol3=digitalRead(brush[2]);
  int vol4=digitalRead(brush[3]);
  int vol5=digitalRead(brush[4]);
  int vol6=digitalRead(brush[5]);

  int voltage[]= {vol1, vol2, vol3, vol4, vol5, vol6};
  // a~f is No.1~6 for brush, abc is colume; def is row
  bool a= voltage[0]<threshold;
  bool b= voltage[1]<threshold;
  bool c= voltage[2]<threshold;
  bool d= voltage[3]<threshold;
  bool e= voltage[4]<threshold;
  bool f= voltage[5]<threshold;

//block for exam code
  // Serial.print(a==true);
  // Serial.print(b);
  // Serial.print(c);
  // Serial.print(d==true);
  // Serial.print(e);
  // Serial.println(f);

  char *number_board[]= {"num1","num2","num3","num4","num5","num6","num7","num8","num9"};
  String hit;
  hit = "not hit";

  if (a == true)
  {
      if (d== true)
      {
          delay(wait);
          if (d== true)
          {
            hit= number_board[0];
          }
          
      }

      else if (e== true)
      {
          delay(wait);
          if (e==true)
          {
          hit= number_board[3];
          }
      }
      else if (f== true)

      {
          delay(wait);
          if (f==true)
          {
          hit= number_board[6];
          }
      }

      else
      {
          hit= "broken";
      }
  }

  else if (b == true)
  {
      if (d== true)
      {
          delay(wait);
          if (d==true)
          {
          hit= number_board[1];
          }
      }

      else if (e== true)
      {
          delay(wait);
          if (e==true)
          {
          hit= number_board[4];
          }
      }
      else if (f== true)

      {
          delay(wait);
          if (f==true)
          {
          hit= number_board[7];
          }
      }

      else
      {
          hit= "broken";
      }
  }

  else if (c == true)
  {
      if (d== true)
      {
          delay(wait);
          if (d==true)
          {
          hit= number_board[2];
          }
      }

      else if (e== true)
      {
          delay(wait);
          if (e==true)
          {
          hit= number_board[5];
          }
      }
      else if (f== true)

      {
          delay(wait);
          if (f==true)
          {
          hit= number_board[8];
          }
      }

      else
      {
          hit= "broken";
      }
  }
  
  
      
  Serial.println(hit);
  delay(1000);
}
