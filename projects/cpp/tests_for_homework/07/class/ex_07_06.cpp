/*
    В одномерном массиве все отрицательные элементы пе­реместить в начало, а остальные — в конец с сохранением по­рядка следования, не используя при этом дополнительный массив.
*/

#include<iostream>
#include<ctime>
#include<cmath>
using namespace std;

void print_arr(int *a,int len)
{
    for (int i=0;i<len;i++){
        cout<<a[i]<<" ";
    }
}


int main()
{
    int A[]={2,-2,-3,3,5,7,-6,2,8,9,-1,0};
    
    int i,j;
    int temp;
    int len=sizeof(A)/sizeof(A[0]);

    print_arr(A,len);
    
    for (i=0;i<len;i++)
    {
        temp=A[i];
        if (temp<0)
        {
            for (j=i-1; A[j]>0 && j>=0;j--)
            {
                A[j+1]=A[j];
            }
            A[j+1]=temp;
        }
    }
    cout<<endl;
    print_arr(A,len);
   return 0;
}