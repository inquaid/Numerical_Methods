#include <bits/stdc++.h>
using namespace std;

double func(double x)
{
    // x^2 - 4x - 10
    return (x * x) - (4 * x) - 10;
}

int main()
{
    cout << fixed << setprecision(5);
    double x1 = 4, x2 = 2;

    // int i = 0;

    while (abs(x2 - x1) >= 0.005)
    {
        cout << x2 << "\n";
        double x3 = x2 - ((func(x2) * (x2 - x1)) / (func(x2) - func(x1)));
        x1 = x2;
        x2 = x3;

        // i++;
    }
}