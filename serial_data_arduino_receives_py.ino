void setup () {
  Serial.begin (115200);
  
}

void loop () {
  if (Serial.available () > 0 ) {
    char data = Serial.read ();
    Serial.print("from Python, i have received: ");
    Serial.println ((data));

  }
}

