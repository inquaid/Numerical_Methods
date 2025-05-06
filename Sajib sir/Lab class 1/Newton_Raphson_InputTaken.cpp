#include <bits/stdc++.h>
using namespace std;

// f1
double func(double x)
{
    // x^2 - 3x + 2
    double a = 1, b = -3, c = 2;
    return (a * x * x) + (b * x) + c;
}

// f`1
double ddx_func(double x)
{
    // 2x - 3
    double a = 0, b = 2, c = -3;
    return (a * x) + (b * x) + c;
    // return ((2 * x) - 3);
}

int main()
{
    cout << fixed << setprecision(5);
    int i = 0;
    double x1 = 0;
    // cout<<ddx_func(x1);
    // return 0;
    while (i < 10)
    {

        cout << x1 << "\n";
        double x2 = x1 - (func(x1) / ddx_func(x1));

        x1 = x2;

        i++;
    }
}