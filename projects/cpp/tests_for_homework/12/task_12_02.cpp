/*
Длины сторон четырехугольника заданы числами X, Y, Z, Т.
Вычислить его площадь, если угол между сторонами X и Y равен A(град), а между сторонами Z и T B(град.)

Вычисление площади оформить в виде фунции square_ quadr
Спецификация функции square_quadr
* Вход - целочисленные длины сторон и углы (град) между ними square_ quadr(int X,int Y, int A,int Z,int T, int B)
* Выход - вещественное значение площади 
* Примечание - математическая модель приведена на рис. task_12_02.png. 
Перед использованием тригонометрических функций градусную меру угла необходимо перевести в радианы
*/

#include<iostream>
#include<stdio.h>
#include<cmath>
#define PI 3.14;
typedef double D;
using namespace std;
//D square_quadr(D,D,D,D,D,D);
D  square_quadr(D X, D Y, D Z, D T, D A, D B)
{
    double result=0;
    double rad_A ;
    double p = (X+Y+Z+T)/2;
    rad_A = A/180.0*PI;
    double rad_B = B/180.0*PI;
    //cout<<rad_A<<"  "<<rad_B<<endl;
    result = sqrt((p-X)*(p-Y)*(p-Z)*(p-T)-X*Y*Z*T*pow(cos((rad_A+rad_B)/2),2));
    return int(result*100)/100.0;
}

int main()
{    
    D X=3.0;
    D Y=4.0;
    D Z=5.5;
    D T=6.1155;
    D A = 90.0;
    D B = 75.0;
    //double A,B;
    /*
    cout<<"Введите стороны четырехугольника"<<endl;    
    cin>>X>>Y>>Z>>T;
    cout<<"Введите угол м/д сторонами X и Y четырехугольника"<<endl;    
    cin>>A;
    cout<<"Введите угол м/д сторонами Z и T четырехугольника"<<endl;    
    cin>>B;
    */
    cout<<square_quadr( X,  Y,Z,  T, A,  B);
    return 0;
    

}

