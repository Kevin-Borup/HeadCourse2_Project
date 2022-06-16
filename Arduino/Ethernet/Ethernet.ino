#include <Servo.h>
#include <SPI.h>
#include <Ethernet.h>

const int pirPin = 2;
const int servoPin = 3;
int pirStat = 0;
int pirCurrent = 0;
byte mac[] = {  
  0x00, 0xAA, 0xBB, 0xCC, 0xDE, 0x02 };
IPAddress otherIp(10, 108, 149, 11);
Servo servo;
  
unsigned int localPort = 5000; // Assign a port to talk over
char packetBuffer[UDP_TX_PACKET_MAX_SIZE]; //dimensian a char array to hold our data packet
String datReq; //String for our data
int packetSize; //Size of the packet
EthernetUDP Udp;

void setup() {
  pinMode(pirPin, INPUT);
  servo.attach(3);
  Serial.begin(9600);
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
  }
  else{
  Serial.print("My IP address: ");
  for (byte thisByte = 0; thisByte < 4; thisByte++) {
    Serial.print(Ethernet.localIP()[thisByte], DEC);
    Serial.print(".");
  }
  Serial.println();
  }
  Udp.begin(localPort); //Initialize Udp
  delay(1500); //delay
}

bool carDetected = false;

void loop() {

  while(!carDetected){
     int currentValue = ReadPir();
     if (currentValue == 1){
      carDetected = true;
     }
   }

   while(carDetected){
    packetSize = Udp.parsePacket(); //Reads the packet size
    if(packetSize>0) { //if packetSize is >0, that means someone has sent a request
      bool response = ReadData();
      if (response){
      carDetected = false;
      }
    //Udp.beginPacket(Udp.remoteIP(), Udp.remotePort()); //Initialize packet send
    //Udp.print(pirStat); //Send the Pressure data
    //Udp.endPacket(); //End the packet
    }
   }
}

int ReadPir(){
  pirStat = digitalRead(pirPin);
  if(pirStat==1 && pirStat != pirCurrent){
    SendData();
  }
  pirCurrent == pirStat;
  return pirStat;
}

void SendData(){
  Udp.beginPacket(otherIp, 712); //Initialize packet send
  Udp.print(pirStat); //Send the Pressure data
  Udp.endPacket(); //End the packet
  memset(packetBuffer, 0, UDP_TX_PACKET_MAX_SIZE); //clear out the packetBuffer array
}

bool ReadData(){
  Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
  String datReq(packetBuffer);
  Serial.print(datReq);
  if(datReq.indexOf("Open" > 0)){
    OpenGate();
    return true;
  } else if (datReq.indexOf("Close" > 0)){
    return true;
  }
  return false;
}

void OpenGate(){
  servo.write(70);
  delay(2000);
  CloseGate();
}

void CloseGate(){
  servo.write(0);
}
