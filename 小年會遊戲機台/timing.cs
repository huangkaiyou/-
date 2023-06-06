void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  double timing= 15; //the interval of time
  double time = micros()/1000000;
  double time1 = time;
  bool hit= true;
  while ((time1-time)<timing && hit== true)
  {
  Serial.print("Time: ");
  //prints time since program started
  Serial.println(time1);
  // wait a second so as not to send massive amounts of data
  time1 = micros()/1000000;
  if ((time1-time)>=5.00)
  {
    hit=false ;
  }
  delay(1000);
  }
  Serial.println("love you");
  
}
