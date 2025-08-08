#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll x, k, d;
  cin >> x >> k >> d;

  ll abs_x = abs(x);
  ll n = abs_x / d;
  ll res = k - n;

  if (k <= n)
  {
    cout << (abs_x - d * k) << endl;
    return 0;
  }

  if (res % 2 == 0)
  {
    cout << abs_x % d << endl;
    return 0;
  }

  cout << (d - (abs_x % d)) << endl;

  return 0;
}
