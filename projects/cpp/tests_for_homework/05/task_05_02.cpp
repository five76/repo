/*
Составить программу для решения следующей задачи: сколько можно купить быков, коров и телят, 
платя за быка (bull) 10 р., за корову (cow) — 5 р., а за теленка (calf) — 0,5 р., если на X р. надо купить Y голов скота?

Решение оформить в виде функции pay_cattle 
Вход: 2 аргумента
    целое X - имеющаяся сумма, 
    целое Y - необходимое количество голов скота  
Выход: строка в формате "bull count_bull;cow count_cow;calf count_calf"
*/

#include<iostream>
#include<cmath>
#include<stdio.h>
#include<string>
using namespace std;

string pay_cattle(int X, int Y)
{
    string result="";
    return result;
}


int main()
{
    int cb ;
    int ck ;
    int ct ;
    float pb = 10;
    float pk = 5;
    float pt = 0.5;
    float pay = 0;
    float summa = 100;
    for (cb=0;cb<=summa/pb;cb++)
        for (ck=0;ck<=summa/pk;ck++)
            for (ct=0;ct<=summa/pt;ct++)
            {
                if (cb*pb+ck*pk+ct*pt == summa && cb+ck+ct == 100)
                    cout<<"Быков - "<<cb<<" Коров - "<<ck<<" Телят - "<<ct<<endl;
            }
    //pay_cattle(100, 100);
    return 0;
}