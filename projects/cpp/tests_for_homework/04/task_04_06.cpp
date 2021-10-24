/*
Два круга заданы координатами своих центров и радиусами — соответственно x1, y1, r1 и х2, у2, r2. 
Определить, пересекаются ли эти круги.
Процесс организовать с помощью функции check_circle(int x1,int y1,int r1, int x2,y2,int r2).
Функция принимает координаты центров и радиусы кругов и возвращает 1 если круги пересекаются, 0 - в противном случае
*/
#include<iostream>
#include<cmath>
#include<stdio.h>
using namespace std;

int check_circle(int x1,int y1,int r1, int x2,int y2,int r2)
{
    float r;
    r=sqrt(pow(abs(x2-x1),2)+pow(abs(y2-y1),2));
    cout<<r<<endl;
    if (r<=(r1+r2))
    {
        
        return 1;
    }
    else
        return 0;
}

int main()
{
    int x1,x2,y1,y2,r1,r2;
    cout<<"Введите координаты центра первой окружности"<<endl;
    cin>>x1>>y1;
    cout<<"Введите радиус первой окружности"<<endl;
    cin>>r1;
    cout<<"Введите координаты центра второй окружности"<<endl;
    cin>>x2>>y2;
    cout<<"Введите радиус второй окружности"<<endl;
    cin>>r2;
    if (check_circle(x1,y1,r1,x2,y2,r2))
        cout<<"Окружности пересекаются"<<endl;
    else
        cout<<"Окружности не пересекаются"<<endl;
    return 0;
}