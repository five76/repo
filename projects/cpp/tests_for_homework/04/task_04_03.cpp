/*
Составить программы, печатающие значение True, если следующие указанные высказывания являются истинными, и значение False — в противном случае.
Координаты левой верхней и правой нижней вершин прямоугольника (x1, y1) и (х2, у2). Точка А(х,у) принадлежит прямоугольнику.

Процесс организовать с помощью функции check_point(int x1,int y1,int x2,int y2, int x, int y)
Функция принимает координаты вершин прямоугольника и точки, и возвращает 1 если точка принадлежит прямоугольнику, 0 - в противном случае
*/

#include<iostream>
#include<cmath>
#include<stdio.h>
using namespace std;

int check_point(int x1,int y1,int x2,int y2, int x, int y)
{
    if (x>=x1 && x<=x2 && y<=y1 && y>=y2)
        return 1;
    else
        return 0;
}

int main ()
{
    int x1,y1,x2,y2,x,y;
    cout<<"Введите координаты левой верхней вершины прямоугольника"<<endl;
    cin>>x1>>y1;
    cout<<"Введите координаты правой нижней вершины прямоугольника"<<endl;
    cin>>x2>>y2;
    cout<<"Введите координаты точки"<<endl;
    cin>>x>>y;

    if (check_point(x1,y1,x2,y2,x,y))
        cout<<"Точка принадлежит прямоугольнику"<<endl;
    else
        cout<<"Точка не принадлежит прямоугольнику"<<endl;
    
   // find_triangle_eq_square(a1, b1, c1);
    return 0;
}