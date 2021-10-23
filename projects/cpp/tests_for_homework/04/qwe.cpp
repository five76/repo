//#include "../prog.cpp"
//#include "../math_add.cpp"
//https://www.programmersought.com/article/63646304754/
//running
//g++ simple_test.cpp -lgtest  -lpthread
//./a.out
//CMake - https://habr.com/ru/post/155467/
#include "gtest/gtest.h"
#include "stdio.h"
#include <iostream>
using namespace std;

int Factorial (int num) {
  if (!num)return 1;
  if (num<0)return -1;
  return num*Factorial(num-1);
}

// Tests Factorial()
// Tests factorial of negative numbers.

TEST(FactorialTest, Negative) {
        // This test is named "Negative", and belongs to the "FactorialTest"
        // test case
        EXPECT_EQ(-1, Factorial(-5));
        EXPECT_EQ(-1, Factorial(-1));
        EXPECT_LT(Factorial(-10), 0);
}
/*
// Tests factorial of 0.<
TEST(FactorialTest, Zero) {
        EXPECT_EQ(1, Factorial(0));
}
// Tests factorial of positive numbers.
TEST(FactorialTest, Positive) {
        EXPECT_EQ(0, Factorial(1))<<"Error in calculate";
        EXPECT_EQ(2, Factorial(2));
        EXPECT_EQ(6, Factorial(3));
        EXPECT_EQ(40320, Factorial(8));
}
*/
/*
TEST(main1, Negative) {
        // This test is named "Negative", and belongs to the "FactorialTest"
        // test case
        EXPECT_EQ(5, main1());
        //EXPECT_EQ(-1, Factorial(-1));
        //EXPECT_LT(Factorial(-10), 0);
}
*/
int main(int argc, char **argv) {
  printf("Running main() from sample1\n");
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
  //int a;
  //a=Factorial (3);
 // cout<<a<<endl; 
}