#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll n, q;
  cin >> n >> q;
  vector<ll> a(n);
  vector<ll> asum(n + 1, 0);

  for (ll i = 0; i < n; i++)
  {
    cin >> a[i];
    asum[i + 1] = asum[i] + a[i];
  }

  for (ll i = 0; i < q; i++)
  {
    ll l, r;
    cin >> l >> r;

    cout << asum[r] - asum[l - 1] << endl;
  }

  return 0;
}
