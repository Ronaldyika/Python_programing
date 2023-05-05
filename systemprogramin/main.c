#include <stdio.h>
int main(){
//creating a file in c
FILE *fptr;
fptr = fopen("text.txt","w");
fprintf(fptr,"hello my guy\n");
fptr = fopen("text.txt","a");
fprintf(fptr,"this is the second stuff added\n");
fclose(fptr);
return 0;
}
