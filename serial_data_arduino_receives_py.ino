const int ledPin = 7;

char data;


void setup () 
{
  Serial.begin (115200);
  pinMode (ledPin, OUTPUT);

}  

  
int getData () {
  
  if (Serial.available ()) 
  {
     data = Serial.read ();
  }  

  return data;
}

void switch_on (char input){
  
  if (input == '1') {
    digitalWrite (ledPin, HIGH);
  }
}


void switch_off (char input) {

  if (input == '0') {
    
    digitalWrite (ledPin, LOW);
  }
}

void loop () 
{ 
  getData();

  switch_on (getData ());

  switch_off (getData ());

}
