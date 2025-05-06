#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_TERMS 100

// Structure to hold a coefficient and its corresponding exponent (power)
typedef struct
{
    int coefficient;
    int exponent;
} Term;

// Function to extract the coefficient and exponent from a term like "3x^2" or "-x"
Term parse_term(const char *term_str)
{
    Term term;
    term.coefficient = 0;
    term.exponent = 0;

    int i = 0, sign = 1;

    // Check if the term starts with a + or - sign
    if (term_str[i] == '-')
    {
        sign = -1;
        i++;
    }
    else if (term_str[i] == '+')
    {
        i++;
    }

    // Extract the coefficient if present
    if (isdigit(term_str[i]))
    {
        term.coefficient = sign * atoi(&term_str[i]);
        while (isdigit(term_str[i]))
        {
            i++;
        }
    }
    else
    {
        // If no coefficient is provided, it is either 1 or -1
        term.coefficient = sign;
    }

    // Look for 'x'
    if (term_str[i] == 'x')
    {
        i++; // Move past 'x'
        if (term_str[i] == '^')
        {
            i++;                                // Move past '^'
            term.exponent = atoi(&term_str[i]); // Extract exponent
        }
        else
        {
            term.exponent = 1; // If no ^ is provided, exponent is 1
        }
    }
    else
    {
        term.exponent = 0; // If no 'x', it's a constant term
    }

    return term;
}

// Function to parse the entire equation and fill the coefficient array
void parse_equation(const char *equation, int *coefficients, int degree)
{
    char temp[100];
    int index = 0;
    int length = strlen(equation);

    for (int i = 0; i <= length; i++)
    {
        if (equation[i] == '+' || equation[i] == '-' || equation[i] == '\0')
        {
            if (index > 0)
            {
                temp[index] = '\0';           // End the current term string
                Term term = parse_term(temp); // Parse the term
                if (term.exponent <= degree)
                {
                    coefficients[term.exponent] += term.coefficient;
                }
            }
            // Start the new term
            temp[0] = equation[i];
            index = 1;
        }
        else
        {
            temp[index++] = equation[i]; // Continue building the term string
        }
    }
}

int main()
{
    int n; // Degree of the polynomial
    char equation[256];

    printf("Degree: ");
    scanf("%d", &n);
    getchar(); // Consume newline after entering degree

    printf("Equation: ");
    fgets(equation, sizeof(equation), stdin);
    equation[strcspn(equation, "\n")] = '\0'; // Remove newline from the input

    // Array to store coefficients of the terms (initialize to 0)
    int coefficients[MAX_TERMS] = {0};

    // Parse the equation to fill the coefficients array
    parse_equation(equation, coefficients, n);

    // Print coefficients for each term from highest to lowest degree
    for (int i = n; i >= 0; i--)
    {
        printf("Coefficient of x^%d: %d\n", i, coefficients[i]);
    }

    return 0;
}
