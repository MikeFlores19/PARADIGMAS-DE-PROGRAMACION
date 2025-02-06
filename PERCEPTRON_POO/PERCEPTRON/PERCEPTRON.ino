// Incluimos la librería de Arduino
#include <Arduino.h>

// Pines de los botones 
int inputA = 2;
int inputB = 3;

// Pines de los potenciómetros para los pesos
int potPinW1 = A0;
int potPinW2 = A1;

// Función para calcular la salida del perceptrón
int compute_output(float w1, float w2, int x1, int x2) {
    float sum = w1 * x1 + w2 * x2;
    return (sum > 0) ? HIGH : LOW; // Función de activación escalón
}

void setup() {
    // Inicializamos la comunicación serial
    Serial.begin(9600);

    // Configuramos los pines de los botones como entradas
    pinMode(inputA, INPUT);
    pinMode(inputB, INPUT);
    
    // Configuramos los pines de los potenciómetros como entradas
    pinMode(potPinW1, INPUT);
    pinMode(potPinW2, INPUT);

    // Configuramos el pin del LED como salida
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    // Leemos el estado de los botones
    int stateA = digitalRead(inputA);
    int stateB = digitalRead(inputB);

    // Leemos los valores de los potenciómetros y mapeamos los valores a los rangos adecuados
    float w1 = map(analogRead(potPinW1), 0, 1023, -920000.0, 10000.0) / 10000.0;
    float w2 = map(analogRead(potPinW2), 0, 1023, -920000.0, 10000.0) / 10000.0;

    // Imprimimos los valores de los potenciómetros en el Monitor Serie
    Serial.print("Valor de w1: ");
    Serial.print(w1, 4); // Imprimir con 2 decimales de precisión
    Serial.print("\tValor de w2: ");
    Serial.println(w2, 4); // Imprimir con 2 decimales de precisión

    // Calculamos la salida del perceptrón con los pesos actualizados
    int output = compute_output(w1, w2, stateA, stateB);

    // Encendemos o apagamos el LED según la salida del perceptrón
    digitalWrite(LED_BUILTIN, output);
    
    // Agregamos un pequeño retardo para estabilizar las lecturas
    delay(500);
}