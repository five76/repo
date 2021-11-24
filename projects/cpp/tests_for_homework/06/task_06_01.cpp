/*
Одноклеточная амеба каждые три часа делится на две клетки. Определить, через какое количество часов количество амеб превысит критический показатель N.
Процесс организовать с помощью функции func_ameba(int N)
Функция func_ameba принимает в качестве аргумента необходимое количество амеб N и возвращает время в часах, через которое оно было достигнуто
*/

#include<iostream>
using namespace std;

int func_ameba(int N)
{
  int result = 3;
  int k = 1;
  while (true)
  {
      k*=2;
      if (k>N) return result;
      result+=3;
  } 
  //...
  //return result;
}

int main()
{
  int N = 100000;
  cout<<func_ameba(N)<<endl;
}
