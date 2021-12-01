/*
Дана символьная строка, представляющая собой запись на­турального числа в p-ричной системе счисления (2 < р < 9). 
Переве­сти это число в десятичную систему счисления.
*/
#include<iostream>
#include<cmath>
#include<stdio.h>
#include<string> //библиотека работы со строками
using namespace std;

int S;
int change_num(string num, int p,int d)
{
    S=0;
    int l;
    string a;
    string ss;
    a=num;
    l=num.length();
    if (l>1) change_num(num.assign(num,0,l-1),p,d);
    
    ss = a[a.length()-1];
    S = S + stoi(ss) * pow(p,d-l);
    return S;
}

int main()
{
    int res = 0;
    string a="11100011";
    res = change_num(a, 2,a.length());
    cout<<res<<endl;
    return 0;
}
