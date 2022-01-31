/*
Дано действительное число x. Вычислить выражение:
*/

#include<iostream>
#include<cmath>
#include<stdio.h>
using namespace std;

long int factorial(int num)
{
    long int result=1;
    for (int i = 1;i<=num;i++)
    {
        result*=i;
    }
    return result;
}

int main()
{
    double znamenatel;
    double chislitel;
    double x=2.0;
    double summa=0;
    float znak = 1.0;
    for  (int i=1;i<=13;i=i+2)
    {
        
        chislitel = pow(x,i);
        znamenatel = factorial(i);
        summa += znak *(chislitel/znamenatel);
        //cout<<i<<" "<<chislitel<<" "<< znamenatel<<" "<<(chislitel/znamenatel)<<" "<<summa<<endl;
        znak = znak *(-1.0);
    }
    printf("\n%5.3f\n",summa);
}

