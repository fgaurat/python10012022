#include<stdio.h>
#include<stdlib.h>
#include"hello.h"




void sayHello()
{
    printf("Bonjour C\n");
}

void hello(const char *name)
{
    printf("Bonjour %s\n",name);
}