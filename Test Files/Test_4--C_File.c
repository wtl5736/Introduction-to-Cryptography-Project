// 
// File: mmult-driver.c
// compilation: gcc -ggdb -Wall -Wextra -pedantic -std=c99 mmult.c -c
// compilation: gcc -ggdb -Wall -Wextra -pedantic -std=c99 mmult-driver.c -c
// compilation: gcc -ggdb -Wall -Wextra -pedantic -std=c99 mmult.o mmult-driver.o -o mmult
// date: Tues Oct 18 10:57:18 PM EDT 2016
// @author Wesley Lee, wtl5736@cs.rit.edu
// 
// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mmult.h"

int main(int argc, char* argv[]){
	(void) argc;
	FILE* fp = fopen(argv[0], "r");	
	char *firstLine = NULL;
	char *ptr;
	if (!fp){
		fprintf(stdout, "Can't Open File");
		return EXIT_FAILURE;
	} else{ // Gets the number of matrices
		char *buf = NULL;
		size_t len = 100;
		while (getline(&buf, &len, stdin)){
			char *pch;
			pch = strtok(buf, " \n");
			firstLine = buf;
			(void) pch;
			break;
		}
	}
	
	int numOfMatrices = strtod(firstLine, &ptr);
	free(firstLine);
	
	// Gets the number of rows and columns of the matrix
	for (int m = 0; m < numOfMatrices; m++){
		int x, y, i, j, w, z;	// Rows and Cols for the Matrices
		Matrices MatA;	// First Matrix
		Matrices MatB;	// Second Matrix
		Matrices MatC;	// Product of MatA and MatB
		Matrices MatD;
		Matrices MatTemp;
		if (numOfMatrices == 1){	// One Matrix
			MatA.matrix = mread(stdin, &x, &y);
			MatA.row = x;
			MatA.col = y;
			printf("%d %d\n", MatA.row, MatA.col);
			mwrite(stdout, MatA.row, MatA.col, MatA.matrix);
			xfree(MatA.row, MatA.col, MatA.matrix);
		} else if (numOfMatrices >= 2){		// Two Matrices
			if (numOfMatrices == 2){
				if (m == 0){
					MatA.matrix = mread(stdin, &x, &y);
					MatA.row = x;
					MatA.col = y;
					
					MatB.matrix = mread(stdin, &i, &j);
					MatB.row = i;
					MatB.col = j;
					
					MatC.matrix = mmult(MatA.row, MatA.col, MatA.matrix, MatB.row, MatB.col, MatB.matrix);
					MatC.row = MatA.row;
					MatC.col = MatB.col;

					xfree(MatA.row, MatA.col, MatA.matrix);
					xfree(MatB.row, MatB.col, MatB.matrix);
					printf("%d %d\n", MatC.row, MatC.col);
					mwrite(stdout, MatC.row, MatC.col, MatC.matrix);
					xfree(MatC.row, MatC.col, MatC.matrix);
				}
			 } else if (numOfMatrices > 2){		// More than two matrices
				if (m == 0){
					MatA.matrix = mread(stdin, &x, &y);
					MatA.row = x;
					MatA.col = y;
					
					MatB.matrix = mread(stdin, &i, &j);
					MatB.row = i;
					MatB.col = j;
					
					MatC.matrix = mmult(MatA.row, MatA.col, MatA.matrix, MatB.row, MatB.col, MatB.matrix);
					MatC.row = x;
					MatC.col = j;
					
					xfree(MatA.row, MatA.col, MatA.matrix);
					xfree(MatB.row, MatB.col, MatB.matrix);
					for (int x = 2; x < numOfMatrices; x++){
						MatD.matrix = mread(stdin, &w, &z);
						MatD.row = w;
						MatD.col = z;
						
						MatTemp.matrix = mmult(MatC.row, MatC.col, MatC.matrix, MatD.row, MatD.col, MatD.matrix);
						MatTemp.row = MatC.row;
						MatTemp.col = MatD.col;
						
						xfree(MatD.row, MatD.col, MatD.matrix);
						xfree(MatC.row, MatC.col, MatC.matrix);
						
						MatC.matrix = MatTemp.matrix;
						MatC.row = MatTemp.row;
						MatC.col = MatTemp.col;

						if (x == (numOfMatrices-1)){
							printf("%d %d\n", MatC.row, MatC.col);
							mwrite(stdout, MatC.row, MatC.col, MatC.matrix);
						}
					}	
					xfree(MatC.row, MatC.col, MatC.matrix);
				} 
			}
		}
	}
	fclose(fp);
}

