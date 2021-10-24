/*
Услуги телефонной сети оплачиваются по следующему правилу: за разговоры до А Минут в месяц платится В рублей, 
а разговоры сверх установленной нормы оплачиваются из расчета С рублей за минуту. 
Вычислить плату за пользование телефоном для введенного времени разговоров за месяц.
Процесс организовать с помощью функции calc_pay(int A,int B,int C,int M)

Функция возвращает сумму оплаты
*/

#include<iostream>
#include<cmath>
#include<stdio.h>
using namespace std;

int calc_pay(int A,int B,int C,int M)
{
    int summa=0;
    if (M<=A)
        summa = B;
    else
        summa = B+(M-A)*C;
    return summa;
}

int main()
{
    int A,B,C,M;
    cout<<"Введите количество минут тарифа"<<endl;
    cin>>A;
    cout<<"Введите cтоимость данного тарифа"<<endl;
    cin>>B;
    cout<<"Введите стоимость минуты разговора сверх тарифа"<<endl;
    cin>>C;
    cout<<"Введите время фактического разговора в минутах"<<endl;
    cin>>M;

    cout<<"Стоимость разговора составляет "<<calc_pay(A,B,C,M)<<" рублей"<<endl;
    
   // find_triangle_eq_square(a1, b1, c1);
    return 0; 
}
