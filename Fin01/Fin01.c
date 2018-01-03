#define FALSE 1
#define TRUE 0

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int  revision(char[]);
void checkin(char[]);
void constructorMatriz(char[], int);
void printing(char[],int);



int revision(char numeros[])
{
    
    int i=0, error=0;
    do{
        if(numeros[i]!='0' && numeros[i]!='1')
            error=1;
        i++;
    }while(numeros[i]!='\0');
    return error;
}

void checkin(char numeros[])
{
    int i=0, tamano=0, estado=0;
    do{
        tamano++;
        i++;
    }while(numeros[i]!='\0');
    printf("\n\t************RUTA DIRECTA*************\n \n|\t\t|\t\t|\n|\t->\t|\tq0\t|\n");
    for(i=0; i<=tamano; i++)
    {
        if(estado==0 && numeros[i]=='1')
            {printf("|\t%c\t|\tq0\t|\n", numeros[i]);}
        else if(estado==2 && numeros[i]=='1')
            {printf("|\t%c\t|\tq0\t|\n", numeros[i]); estado=0;}
        else if(estado==0 && numeros[i]=='0')
            {printf("|\t%c\t", numeros[i]); estado=1; printf("|\tq%d\t|\n", estado);}
        else if(estado==1 && numeros[i]=='1')
            {
                printf("|\t%c\t", numeros[i]);
                estado=2;
                if(i==tamano-1)
                   printf("|\tq%d <---\t|\n", estado);
                else
                    printf("|\tq%d\t|\n", estado);
            }
        else if(estado==1 && numeros[i]=='0')
            {printf("|\t%c\t", numeros[i]); estado=1; printf("|\tq%d\t|\n", estado);}
        else if(estado==2 && numeros[i]=='0')
            {printf("|\t%c\t", numeros[i]); estado=1; printf("|\tq%d\t|\n", estado);}
    }
    printf("\n\n");
    constructorMatriz(numeros, tamano);
	return;
}

void constructorMatriz(char numeros[], int total)
{
    int i, estado=0, x=0, j;
    printf("\n\n\t*****************Matriz*****************\n\n|\t->\t|  q0\n");
    for(i=0; i<=total; i++)
    {
        if(estado==0 && numeros[i]=='0')
            estado=1;
        else if(estado==1 && numeros[i]=='1')
            estado=2;
        else if(estado==1 && numeros[i]=='0')
            {estado=1; x++;}
        else if(estado==2 && numeros[i]=='1')
            {estado=0; x++;}
        else if(estado==2 && numeros[i]=='0')
            {estado=1; x++;}

        if(numeros[i]!='\0')
            printf("|\t%c\t|  q0", numeros[i]);
        if(numeros[i]=='1' && estado==0)
            {
                for(j=0; j<x; j++)
                printf("  X");
            }
        if(estado!=0 && numeros[i]!='\0')
            {
                for(j=0; j<x; j++)
                printf("  X");
                printf("  q%d\n", estado);
            }
        else
            printf("\n");

    }
	return;
}

void printing(char numeros[],int opcion)
{
	if (opcion == 2){		
		printf("Revise el archivo SalidaFin01Automatico.txt para ver resultados\n");
		freopen("SalidaFin01Automatico.txt", "w+",stdout);
   		checkin(numeros);
    		fclose(stdout);
	} else{
		printf("Revise el archivo SalidaFin01Manual.txt para ver resultados\n");
    		freopen("SalidaFin01Manual.txt", "w+",stdout);
		checkin(numeros);
		fclose(stdout);
	}
}

int main()
{
    char numero[10000];
    int random,seleccion,lim,random2;
    printf("\tSeleccione una opcion:\n[1] Manual\n[2] Automatico\n[3] Salir\n");
    scanf("%i",&seleccion);
    if (seleccion == 1){
        printf("Ingrese un numero binario:");
            scanf("%s", numero);
            if(revision(numero)==TRUE)
                printing(numero,seleccion);
            else
            {
                printf("Caracter no identificado, saliendo...\n\n");
            }


    } else if (seleccion == 2){
            time_t t;
            srand((unsigned)time(&t));	
            random = rand()%10+1;
            for (int i = 0; i<random; i++){
			random2 = rand()%1000+1;
			if (random2%2==0){
				numero[i] = '0';			
			} else {
				numero[i] = '1';			
			}				
		}
            printing(numero,seleccion);


    } else if (seleccion == 3){
        printf("Saliendo...\n");
    }
    else{
         printf("Seleccione una opcion valida.\n\n");
        main();
    }
        
    return 0;
}




