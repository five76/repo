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
#include "tasktemp_04_03.cpp"
using namespace std;

TEST(check_point, Negative) {
        // This test is named "Negative", and belongs to the "FactorialTest"
        // test case
        EXPECT_EQ(1, check_point(0,5,5,0,2,2))<<"Функция возвращает неправильное значение";
        EXPECT_EQ(1, check_point(5,5,10,0,6,4))<<"Функция возвращает неправильное значение";
        EXPECT_EQ(0, check_point(5,5,10,0,-2,3))<<"Функция возвращает неправильное значение";
        EXPECT_EQ(0, check_point(-3,-3,2,5,0,6))<<"Функция возвращает неправильное значение";
}

int main(int argc, char **argv) {
  printf("Running main() from sample1\n");
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}