#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

int main()
{
  ll n, k;
  cin >> n >> k;

  vector<ll> a(n);
  vector<ll> b(n);
  vector<ll> c(n);
  vector<ll> d(n);

  for (ll i = 0; i < n; i++)
  {
    cin >> a[i];
  }

  for (ll i = 0; i < n; i++)
  {
    cin >> b[i];
  }

  for (ll i = 0; i < n; i++)
  {
    cin >> c[i];
  }

  for (ll i = 0; i < n; i++)
  {
    cin >> d[i];
  }

  vector<ll> ab(n * n);
  vector<ll> cd(n * n);

  for (ll i = 0; i < n; i++)
  {
    for (ll j = 0; j < n; j++)
    {
      ab[i * n + j] = a[i] + b[j];
      cd[i * n + j] = c[i] + d[j];
    }
  }

  sort(cd.begin(), cd.end());

  ll flg = false;
  for (ll i = 0; i < n * n; i++)
  {
    ll rest = k - ab[i];
    ll idx = lower_bound(cd.begin(), cd.end(), rest) - cd.begin();
    if (cd[idx] == rest)
    {
      flg = true;
      break;
    }
  }

  cout << (flg ? "Yes" : "No") << endl;

  return 0;
}
