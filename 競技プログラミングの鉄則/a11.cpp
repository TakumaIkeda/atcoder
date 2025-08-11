#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

int main()
{
  ll n, x;
  cin >> n >> x;
  vector<ll> a(n);
  for (ll i = 0; i < n; i++)
  {
    cin >> a[i];
  }

  sort(a.begin(), a.end());
  ll ans = lower_bound(a.begin(), a.end(), x) - a.begin();

  cout << ans + 1 << endl;

  return 0;
}
