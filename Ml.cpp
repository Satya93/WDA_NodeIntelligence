#include "Ml.h"
#include <Arduino.h>

int *buff = 0;

void Ml::clear_all()
{
  _cnt = 0;
  _sum = 0;
  _min = 0.0;
  _max = 0.0;
  _stddev = 0.0;
  _pin = 4;
  _old = 0;
  randomSeed(48);
}

void Ml::append(float f)
{
  int dev;
  if(_cnt==0)
  {
    _min = f;
    _max = f;
  }
  else{
    if (f < _min){
      _min = f;
    }
    if (f > _max){
      _max = f;
    }
  }
  _sum += f;
  _cnt++;
  _mean = _sum/_cnt;
  dev = f-_mean;
  _stddev = (_stddev+dev)/_cnt;
  //-------------------------------------------------
  //Slope Calculations
  //-------------------------------------------------
  _del = f-_old;
  _old = f;
  /*SerialUSB.print("Count : ");
  SerialUSB.println(_cnt);
  SerialUSB.print("Minimum Value : ");
  SerialUSB.println(_min);
  SerialUSB.print("Maximum Value : ");
  SerialUSB.println(_max);
  SerialUSB.print("Sum : ");
  SerialUSB.println(_sum);
  SerialUSB.print("Standard Deviation : ");
  SerialUSB.println(_stddev);
  //SerialUSB.print("Change in readings : ");
  //SerialUSB.println(_del);
  //SerialUSB.print("Target Value : ");
  //SerialUSB.println(calc_val);
  //SerialUSB.print("Err : ");
  //SerialUSB.println(_err/_cnt);
  //SerialUSB.println(" ");*/
}

void Ml::sample(int s)
{
  buff = (int*) malloc(s * sizeof(int));
  int curr_val;
  int mx_cnt = s;
  _mx_cnt = s;
  int count = 0;
  while(count<s){
    curr_val = _sample_data[count];
    //get_data();
    append(curr_val);
    buff[count] = curr_val;
    count++;
  }
}

int Ml::get_data()
{
  //Insert logic to get data
  //return analogRead(4);
  //append(5);
  int randi;
  randi = random(10,100);
  //SerialUSB.println(randi);
  return randi;
}

void Ml::regression(float inp_par, float inp_ar)
{
  float ar = inp_ar;
  float err = 1000; 
  float m = 5;
  float c = _mean;
  float calc_val;
  float alpha = 0.05;
  float err_1;
  float err_0;
  float toterr_0;
  float toterr_1;
  double cost = 1000; // Power and accuracy comparison using double and float
  int i = 0;
  float olderr = 8;
  float tot_cost = 10;
  int itno = 0;
  int boost = 1;
   SerialUSB.print("Adaptation ratio : ");
   SerialUSB.println(ar);
    //int maxcnt = inp_par;
    //SerialUSB.println("Regression");
    //while(tot_cost>inp_par){
    //while(itno<maxcnt){
    while(abs(olderr-tot_cost)>inp_par){
      // Reset Aggregation variables
      olderr = tot_cost;
      cost = 0;
      i = 0;
      toterr_1 = 0;
      toterr_0 = 0;
      // Begin iteration
      while(i<_mx_cnt){
        // Get Initial Estimate
        calc_val = m*(i+1) + c;
        // Calculate Cost and First Derivatives of Slope and Error
        cost = ((calc_val-buff[i])*(calc_val-buff[i]));
        err_0 = (calc_val-buff[i]);
        err_1 = (calc_val-buff[i])*(i - _min)/(_max-_min);
        // Aggregate Errors
        toterr_0 += err_0;
        toterr_1 += err_1;
        tot_cost += cost;
        i++;
      }
      // Calculate Iteration Cost
      tot_cost = tot_cost/(2*_mx_cnt);
      if(olderr>tot_cost){
        alpha = alpha*(1+ar);
      }
      else{
        alpha = alpha*(1-ar);
      }
      // Update Slope and Intercept
      m = m - (alpha*toterr_1/_mx_cnt);
      c = c - (alpha*toterr_0/_mx_cnt);
      itno++;
    }
    SerialUSB.print("Iterations : ");
    SerialUSB.println(itno);
    SerialUSB.print("Total Error :");
    SerialUSB.println(tot_cost);
    //SerialUSB.println( );
    SerialUSB.print("Slope : ");
    SerialUSB.println(m);
    SerialUSB.print("Intercept : ");
    SerialUSB.println(c);
    _slope = m;
    _inter = c;
  test();
  }

void Ml::test(){
 float mse;
  int curr_val;
  int count = _mx_cnt;
  while(count<_max_el){
    curr_val = (_slope*count)+_inter-_sample_data[count];
    //SerialUSB.print("Comparison Values : ");
    //SerialUSB.print((_slope*count)+_inter);
    //SerialUSB.print(" | ");
    //SerialUSB.println(_sample_data[count]);
    get_data();
    append(curr_val*curr_val);
    mse = mse+(curr_val*curr_val);
    count++;
    clear_all();
    sample(75);
  }
  mse = mse/(_max_el-_mx_cnt);
  SerialUSB.print("Mean Square Error on Test Dataset is : ");
  SerialUSB.println(mse);
  SerialUSB.println( );
}

