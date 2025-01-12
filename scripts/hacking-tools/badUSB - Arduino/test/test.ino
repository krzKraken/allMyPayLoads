#include "Keyboard.h"

void setup() {
  Keyboard.begin();  // Inicializa la emulación del teclado
  delay(1000);       // Espera un segundo para asegurar la detección del dispositivo

  // Abrir CMD con Win + R y escribir cmd
  Keyboard.press(KEY_LEFT_GUI);  // Tecla Windows
  Keyboard.press('r');           // Tecla R
  delay(500);
  Keyboard.releaseAll();         // Suelta las teclas

  delay(500);
  Keyboard.println("cmd");       // Escribe "cmd" y presiona Enter
  delay(500);
  Keyboard.press(KEY_RETURN);    // Presiona Enter
  Keyboard.releaseAll();

  delay(1000);
  
  delay(500);
  Keyboard.println("notepad.exe");
  delay(500);
  Keyboard.press(KEY_RETURN);
  Keyboard.releaseAll();

  Keyboard.println("hola mi amor estoy haciendo esto desde la usb");

  Keyboard.end();  // Desactiva la emulación del teclado
}

void loop() {
  // No se usa en este caso
}
