/*
Составить программы, печатающие значение True, если следующие указанные высказывания являются истинными, и значение False — в противном случае.
Даны три стороны одного треугольника и три стороны другого. Эти треугольники равновеликие, т.е. имеют равные площади.

Процесс организовать с помощью функции check_tr(int a1,int b1,int c1,int a2,int b2,int c2).
Функция принимает три стороны одного и три стороны другого треугольника, и возвращает 1 если утверждение истино, 0 - в противном случае
*/

#include<iostream>
#include<cmath>
#include<stdio.h>
using namespace std;

float square_triangle(float a, float b, float c)
{
    float S;
    float p;
    p = (a+b+c)/2;
    S = sqrt(p*(p-a)*(p-b)*(p-c));
    //printf("Площадь равна %5.3f\n",S);
    return S;
}

int check_tr(int a1,int b1,int c1,int a2,int b2,int c2)
{
    float S1,S2;
    S1 = square_triangle(a1,b1,c1);
    S2 = square_triangle(a2,b2,c2);
    if (S1 == S2) 
        return 1; 
    else 
        return 0;
}

int main ()
{
    int a1, b1, c1;
    int a2, b2, c2;
    cout<<"Введите стороны первого треугольника"<<endl;
    cin>>a1>>b1>>c1;
 
    cout<<"Введите стороны второго треугольника"<<endl;
    cin>>a2>>b2>>c2;
    if (check_tr(a1, b1, c1, a2, b2, c2))
        cout<<"Треугольники равновеликие"<<endl;
    else
        cout<<"Треугольники имеют разные площади"<<endl;
    
   // find_triangle_eq_square(a1, b1, c1);
    return 0;
}