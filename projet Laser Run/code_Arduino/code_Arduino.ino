// Broches des LEDs dans un tableau
const int ledPins[5] = {12, 8, 7, 4, 2};

// Entrée de la LDR
const int ldrPin = A0;

// Seuil à ajuster selon ton montage et ton ambiant
const int seuil = 50;

// Variables de détection de front
int ldrValeur = 0;
bool etatPrecedent = false;   // false = en-dessous du seuil
int compteur = 0;             // Nombre de LEDs allumées

void setup() {
  // Initialise les broches LED en sortie
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);
  }
  // (Optionnel) Moniteur série pour debug
  Serial.begin(9600);
}

void loop() {
  // Lecture LDR
  ldrValeur = analogRead(ldrPin);
  bool auDessus = (ldrValeur >= seuil);

  // Détecter front montant : passage de bas en haut
  if (auDessus && !etatPrecedent) {
    // On a un flash : on incrémente le compteur (max 5)
    compteur++;
    if (compteur > 5) compteur = 5;
    Serial.print("Flash détecté ! compteur = ");
    Serial.println(compteur);
  }
  etatPrecedent = auDessus;

  // Allumer les LEDs selon le compteur
  for (int i = 0; i < 5; i++) {
    if (i < compteur) digitalWrite(ledPins[i], HIGH);
    else             digitalWrite(ledPins[i], LOW);
  }

  delay(50); // Anti-rebond / petite temporisation
}
