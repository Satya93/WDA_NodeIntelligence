#ifndef Ml_h
#define Ml_h

#include <math.h>;

class Ml
{
  public:
    void clear_all();
    void append(float);
    int count();
    float sum();
    float average();
    float minimum();
    float maximum();
    float std_dev();
    void sample_sensor(int, int);
    void regression(float,float);
    void sample(int,int);
    void test();
    int _sample_data[100] = {-3,0,-2,7,4,0,12,13,9,9,4,14,10,10,16,12,24,24,9,13,12,27,27,30,30,29,20,34,18,22,37,33,40,42,24,34,45,40,29,40,36,48,46,35,53,51,40,44,41,43,56,61,52,51,57,62,56,59,54,59,57,64,64,70,58,69,67,73,67,61,78,79,82,69,78,72,76,86,86,87,71,79,86,73,79,82,87,91,85,99,94,98,85,92,99,104,106,92,106,98};
    //int _sample_data[100] = {81,5,7,37,23,7,9,71,90,19,74,82,72,20,23,34,81,35,18,84,28,86,96,73,80,17,55,87,74,20,24,64,79,74,6,47,32,57,62,31,30,34,5,79,73,5,72,6,100,51,43,53,72,18,49,93,76,65,28,67,26,83,19,98,48,37,80,69,89,90,98,87,36,13,14,52,74,88,85,58,87,51,88,32,87,50,74,27,67,6,79,22,65,52,70,82,94,91,55,94};
    int get_data();
    int _max_el = 100;
    int _train_el = 75;
    int _test_el = 25;
    float _slope;
    float _inter;

  protected:
    int _old;
    long _cnt;
    float _store;
    float _sum;
    float _min;
    float _max;
    float _mean;
    float _del;
    float _stddev;
    float _variance;
    float _err;
    int _mx_cnt;
    int _pin = 4;
};
#endif
