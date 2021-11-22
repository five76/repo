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
#include"tasktemp_12_02.cpp"
using namespace std;
//typedef double D;

TEST(square_quadr, Negative) {
          
        EXPECT_EQ(11.99, square_quadr(3.0,4.0,3.0,4.0,90.0,90.0))<<"Функция возвращает неправильное значение"<<"Не та функция";
        EXPECT_EQ(20, square_quadr(3.0,4.0,5.5,6.1155,90.0,75.0))<<"Функция возвращает неправильное значение"<<"Не та функция";

}

int main(int argc, char **argv) {
  printf("Running main() from sample1\n");
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}