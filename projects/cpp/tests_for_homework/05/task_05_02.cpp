/*
Составить программу для решения следующей задачи: сколько можно купить быков, коров и телят, 
платя за быка 10 р., за корову — 5 р., а за теленка — 0,5 р., если на 100 р. надо купить 100 голов скота?
*/

#include<iostream>
#include<cmath>
#include<stdio.h>
using namespace std;

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
}