const int ledPin = 53;
const int buttonPin = 52;

bool ledState = false;
bool lastButtonState = HIGH;

unsigned long ledOnStartTime = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);

  digitalWrite(ledPin, LOW);

  Serial.println("Duration(s)");
}

void loop() {
  bool currentButtonState = digitalRead(buttonPin);

  if (lastButtonState == HIGH && currentButtonState == LOW) {

    ledState = !ledState;
    digitalWrite(ledPin, ledState);

    if (ledState == true) {
      ledOnStartTime = millis();
    } 
    else {
      unsigned long durationMs = millis() - ledOnStartTime;
      float durationSec = durationMs / 1000.0;

      Serial.println(durationSec, 3);
    }

    delay(50);
  }

  lastButtonState = currentButtonState;
}