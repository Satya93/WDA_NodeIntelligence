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
    void regression(float,float);
    void sample(int,int);
    void test();
    int _sample_data[100] = {-3,0,-2,7,4,0,12,13,9,9,4,14,10,10,16,12,24,24,9,13,12,27,27,30,30,29,20,34,18,22,37,33,40,42,24,34,45,40,29,40,36,48,46,35,53,51,40,44,41,43,56,61,52,51,57,62,56,59,54,59,57,64,64,70,58,69,67,73,67,61,78,79,82,69,78,72,76,86,86,87,71,79,86,73,79,82,87,91,85,99,94,98,85,92,99,104,106,92,106,98};
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
