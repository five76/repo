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
#include"tasktemp_12_06.cpp"
using namespace std;

TEST(happy_ticket, Negative) {
        // This test is named "Negative", and belongs to the "FactorialTest"
        // test case
        EXPECT_EQ(5802, happy_ticket(111111,222222))<<"Функция возвращает неправильное значение"<<"Не та функция";
        EXPECT_EQ(25978, happy_ticket(111111,555555))<<"Функция возвращает неправильное значение"<<"Не та функция";
        EXPECT_EQ(37927, happy_ticket(333333,999999))<<"Функция возвращает неправильное значение"<<"Не та функция";

}


int main(int argc, char **argv) {
  printf("Running main() from sample1\n");
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}