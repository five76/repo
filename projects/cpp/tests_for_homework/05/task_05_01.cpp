/*
Одноклеточная амеба каждые три часа делится на две клетки. Определить, сколько амеб будет через 3, 6 , 9, 12, ..., 3n часов.
Процесс организовать с помощью функции func_ameba(int n)
Функция func_ameba принимает в качестве аргумента количество часов n и возвращает количество через 3n часов
*/
#include<iostream>
#include<cmath>
#include<stdio.h>
using namespace std;

int func_ameba(int n)
{
    int k=1;
    for (int i=1;i<=3*n;i++)
    {
        k = pow(2,i);
        if (i%3 == 0)
        {
           printf("\nКоличество амеб через %d часов равно %d",i,k);
        }
    }
    return k;
}

int main()
{
    int k=1;
    int n=2;
    k = func_ameba(n);
    printf("\nКоличество амеб через %d часов равно %d",3*n,k);
    return 0;
}