#include <iostream>
#include <cmath>
#include <vector>

using namespace std;


void user_input(unsigned int n, vector<vector<double>> &a, vector<double> &answ){
    for (int i = 0; i < n; ++i) {
        a[i].resize(n);
        for (int j = 0; j < n; ++j) {
            cin >> a[i][j];
        }
        cin >> answ[i];
    }
}


vector<vector<double>> zeroed_matrix(unsigned int n) {
    vector<vector<double>> p(n);
    for (int i = 0; i < n; ++i) {
        p[i].resize(n);
        for (int j = 0; j < n; ++j) {
            p[i][j] = 0;
        }
    }
    return p;
}


void Cholesky_Decomposition(vector<vector<double>> p, unsigned int n, vector<vector<double>> &L, vector<vector<double>> &U) {
    long i, j, k; double val = 0, val2 = 0;

    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++) {
            val = 0; val2 = 0;
            if (i > j) {
                if (j > 0)
                    for (k = 1; k < j + 1; k++) val2 += (L[i][k - 1] * L[j][k - 1]);
                L[i][j] = (p[i][j] - val2) / L[j][j];
            }
            else if (i == j) {
                for (k = 0; k < i; k++) val += pow(L[i][k], 2);
                L[i][j] = sqrt(p[i][j] - val);
            }
            else
                L[i][j] = 0;
        }

    for (i = 0; i < n; i++) for (j = 0; j < n; j++) U[i][j] = L[j][i];
}



void output_matrix(vector<vector<double>> &a, long n) {
    for (long i = 0; i < n; i++) {
        for (long j = 0; j < n; j++)
            cout << a[i][j] << "\t";
        cout << "\n";
    }
    cout << "\n";
}


void result(vector<vector<double>> &U, vector<double> &answ, unsigned int n, vector<double> &x){
    vector<double> y(n);
    for (int i = 0; i < n; ++i) {
        double val = 0;
        for (int j = 0; j < i; ++j)
            val += U[j][i] * y[j];
        y[i] = (answ[i] - val) / U[i][i];
    }
    for (int k = n - 1; k >= 0; --k) {
        double val = 0;
        for (int i = k + 1; i < n; ++i)
            val += U[k][i] * x[i];
        x[k] = (y[k] - val) / U[k][k];
    }
}


int main() {
    unsigned int n;
    cout << "Enter amount of variables: ";
    cin >> n;
    vector<vector<double>> a(n);
    vector<double> answ(n);
    cout << "Enter matrix: \n";
    user_input(n, a, answ);

    vector<vector<double>> L = zeroed_matrix(n); vector<vector<double>> U = zeroed_matrix(n);
    Cholesky_Decomposition(a, n, L, U);
    vector<double> res(n);
    result(U, answ, n, res);

    cout << "\nRESULTS: \n";
    for (int i = 1; i < n + 1; ++i) cout << "x" << i << " = " << res[i] << "\n";
    cout << "\n";

    cout << "L matrix: \n";
    output_matrix(L, n);
    cout << "U matrix: \n";
    output_matrix(U, n);
}


//1.17 -0.65 1.54
//-0.65 1.16 -1.73
//1.54 -1.73 2.15