#include <iostream>
#include <regex>
#include <string>
#include <map>
using namespace std;
int main()
{
    int n;
    cout << "Degree: ";
    cin >> n;
    cin.ignore(); // Ignore newline left by cin

    string equation;
    cout << "Equation: ";
    getline(cin, equation);

    map<int, int> coefficients;

    // Regular expression to match terms of the form ±ax^b or constants
    regex term_pattern(R"(([+-]?\d*)x\^?(\d*)|([+-]?\d+))");
    
    auto words_begin = sregex_iterator(equation.begin(), equation.end(), term_pattern);
    auto words_end = sregex_iterator();

    for (sregex_iterator i = words_begin; i != words_end; ++i)
    {
        smatch match = *i;

        if (match[1].matched)
        { // If there's a coefficient term
            string coefficient_str = match[1].str();
            string power_str = match[2].str().empty() ? "1" : match[2].str();

            // Convert the coefficient string to an integer
            int coefficient = coefficient_str == "+" || coefficient_str == "-" ? stoi(coefficient_str + "1") : (coefficient_str.empty() ? 1 : stoi(coefficient_str));

            // Convert the power string to an integer
            int power = stoi(power_str);

            coefficients[power] = coefficient;
        }
        else if (match[3].matched)
        { // If it's a constant term
            int constant = stoi(match[3].str());
            coefficients[0] = constant;
        }
    }

    // Output coefficients from highest to lowest degree
    for (int i = n; i >= 0; --i)
    {
        int coefficient = coefficients.count(i) ? coefficients[i] : 0;
        cout << "Coefficient of x^" << i << ": " << coefficient << endl;
    }

    return 0;
}
