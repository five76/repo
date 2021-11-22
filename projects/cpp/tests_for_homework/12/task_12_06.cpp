/*
Имеется часть катушки с автобусными билетами. Номер билета шестизначный. Определить количество счастливых билетов на катушке, если меньший номер билета — N, а больший — М.
(Билет является счастливым, если сумма трех первых его цифр равна сумме трех последних цифр.)
Процесс организовать с использованием функции happy_ticket

Спецификация функции happy_ticket
---------------------------------
* Вход - целочисленные значения наименьшего и наибольшего номеров на катушке - (int N, int M) 
* Выход - количество счастливых билетов на катушке 

*/
#include<iostream>
#include<cmath>
#include<stdio.h>
using namespace std;

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

int happy_ticket(int N, int M)
{
	int result=0;
	int beg,end;
	int cht=0;
	for (int i=N;i<=M;i++)
	{
		beg = i/1000;
		end = i%1000;
		int sd_beg = sum_digits(beg);
		int sd_end = sum_digits(end);
		if (sd_beg == sd_end)
		{
			//printf("%6d - %3d - %3d  - %3d - %3d \n",i,beg,sd_beg,end,sd_end);
			result++;
		}
		//cout<<N<<" - "<<beg<<" - "<<" "<<end<<endl;

	}
	return result;
}

int main()
{	
	int cht=0;
	int N = 333333;
	int M = 999999;
	cht = happy_ticket(N,M);
	cout<<"Count of happy tickets - "<<cht<<endl;
	return 0;
}

