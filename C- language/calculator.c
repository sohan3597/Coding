#include <stdio.h>

int main(void) {
    char choice;

    do {
        double a,b;
        char operator;

        printf("Enter first number: ");
        scanf("%lf", &a);
        printf("enter 2nd number: ");
        scanf("%lf", &b);

        printf("Enter operator (+, -, *, /): ");
        scanf(" %c", &operator);

        if (operator == '+') {
            printf("%.2lf + %.2lf = %.2lf\n", a, b, a + b);
        } else if (operator == '-') {
            printf("%.2lf - %.2lf = %.2lf\n", a, b, a - b);
        } else if (operator == '*') {
            printf("%.2lf * %.2lf = %.2lf\n", a, b, a * b);
        } else if (operator == '/') {
            if (b != 0) {
                printf("%.2lf / %.2lf = %.2lf\n", a, b, a / b);
            } else {
                printf("Error: Division by zero is not allowed.\n");
            }
        } else {
            printf("Error: Invalid operator.\n");
        }
        
        printf("Do you want to perform another calculation? (y/n): ");
        scanf(" %c", &choice);
    } while (choice == 'y' || choice == 'Y');



return 0;
}