#include <bits/stdc++.h>
using namespace std;

double f1(double x2, double x3)
{
    return (5 - x2 - x3) / 2.0;
}

double f2(double x1, double x3)
{
    return (15 - (3 * x1) - (2 * x3)) / 5.0;
}

double f3(double x1, double x2)
{
    return (8 - x2 - (2 * x1)) / 4.0;
}

int main()
{
    cout << fixed << setprecision(5);

    double x1 = 0, x2 = 0, x3 = 0;
    // cout << f1(0, 0);
    // return 0;

    int i = 0;
    while (i < 10)
    {
        cout << x1 << ", " << x2 << ", " << x3 << endl;
        x1 = f1(x2, x3);
        x2 = f2(x1, x3);
        x3 = f3(x1, x2);
        i++;
    }
}

