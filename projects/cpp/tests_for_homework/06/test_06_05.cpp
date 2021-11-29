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
#include"tasktemp_06_05.cpp"
using namespace std;


TEST(compare_numbers, Negative) {
          
        EXPECT_EQ(1, check_numbers(2,145,2))<<"Функция возвращает неправильное значение"<<"Не та функция";
        
        EXPECT_EQ(1, check_numbers(2,145,9))<<"Функция возвращает неправильное значение"<<"Не та функция";

        EXPECT_EQ(0, check_numbers(13,14,7))<<"Функция возвращает неправильное значение"<<"Не та функция";
        
       // EXPECT_EQ(333, subtr_summ(4597))<<"Функция возвращает неправильное значение"<<"Не та функция";

}

int main(int argc, char **argv) {
  printf("Running main() from sample1\n");
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}