#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll d, n;
  cin >> d >> n;

  vector<ll> l(n);
  vector<ll> r(n);
  vector<ll> a(d + 2);
  vector<ll> asum(d + 1);
  for (ll i = 0; i < n; i++)
  {
    cin >> l[i] >> r[i];

    a[l[i]]++;
    a[r[i] + 1]--;
  }

  for (ll i = 1; i <= d; i++)
  {
    asum[i] = asum[i - 1] + a[i];

    cout << asum[i] << endl;
  }

  return 0;
}
