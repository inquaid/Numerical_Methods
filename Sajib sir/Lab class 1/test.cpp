#include <bits/stdc++.h>
using namespace std;

class test {
  public:
    char symbol = '+';
    int num = 0;
    pair<int, int> x = {-1, 1};
    pair<int, int> y = {-1, 1}; // first = value, second = power

    test(string eqn) {
        // +12x2
        int index = 0, len = eqn.size();
        if (eqn[0] == '-') {
            this->symbol = '-';
            index++;
        }
        if (eqn[0] == '+') {
            index++;
        }
        string numTemp = "";
        while (index < len and isdigit(eqn[index])) {
            numTemp += eqn[index];
            index++;
        }
        if (numTemp.empty() == false) {
            this->num = stoi(numTemp);
        }

        while (index < len and (eqn[index] == 'x' or eqn[index] == 'y')) {
            if (eqn[index] == 'x') {
                index++;
                string powerTemp = "";
                while (index < len and isdigit(eqn[index])) {
                    powerTemp += eqn[index];
                    index++;
                }
                this->x.first = 1;
                this->x.second = stoi(powerTemp);
            } else {
                index++;
                string powerTemp = "";
                while (index < len and isdigit(eqn[index])) {
                    powerTemp += eqn[index];
                    index++;
                }
                this->y.first = 1;
                this->y.second = stoi(powerTemp);
            }
        }
    }
    int calculate(int x, int y) {
        this->x.first = x;
        this->y.first = y;
        int val = num * pow(this->x.first, this->x.second) *
                  pow(this->y.first, this->y.second);
        if (this->symbol == '-')
            return -val;
        return val;
    }
};

int main() {
    test t1("-2112x2y4");
    cout << t1.calculate(2, 3);
}