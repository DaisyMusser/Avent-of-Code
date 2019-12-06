#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

// determines longest line of file
// adapted from: https://github.com/imhoffman/advent/blob/master/2019/01/one.c
void file_reader ( FILE*fp, int*input ) {
    char temp[12];
    
    fgets(temp, 6, fp) != NULL 
    
    return;
}


// main function
int main ( void ) {
    //adapted from: https://github.com/imhoffman/advent/blob/master/2019/01/one.c
    FILE* fp;
    int input[2];
    char file_name[10] = "input.txt";           // change here for different file names
    
    fp = fopen( file_name, "r" );
    file_reader( fp, &input );
    fclose( fp );                               // done with file...only read the file once

    printf( "%d\n\n\n", input[0] );

    return 0;
}
