nclude <stdio.h>
int main(int argc,char **argv)
{
FILE *infile;
infile=fopen(argv[1],"r");
cahr c;
while((c=fgetc(infile))!=EOF)
{
putchar(c);
}
}
