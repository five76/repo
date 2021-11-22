/*
Дано простое число. Составить функцию find_simple_number, которая будет находить следующее за ним простое число.
Спецификация find_simple_number:
Вход - целое простое число N
Выход - следующее простое число
*/

#include<iostream>
#include<stdio.h>
#include<cmath>

using namespace std;

 int find_simple_number(int N)
 {
    int result = 0;
    while (true)
    {
       N++;
       if ((N%2!=0) && (N%3!=0) && (N%5!=0) && (N%7!=0)) return N;
    }
 }

int main()
{
   cout<<find_simple_number(457)<<endl;
   return 0;
}