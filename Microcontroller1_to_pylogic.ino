#include <SoftwareSerial.h>
SoftwareSerial mySerial(3, 2); //SIM800L Tx & Rx is connected to Arduino #3 & #2 

//code that gets text message information from the sim800L module and sends the information vai serial to the python logic processor

String data; // varaible to hold raw data from sim module
String userNumber; // varaible to hold userNumber substring
String messageBody; // varaible to hold message body substring

void setup()
{
  Serial.begin(57600);//Begin serial communication with Arduino and Arduino IDE (Serial Monitor)
  mySerial.begin(57600); //Begin serial communication with Arduino and SIM800L
  smsMode(); // function to place the sim module to recieve SMS messages 
 
 }

void loop() //
{
 
  if(mySerial.available() > 0){
    data = mySerial.readString();//read the message from the sim800L module
    //Serial.println(data.substring(7,49));//data from sim800L sent to python logic vai UART
    userNumber = data.substring(9,22); // substring for the user number from sim module
    messageBody = data.substring(50); // substring containing the message body from sim module
    Serial.print(userNumber); // send userNumber information vai serial(UART) to python logic
    delay(1500);
    Serial.print(messageBody); // send MessageBody information vai serial(UART) to python logic
    delay(200);
 
      }
    
    }
  
void smsMode(){ // function to set sim800L module into SMS mode
  mySerial.println("AT+CMGF=1"); //set SMS to test mode
  delay(200);
  mySerial.println("AT+CNMI=1,2,0,0,0"); // procedure to handle newly arrived messages
  delay(200);
  mySerial.println("AT+CMGD=1,4"); // deletes all the messages 
  delay(200);
  
 }
 
