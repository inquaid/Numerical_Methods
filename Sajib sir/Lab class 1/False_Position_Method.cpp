#include <bits/stdc++.h>
using namespace std;

double f(double x)
{
    //  f(x) = x^2 - 4x - 10
    return ((x * x) - x - 2);
}

int main()
{
    cout << "\nEnter x1 and x2: ";
    double a, b;
    cin >> a >> b;
    cout << "\nn: ";
    int n, i = 0;
    cin >> n;
    while (true)
    {
        double x1 = a, x2 = b;
        double f1 = f(x1);
        double f2 = f(x2);

        double x0 = x1 - ((f1 * (x2 - x1)) / (f2 - f1));
        double f0 = f(x0);

        cout << x1 << " " << x2 << endl;
        if (abs(f0) < 0.005)
        {
            cout << "\n\t" << x0;
            return 0;
        }
        if ((f0 * f1) < 0)
        {
            b = x0;
        }
        else
        {
            a = x0;
        }
        i++;
        if (i >= n)
            return 0;
    }
}