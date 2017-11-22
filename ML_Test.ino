/*
 * Example to demonstrate thread definition, semaphores, and thread sleep.
 */
#include <FreeRTOS_ARM.h>
#include "PowerDueLED.h"
#include "Ml.h"

void setup() {
  float cie = 0.00005;
  pd_rgb_led_init();
  pd_rgb_led(PD_OFF);
  SerialUSB.begin(9600);
  while(!SerialUSB){
  }
  delay(1000);
  Ml ml;
  ml.clear_all();
  //ml.append(200);
  //ml.append(100);
  //ml.append(300);
  ml.sample(75);
  SerialUSB.println("Begin");
  pd_rgb_led(PD_RED);
  delay(1000);
  ml.regression(cie,0);
  ml.regression(cie,0.1);
  ml.regression(cie,0.2);
  //ml.regression(cie,0.3);
  ml.regression(cie,0.4);
  //ml.regression(cie,0.5);
  ml.regression(cie,0.6);
  //ml.regression(cie,0.7);
  //ml.regression(cie,0.8);
  ml.regression(cie,0.9);
  pd_rgb_led(PD_OFF);
  SerialUSB.println("Done");

}
//------------------------------------------------------------------------------
// WARNING idle loop has a very small stack (configMINIMAL_STACK_SIZE)
// loop must never block
void loop() {
  // Not used.
}
