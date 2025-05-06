#include <bits/stdc++.h>
using namespace std;

double f(double x)
{
    //  f(x) = x^2 - 4x - 10
    return ((x * x) - (4 * x) - 10);
}

int main()

{
    cout << "Enter x1 and x2: ";
    double a, b;
    cin >> a >> b;
    cout << "\nn: ";
    int n;
    cin >> n;

    int i = 0;
    while (true)
    {
        double x1 = a, x2 = b;
        double x0 = ((x2 + x1) / 2);
        double f0 = f(x0);
        double f1 = f(x1);
        double f2 = f(x2);

        cout << x1 << " " << x2 << endl;
        if (abs(f0) == 0)
        {
            cout << "\n"
                 << x0 << endl;
            cout << "\ni: " << i + 1;
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