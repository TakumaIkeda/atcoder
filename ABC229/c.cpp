#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

int main()
{
  ll n, w;
  cin >> n >> w;

  vector<pair<ll, ll>> a(n);

  for (ll i = 0; i < n; i++)
  {
    cin >> a[i].first >> a[i].second;
  }

  sort(a.rbegin(), a.rend());

  ll ans = 0;

  for (ll i = 0; i < n; i++)
  {
    if (w <= 0)
      break;

    ans += a[i].first * min(a[i].second, w);
    w -= min(a[i].second, w);
  }

  cout << ans << endl;

  return 0;
}
