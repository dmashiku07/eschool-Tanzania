#include <SoftwareSerial.h>
SoftwareSerial mySerial(3, 2); // bluetooth Module/sim800L module Tx & Rx conneced to Arduino #3 & #2
// this code is used to get information from the python logic processor and send the reply information to the user


String pyLogic; //raw data reading from pyLogic
String replyChar; //first character of the pyLogic String used to convert to int
String replyNumber; //number to send SMS text back to the sender
String replyMessage;//result from pylogic to be sent back to the user
int replyInt; //to be used in switch case statement to trigger module reply
void setup() {
 Serial.begin(57600);
 mySerial.begin(57600);

}

void loop() {
  if(Serial.available() > 0){ // statement to check if there is information coming in from the python logic processor
  pyLogic = Serial.readString();
  replyChar = pyLogic.substring(0,1); //first charater of the pyLogic string
  //mySerial.println(replyChar);
  replyNumber = pyLogic.substring(2,15); // reply number from the pyLogic string
  replyMessage = pyLogic.substring(16); // reply message from the pyLogic string
  mySerial.println(replyMessage);
  delay(500);
  if(replyChar == "j"){
    SendMessage(); // function to send reply information to the user
    }
  }
  
}

void SendMessage()
{
  mySerial.println("AT+CMGF=1");    //Sets the GSM Module in Text Mode
  delay(100);  // Delay of 1000 milli seconds or 1 second
  mySerial.println("AT+CMGS=\"" + replyNumber + "\"\r");
  delay(100);
  mySerial.println(replyMessage);// The SMS text you want to send
  delay(100);
   mySerial.println((char)26);// ASCII code of CTRL+Z
  delay(100);
}
