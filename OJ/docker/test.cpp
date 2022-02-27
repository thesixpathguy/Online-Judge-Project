#include <iostream>
using namespace std;

#define lint long long

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        lint n;
        cin >> n;
        if (n % 2 == 0)
        {
            lint p = 2;
            for (lint i = 0; i < n / 2; i++)
            {
                cout << p << " " << p - 1 << " ";
                p = p + 2;
            }
            cout << endl;
        }
        else
        {
            lint arr[n];
            lint p = 2;
            lint c = 0;
            for (lint i = 0; i < n / 2; i++)
            {
                arr[c] = p;
                arr[c + 1] = p - 1;
                c = c + 2;
                p = p + 2;
            }
            arr[n - 1] = n;
            swap(arr[n - 1], arr[n - 2]);
            for (lint i = 0; i < n; i++)
                cout << arr[i] << " ";
            cout << endl;
        }
    }
    return 0;
}
