#include <stdio.h>
#include <stdlib.h>
#include "libmedia.h" 

int main(int argc, char *argv[]){
  int bim1, bim2, med;
  printf("Media IFRN\n");
  printf("Bimestre 1:");
  scanf("%d",&bim1);
  printf("Bimestre 2:");
  scanf("%d",&bim2);
  med = mediaifrn(bim1,bim2);
  printf("media IFRN = %d\n",med);
  exit(0);
}
