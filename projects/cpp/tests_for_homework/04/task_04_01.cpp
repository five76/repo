/*
Составить программ, печатающие значение True, если следующие указанные высказывания являются истинными, и значение False — в противном случае.

Квадрат заданного трехзначного числа равен кубу суммы цифр этого числа.

Процесс организовать с помощью функции check_cub(int num)
Функции передается число. Возвращает 1 если утверждение истино, 0 - в противном случае 
*/

#include<iostream>
#include<cmath>
using namespace std;
int check_cub(int num)
{
    int kv=0;
    int result=0;
    int sum_dig=0;
    int s,d,e;
    s = num/100;
    num = fmod(num,100);
    d = num/10;
    e = fmod(num,10);
    cout<<"Сотни "<<s<<endl;
    cout<<"Десятки "<<d<<endl;
    cout<<"Единицы "<<e<<endl;
    if (pow(num,2) == pow((s+d+e),3))
    {
        result = 1;
    }
    return result;
}

int main()
{
    int x;
    int result;
    cout<<"Введите число"<<endl;
    cin>>x;
    result = check_cub(x);
    cout<<result<<endl;
    return 0;
}
