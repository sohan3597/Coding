#include <stdio.h>

int main() {
    int a, b;
    char operator;

    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    printf("You entered: %d and %d\n", a, b);

    printf("Enter an operation (+, -, *, /): ");
    scanf(" %c", &operator);

    if (operator == '+') {
        printf("Result: %d\n", a + b);
    } else if (operator == '-') {
        printf("Result: %d\n", a - b);
    } else if (operator == '*') {
        printf("Result: %d\n", a * b);
    } else if (operator == '/') {
        if (b != 0) {
            printf("Result: %d\n", a / b);
        } else {
            printf("Error: Division by zero is not allowed.\n");
        }
    } else {
        printf("Error: Invalid operator.\n");
    }

    return 0;
}