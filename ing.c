#include <stdlib.h>
#include <stdio.h>
#include <string.h>


void lecturaArchivo(void);
void manual (void);
void impresion(char*,int);
char* guardado(char*,char*,int,int);

int main (void){

	char sel;

	printf("[1]Lectura de archivo\n[2]Ingreso manual\n[3]Salir\nOpción:");
	scanf("%c", &sel);

	switch(sel)
		{
			case '1':
				lecturaArchivo();
				break;
			case '2':
				manual();
				break;
			case '3':
					break;
		}
	return 0;
}

void lecturaArchivo(){

	int estado = 0;
	int pos, j = 1;

	FILE* salida;
	FILE* archivo;

	char caracteres[100];
	char *ap = &caracteres[0];

	
	salida = fopen("SalidaIng.txt","w+");
	archivo = fopen("Archivo.txt","rt");

	int n = 10000000;
	printf("%i\n", n);

	fgets(caracteres,n,archivo);

	do{
		for (; *ap!='\0';ap++)
			{
		    	if(*ap=='i' && estado == 0){
		    			pos++;
			    		fprintf(salida,"Estado:%i\nLetra: %c\n\n",estado,*ap);
			    		impresion(ap, estado);
			    		estado = 1;
		    	}else{
		    		if(*ap=='n' && estado == 1){
		    			pos++;
			    		fprintf(salida,"Estado:%i\nLetra: %c\n\n",estado,*ap);
			    		impresion(ap, estado);
			    		estado = 2;

		    		}else{
		    			if(*ap=='g' && estado == 2 && *ap+1 == ' '){
		    				pos++; 
		    				fprintf(salida,"Estado:%i\nLetra: %c\n\n",estado,*ap);
		    				impresion(ap, estado);
		    				
		    			}else{
		    					if(*ap == ' '){
		    						pos++;
		    						fprintf(salida,"Estado:%i\nLetra: %c\n\n",estado,*ap);
		    						impresion(ap, estado);
		    						estado = 0;
		    					} else{
		    						pos++;
		    						fprintf(salida,"Estado:%i\nLetra: %c\n\n",estado,*ap);
				    				impresion(ap, estado);
				    				estado = 0;
		    					}
		    				
		    		
		    			}

		    		}
		    	}

			}

	}while(*ap != '\0');
	
	

	
	fclose(archivo);
	fclose(salida);
		
}

void manual(){

	char texto[10000]={};
	char palabras[10000];
	char *ap = &texto[0];
	char *pal = &palabras[0];
	char palabrasGuardadas[10000];
	int estado = 0;
	int pos = 0;
	int posiciones[10000];
	FILE* salida;

	salida = fopen("SalidaIng.txt","w+");
	printf("Ingrese el texto en el que se buscara la terminación ing: ");
	getchar();
    scanf("%[^\n]",texto); pal = ap;

    for (; *ap!='\0';ap++)
		{
	    	if(*ap=='i' && estado == 0){
	    			pos++;
		    		fprintf(salida,"Estado:%i\nLetra: %c\n\n",estado,*ap);
		    		impresion(ap, estado);
		    		estado = 1;
	    	}else{
	    		if(*ap=='n' && estado == 1){
	    			pos++;
		    		fprintf(salida,"Estado:%i\nLetra: %c\n\n",estado,*ap);
		    		impresion(ap, estado);
		    		estado = 2;

	    		}else{
	    			if(*ap=='g' && estado == 2 && *ap+1 == ' '){
	    				pos++; 
	    				fprintf(salida,"Estado:%i\nLetra: %c\n\n",estado,*ap);
	    				impresion(ap, estado);
	    				
	    			}else{
	    					if(*ap == ' '){
	    						pos++;
	    						posiciones[pos] = pos;
	    						fprintf(salida,"Estado:%i\nLetra: %c\n\n",estado,*ap);
	    						impresion(ap, estado);
	    						estado = 0;
	    					} else{
	    						pos++;
	    						fprintf(salida,"Estado:%i\nLetra: %c\n\n",estado,*ap);
			    				impresion(ap, estado);
			    				estado = 0;
	    					}
	    				
	    		
	    			}

	    		}
	    	}


		}
/*
	for(int i = 0; i<pos; i++){
		if(posiciones[i]!=0){
			printf("%i\n", posiciones[i]);
		}
			
	}	  
	for(;*pal!='\0';pal++){
		fprintf(salida, "%c\n", *pal);
	}
*/
	fclose(salida);
}

void impresion(char* ap, int estado){
	printf("Estado:%i\nLetra: %c\n\n",estado,*ap);

}
