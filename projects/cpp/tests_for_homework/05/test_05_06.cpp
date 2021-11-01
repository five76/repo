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
#include "tasktemp_04_06.cpp"
using namespace std;

TEST(check_point, Negative) {
        // This test is named "Negative", and belongs to the "FactorialTest"
        // test case
        EXPECT_EQ(1, check_circle(0,0,3,5,5,5))<<"Функция возвращает неправильное значение"<<"Не та функция";
        EXPECT_EQ(1, check_circle(5,5,2,17,5,10))<<"Функция возвращает неправильное значение";
        EXPECT_EQ(0, check_circle(5,5,2,17,5,9))<<"Функция возвращает неправильное значение";
        EXPECT_EQ(0, check_circle(-5,-5,5,5,5,5))<<"Функция возвращает неправильное значение";
}


int main(int argc, char **argv) {
  printf("Running main() from sample1\n");
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}