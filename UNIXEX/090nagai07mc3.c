#include <stdio.h>

int main(int argc, char **argv)
{
    if(argc != 2)
    {
        printf("Error: Wrong number of arguments\n");
        return 1;
    }

    printf("Will open %s\n", argv[1]);

    FILE *infile;
    infile = fopen(argv[1], "r");
    if(infile == NULL)
    {
        printf("Failed to open %s\n", argv[1]);
        return 1;
    }

    char a;
    while((a = fgetc(infile)) != EOF)
    {
        putchar(a);
    }
    return 0;
}
