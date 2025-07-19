#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

// bool judge(const vector<ll> &red, const vector<ll> &blue)
// {
//   bool flag = true;
//   for (int i = 1; i < 10; i++)
//   {
//     if (red[i] != 0 || blue[i] != 0)
//     {
//       flag = false;
//       break;
//     }
//   }
// }

int main()
{
  ll n, x, y;
  cin >> n >> x >> y;

  vector<ll> red(10);
  vector<ll> blue(10);

  red[n - 1] = 1;

  for (int i = n - 1; i > 0; i--)
  {
    red[i - 1] += red[i];
    blue[i] += red[i] * x;
    red[i] = 0;

    red[i - 1] += blue[i];
    blue[i - 1] += blue[i] * y;
  }

  cout << blue[0] << endl;

  return 0;
}
