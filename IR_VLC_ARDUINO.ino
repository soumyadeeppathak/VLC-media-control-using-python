#include <IRremote.h>

int RECV_PIN = 11;//The definition of the infrared receiver pin 11
IRrecv irrecv(RECV_PIN);
decode_results results;

void setup()
{
  Serial.begin(9600); //Open serial 
  irrecv.enableIRIn(); // Initialization infrared receiver
} 

void loop() 
{
  if (irrecv.decode(&results)) {

    if(results.value == 0xFFA857){ //these hex codes will differ for different remotes
      Serial.println("volumn up");
    }
    if(results.value == 0xFFE01F){
      Serial.println("volumn down");
    }
    if(results.value == 0xFFC23D){
      Serial.println("play/pause");
    }
    if(results.value == 0xFF02FD){
      Serial.println("skip 10+ s");
    }
    
    if(results.value == 0xFF22DD){
      Serial.println("BACKskip 10- s");
    }
    
    if(results.value == 0xFF906F){
      Serial.println("toggle fullscreen");
    }
    if(results.value == 0xFF6897){
      Serial.println("EXIT");
    }
    irrecv.resume(); 
  }
  delay(100);
}
