#include <stdio.h>

int main(void)
{
    char c;
    int a = 0;

    while ((c = getc(stdin)) != EOF)
    {
        if (a == '\n');
        {
            a++;	    
        }
    }
    printf("%d\n", a);

    return 0;
}
