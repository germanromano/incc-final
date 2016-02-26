## TP Final - Intro. a la Neurociencia

* Instalar [NLTK](http://www.nltk.org/install.html)
* Descargar fuentes de [Stanford POS Tagger](http://nlp.stanford.edu/software/stanford-postagger-full-2015-04-20.zip) y descomprimir dentro de la carpeta de este repositorio

**Fuente de libros:** [Project Gutenberg](https://www.gutenberg.org/browse/scores/top)

### Partes en las que se divide el trabajo:

## Separación de libros en sets de desarrollo y verificación

## Preprocesamiento de los datos
En este caso, el principial preprocesamiento que se hizo, fue leer las primeras líneas de cada libro para obtener el nombre del autor y extraer de él su género. Para saber si un nombre es de hombre o de mujer, se repasaron listas conseguidas en **cita**, y se descartaron tanto los que no pertenecían a ninguno de las dos listas como los que pertenecían a ambas. Luego se iteró sobre los resultados, quitando algunos nombres que figuraban en ambas listas pero eran ampliamente mayoritarios de un género. 

## Extracción de features
Lista de features extraídos:
1. Frecuencias de letras
2. Cantidad de palabras por clasificación sintáctica
3. Proporción de pronombres femeninos sobre femeninos
4. Proporción de vocales
5. Promedio de letras por palabra
6. Promedio de palabras por oración
7. Cantidad promedio de preguntas
8. Cantidad promedio de exclamaciones

## 
