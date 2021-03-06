/*
Ежемесячная стипендия студента составляет сумму А рублей, а расходы на проживание превышают стипендию и составляют сумму В рублей в месяц. 
Рост цен ежемесячно увеличивает расходы на 3 %. 
Рассчитать сумму, которую следует единовременно попросить у родителей, чтобы прожить учебный год (10 месяцев), 
используя только эти деньги и стипендию.
Процесс организовать с помощью функции func_summ(int A, int B)
Функция func_summ принимает в качестве аргументов стипендию и расходы и возвращает сумму, которую необходимо попросить у родителей
*/
#include<iostream>
#include<cmath>
#include<stdio.h>
using namespace std;


float func_summ(int A, int B)
{
    float summa = B; 
    for (int i=2;i<=10;i++)
    {
        B*=1.03;
        summa+=B;    
    }
    return summa - A*10;
}

int main()
{
    float st;
    float ras;
    cout<<"Стипендия?";
    cin>>st;
    cout<<"Расходы в месяц?";
    cin>>ras;
    cout<<"У родителей необходимо попросить"<<func_summ(st,ras)<<" рублей"<<endl;
    return 0;
}
