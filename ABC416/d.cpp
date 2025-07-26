#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

int main()
{
  ll t;
  cin >> t;

  for (ll i = 0; i < t; i++)
  {
    ll n, m;
    cin >> n >> m;
    vector<ll> a(n);
    vector<ll> b(n);
    ll a_sum = 0;
    ll b_sum = 0;

    for (ll i = 0; i < n; i++)
    {
      cin >> a[i];
      a_sum += a[i];
    }

    for (ll i = 0; i < n; i++)
    {
      cin >> b[i];
      b_sum += b[i];
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    ll k = 0;
    ll l = n - 1;
    ll pair_count = 0;

    while (k < n && l >= 0)
    {
      if (a[k] + b[l] >= m)
      {
        pair_count++;
        k++;
        l--;
      }
      else
      {
        k++;
      }
    }

    cout << a_sum + b_sum - pair_count * m << endl;
  }

  return 0;
}
