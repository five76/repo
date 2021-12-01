/*
Вычислить площадь правильного шестиугольника со стороной а, используя подпрограмму вычисления площади треугольника.
Решение выполнить с использованием функции square_triangle(int a)
Спецификация:
-------------
* Назначение - вычисление площади правильного треугольника
* Вход - целочисленное значение стороны a
* Выход - вещественное значение площади треугольника

double square_triangle(int a)
{
	//...
}

*/
#include<iostream>
#include<stdio.h>
#include<cmath>

using namespace std;


double square_triangle(int a)
{
        double S = (a*a)*sqrt(3)/4;
        return int(S*1000)/1000.0; //округление до 3 знаков после запятой
}

int main()
{
        int a = 8;
        cout<<square_triangle(a)<<endl;
        cout<<3*a*a*sqrt(3)/2<<endl;
        return 0;
}


