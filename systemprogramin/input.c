#include<stdio.h>
int main(){
int age;
char name[] = "";
printf("enter your age and name: ");
scanf("%d %s",&age,&name);
printf("my name is %s\n",name);
printf("i am %d years\n",age);
return 0;
}
