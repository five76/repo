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
#include "tasktemp_05_04.cpp"
using namespace std;

TEST(func_summ, Negative) {
        // This test is named "Negative", and belongs to the "FactorialTest"
        // test case
        EXPECT_EQ(12904, func_summ(1000,2000))<<"Функция возвращает неправильное значение";
        EXPECT_EQ(13127, func_summ(1500,2456))<<"Функция возвращает неправильное значение";
}

int main(int argc, char **argv) {
  printf("Running main() from sample1\n");
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}