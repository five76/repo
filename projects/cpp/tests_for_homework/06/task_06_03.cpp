/*
Составить программу для нахождения суммы четных элементов последовательности целых чисел, неравных 0.

Спецификация (требование к работе программы): числа вводятся вручную. Окончанием ввода считается введения числа 0
*/

#include<iostream>
using namespace std;

int main()
{
    int sum=0;
    int x;
    int index;
    cout<<"Введите последовательность целых чисел не равных 0 . Для окончания ввод введите 0 ";
    cin>>x;
    index = 1;
    while (x!=0)
    {
        if (index%2==0) sum+=x;
        cin>>x;
        index++;
    }
    cout<<"сумма четных элементов последовательности целых чисел "<<sum<<endl;
}