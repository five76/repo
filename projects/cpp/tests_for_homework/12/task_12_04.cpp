/*
Из заданного числа вычесть сумму его цифр. Из полученного результата также вычесть сумму его цифр и т.д. 
Определить,сколько требуется выполнить таких действий, чтобы получить нуль.
Вычитание суммы цифр из числа оформить в виде функции subtr_summ(int n)
Спецификация функции subtr_summ:
Вход - целое число n
Выход - разность между суммой цифр и исходным числом
*/
#include<iostream>
#include<cmath>
#include<stdio.h>

//#include"task_12_06.cpp"
using namespace std;
int result = 0;
//int sum_digits(int num)

//нахождение сумм цифр числа
int sum_digits(int num)
{
	int sd = 0;
	while (num>=10)
	{
		sd+= num %10;
		num = num/10;
	}
	sd+=num;
	return sd;
} 

//подсчтет количества итераций для достжения 0 при вычитании из числа суммы его цифр
int subtr_summ(int n)
{
    if (n==0) return result;
    int k = sum_digits(n);
    //cout<<n<<" - "<<k<<endl;
    result++;
    subtr_summ(n-k);
}

int main()
{
    cout<<subtr_summ(4597);
    return 0;
}