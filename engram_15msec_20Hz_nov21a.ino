      //Closed loop trough

unsigned long start_t, start_tt, start_tt_st, start_t_us, start_this_t, dt_micros, dt_per_trial_millis, dt_trigger_micros, dt_after_peak_mills, dt_stutter_mills;
int thr, last_v, this_v, this_delta_v, last_delta_v, ii;


void setup() {
  // put your setup code here, to run once:

  //Input pins
  pinMode(2, INPUT); //Trial onset trigger

  //Output pins
  pinMode(13, OUTPUT); //Laser trigger

  //Turn all output off
  digitalWrite(13, LOW);

  //Initialize variables
  dt_micros = 1000; //Time between samples (usec)
  dt_after_peak_mills = 0; //Time between samples (usec)
  dt_per_trial_millis = 2500; //Time per trial (msec)
  dt_trigger_micros = 15000; //Trigger on time (usec)
  dt_stutter_mills=35;//Stutter time (usec)

}

void loop() {
  // put your main code here, to run repeatedly:

 
  //Wait for trial go signal from olfactometer
  ii = 0;
  while (digitalRead(2) == LOW) {
  }

  start_t = millis();
  while ((millis() - start_t) < dt_per_trial_millis) {
    start_this_t = micros();
    ii = ii + 1;
//
//    if (ii == 1) {
//      this_v = analogRead(0);
//      while ((micros() - start_this_t) < dt_micros) {
//      }
//      ii = ii + 1;
//    }

    if (ii > 1) {
//      last_v = this_v;
//      this_v = analogRead(0);
//      this_delta_v = this_v - last_v;
//      if (ii == 2) {
//        last_delta_v=this_delta_v;
//      }
      this_delta_v=1;
      if (this_delta_v ==1)  {
        //Continuous stimulation

        //Delay
        start_t_us = millis();
        while ((millis() - start_t_us) < dt_after_peak_mills) {
        }

        //Turn on laser
        digitalWrite(13, HIGH);

        //Leave laser on
        start_tt = micros();
        while ((micros() - start_tt) < dt_trigger_micros) {
        }

        //Turn laser off
        digitalWrite(13, LOW);

        //Wait for the next pulse
        start_tt_st = millis();
        while ((millis() - start_tt_st) < dt_stutter_mills) {
        }
      }

      last_delta_v = this_delta_v;
    }
    while ((micros() - start_this_t) < dt_micros) {
    }
  }
}
