#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_SIZE 1024

void estado0(char *, int *);
void estado1(char *, int *);
void estado2(char *, int *);
void estado3(char *, int *);
void estado4(char *, int *,int);
void initAutomata(char *, int *);
void manual(char *, int *);
void automatico();
void lectura();

void manual(char *cad, int *p)
{
	initAutomata(cad, p);
}
void lectura()
{
	int posicion = 0;
	FILE* entrada = fopen("PruebaTuring.txt","r+");
	char str[MAX_SIZE];

	if(entrada == NULL)
	{
		perror("Error archivo");
		exit(-1);
	}

	fgets(str, MAX_SIZE, entrada);
	initAutomata(str, &posicion);
	fclose(entrada);
}

int main()
{
	//int argc, char **argv
	int posicion = 0;
	int seleccion;
	char *cadena;

	printf("Seleccione una opcion\n[1] Lectura de archivo\n[2] Manual\n[3] Random\n[4] Salir\n");
	scanf("%i", &seleccion);
	
	switch(seleccion){
	case 1:lectura();
	case 2:printf("Ingrese una cadena de 1's y 0's:");scanf("%s",cadena);printf("Revise el archivo Salida Turing.txt para ver resultados\n");manual(cadena,&posicion);	
	case 3: printf("Revise el archivo SalidaTuring.txt para ver los resultados\n");automatico();
	case 4: printf("Saliendo...");
		break;
	default:
		printf("Ingrese una opcion valida\n");
		main();
	}
	return 0;
}


void automatico(){
	char *cadena;
	int posicion = 0;
	int random, random2;
	time_t t;
            srand((unsigned)time(&t));	
            random = rand()%1000+1;
            for (int i = 0; i<random; i++){
			random2 = rand()%1000+1;
			if (random2%2==0){
				cadena[i] = '0';			
			} else {
				cadena[i] = '1';			
			}				
		}
            initAutomata(cadena,&posicion);

}
void estado0(char *cad, int *p)
{
	char var;
	var = cad[*p];
	cad[*p] = '*';
	fprintf(stdout, "q0 Posicion cadena %d - %s\n", *p, cad);
	cad[*p] = var;
	cad[*p] = 'X';
	(*p)++;
	if(cad[*p] == '1')
		estado2(cad, p);
	else if(cad[*p] == 'X' || cad[*p] == 'Y' || cad[*p] == '0')
		estado1(cad, p);
	else
		estado4(cad, p,0);
}
void estado1(char *cad, int *p)
{
	char var;
	var = cad[*p];
	cad[*p] = '*';
	fprintf(stdout, "q1 Posicion cadena %d - %s\n", *p, cad);
	cad[*p] = var;
	(*p)++;
	if(cad[*p] == '1')
		estado2(cad, p);
	else if(cad[*p] == 'X' || cad[*p] == 'Y' || cad[*p] == '0')
		estado1(cad, p);
	else
		estado4(cad, p,1);
}
void estado2(char *cad, int *p)
{
	char var;
	var = cad[*p];
	cad[*p] = '*';
	fprintf(stdout, "q2 Posicion cadena %d - %s\n", *p, cad);
	cad[*p] = var;
	cad[*p] = 'Y';
	(*p)--;
	if(cad[*p] == '0' && cad[*p-1] == 'X')
		estado0(cad, p);
	else if(cad[*p] == 'Y' || cad[*p] == '0' || cad[*p] == 'X')
		estado3(cad, p);
	else
		estado4(cad, p,2);
}
void estado3(char *cad, int *p)
{
	char var;
	var = cad[*p];
	cad[*p] = '*';
	fprintf(stdout, "q3 Posicion cadena %d - %s\n", *p, cad);
	cad[*p] = var;
	(*p)--;
	if(cad[*p] == '0'&& cad[*p-1] == 'X')
		estado0(cad, p);
	else if(cad[*p] == 'Y' || cad[*p] == '0' || cad[*p] == 'X')
		estado3(cad, p);
	else if (cad[*p] == '\0')
		for(int i = 0; cad[i] != '0' || cad[i]=='1'; i++)
			{if (cad[i] == '0' || cad[i] == '1')
				{estado4(cad,p,3);}
			else
				{estado4(cad,p,4);}}
}
void estado4(char *cad, int *p,int estado)
{

	fprintf(stdout, "\nq%d Posicion cadena %d - %s\n",estado,*p,cad);
	fprintf(stdout, "Terminado\n");
	exit(2);
}
void initAutomata(char *cad, int *p)
{
	freopen("SalidaTuring.txt","w+",stdout);
	if(*p < strlen(cad))
		{if(cad[0] == '0'){
			estado0(cad, p);}
		else
			{fprintf(stderr, "Cadena no aceptada\n");}}
	
	fclose(stdout);
	exit(1);
}
