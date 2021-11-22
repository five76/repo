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
#include"tasktemp_12_05.cpp"
using namespace std;

TEST(change_num, Negative) {
        // This test is named "Negative", and belongs to the "FactorialTest"
        // test case
        EXPECT_EQ(20, change_num("24",8,2))<<"Функция возвращает неправильное значение"<<"Не та функция";
        EXPECT_EQ(227, change_num("11100011",2,8))<<"Функция возвращает неправильное значение"<<"Не та функция";
        EXPECT_EQ(16, change_num("121",3,3))<<"Функция возвращает неправильное значение"<<"Не та функция";

}


int main(int argc, char **argv) {
  printf("Running main() from sample1\n");
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}