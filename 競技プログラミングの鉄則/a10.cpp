#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

int main()
{
  ll n;
  cin >> n;

  vector<ll> a(n + 10);
  vector<ll> lmax(n + 10);
  vector<ll> rmax(n + 10);
  for (ll i = 1; i <= n; i++)
  {
    cin >> a[i];
  }

  lmax[1] = a[1];
  for (ll i = 2; i <= n; i++)
  {
    lmax[i] = max(lmax[i - 1], a[i]);
  }

  rmax[n] = a[n];
  for (ll i = n - 1; i >= 1; i--)
  {
    rmax[i] = max(rmax[i + 1], a[i]);
  }

  ll d;
  cin >> d;
  for (ll i = 0; i < d; i++)
  {
    ll l, r;
    cin >> l >> r;
    cout << max(lmax[l - 1], rmax[r + 1]) << endl;
  }

  return 0;
}
