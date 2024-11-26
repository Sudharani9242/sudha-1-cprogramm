#include <stdio.h>

int main() {
    int number;

    
    printf("Enter a number: ");
    scanf("%d", &number);

   
    if (number > 0) {
        printf("The number is positive.\n");

        
     
 if (number % 2 == 0) {
            printf("The number is even.\n");
        } else {
            printf("The number is odd.\n");
        }
    }
    // If number is not positive, check if it's negative
    else if (number < 0) {
        printf("The number is negative.\n");

        // Nested if statement: Check if the negative number is even or odd
        if (number % 2 == 0) {
            printf("The negative number is even.\n");
        } else {
            printf("The negative number is odd.\n");
        }
    }
    // If number is zero
    else {
        printf("The number is zero.\n");
    }

    return 0;
}
