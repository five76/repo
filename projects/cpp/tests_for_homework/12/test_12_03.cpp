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
#include"tasktemp_12_03.cpp"
using namespace std;


TEST(find_simple_number, Negative) {
          
        EXPECT_EQ(13, find_simple_number(11))<<"Функция возвращает неправильное значение"<<"Не та функция";
        EXPECT_EQ(53, find_simple_number(47))<<"Функция возвращает неправильное значение"<<"Не та функция";
        EXPECT_EQ(461, find_simple_number(457))<<"Функция возвращает неправильное значение"<<"Не та функция";

}

int main(int argc, char **argv) {
  printf("Running main() from sample1\n");
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}