/*
Задача:
Составить программу вычисления корней квадратного уравнения ax^2+bx+c=0
Решение должно содержать 3 функции: discr,root_x1,root_x2

Спецификация функций:
discr:
Назначение - вычисление дискриминанта
Вход - вещественные коэффициенты квадратного уравнения (double a,double b,double c)
Выход - вещественное значение дискриминанта

root_x1:
Назначение - вычисление первого (единственного) корня
Вход - вещественные коэффициенты квадратного уравнения и дискриминант (double a,double b,double d)
Выход - вещественное значение первого (единственного) корня

root_x2:
Назначение - вычисление второго корня
Вход - вещественные коэффициенты квадратного уравнения и дискриминант (double a,double b,double d)
Выход - вещественное значение второго корня

*/

#include<iostream>
#include<fstream> //библиотека для работы с файлами
#include <cstdio>
#include<cmath>
using namespace std;

//Прототипы функции
double discr(double a,double b, double c);
double root_x1(double a,double b,double d);
double root_x2(double a,double b,double d);

//Основная программа----------------------
int main(){
	double a,b,c;
	double x1,x2;
	double d;
	cout<<"Введите коэффициенты квадратного уравнения"<<endl;
	cin>>a>>b>>c;
	d = discr (a,b,c);
	if (d >= 0)
	{
		x1 = root_x1(a,b,d);
		x2 = root_x2(a,b,d);
		printf("x1 = %5.2f, x2 = %5.2f",x1,x2);
	}
	else
	{
		cout<<"Действительных корней нет"<<endl;
	}

}
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//Определение функций
//Функция вычисления дискриминанта
double discr(double a,double b, double c){
	double D;
	D=pow(b,2.0)-4*a*c;
	return D;
}

//Функции вычисления корней
double root_x1(double a,double b,double d){
	double x1;
	x1 = (-b-sqrt(d))/(2*a)	;
	return x1;
}

double root_x2(double a,double b,double d){
	double x1;
	x1 = (-b+sqrt(d))/(2*a)	;
	return x1;
}
