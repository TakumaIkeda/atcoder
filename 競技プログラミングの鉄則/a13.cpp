#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll n, k;
  cin >> n >> k;
  vector<ll> a(n);
  for (ll i = 0; i < n; i++)
  {
    cin >> a[i];
  }

  ll right = 0;
  ll ans = 0;
  for (ll left = 0; left < n; left++)
  {
    ll tmp = right;
    while (right < n && a[right] - a[left] <= k)
    {
      right++;
    }
    ans += right - left - 1;
  }

  cout << ans << endl;

  return 0;
}
