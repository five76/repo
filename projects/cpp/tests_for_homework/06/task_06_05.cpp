/*
Даны натуральные числа n и k. Составить программу для проверки, есть ли в записи числа n*k цифра d
Решение оформить с помощью функции check_numbers(int n, int k, int d)
Функция принимает три целочисленных аргумента n,k,d и возвращает 1, если условие выполнено. 
В противном случае функция возвращает значение 0
*/
#include<iostream>
using namespace std;

int check_numbers(int n, int k, int d)
{
  int result = 0;
  int temp = n*k;
  cout<<temp<<endl;
  while (temp>=1)
  {
    if (temp%10 == d) return 1;
    temp = temp/10;
  }
  return 0;
}

int main()
{
  int n=13;
  int k= 14;
  cout<<check_numbers(n, k, 8)<<endl;
}
