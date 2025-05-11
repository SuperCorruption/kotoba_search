#include <stdio.h>

int main(void)
{
    int i;

    for (i = 1; i <= 15; i++)
    {
        if (i % 3 == 0 && i % 5 != 0)
        {
            printf("%d! ", i);
        }
        if (i % 5 == 0)
        {
            printf(" ");
        }
        if (i % 3 != 0 && i % 5 != 0)
        {
            printf("%d ", i);
        }
    }

    return 0;
}
