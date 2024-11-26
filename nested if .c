#include <stdio.h>

int main() {
    int number;

    // Ask user for input
    printf("Enter a number: ");
    scanf("%d", &number);

    // Outer if statement: Check if the number is positive
    if (number > 0) {
        printf("The number is positive.\n");

        // Nested if statement: Check if the number is even or odd
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
            printf("
