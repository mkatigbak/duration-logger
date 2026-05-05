const int ledPin = 53;
const int buttonPin = 52;

bool ledState = false;
bool lastButtonState = HIGH;

void setup() {
  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);

  digitalWrite(ledPin, LOW);
}

void loop() {
  bool currentButtonState = digitalRead(buttonPin);

  if (lastButtonState == HIGH && currentButtonState == LOW) {

    ledState = !ledState;
    digitalWrite(ledPin, ledState);

    if (ledState == true) {
      Serial.println("ON");
    } else {
      Serial.println("OFF");
    }

    delay(50);
  }

  lastButtonState = currentButtonState;
}