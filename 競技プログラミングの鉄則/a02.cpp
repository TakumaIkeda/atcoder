#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll n, x;
  cin >> n >> x;

  vector<ll> a(n);

  bool flg = false;

  for (ll i = 0; i < n; i++)
  {
    cin >> a[i];
    if (a[i] == x)
    {
      flg = true;
    }
  }

  cout << (flg ? "Yes" : "No") << endl;

  return 0;
}
