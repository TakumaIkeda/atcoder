#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;
const ll MOD = 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 + 7;

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

  ll b0 = 0; // aの転倒数
  for (ll i = 0; i < n; i++)
  {
    for (ll j = i + 1; j < n; j++)
    {
      if (a[i] > a[j])
      {
        b0++;
      }
    }
  }

  ll b = 0; // aを繰り返す場合の、b[i]の転倒数の和
  for (ll i = 0; i < n; i++)
  {
    for (ll j = 0; j < n; j++)
    {
      if (a[i] > a[j])
      {
        b++;
      }
    }
  }

  ll ans = 0;

  ans += b0 * k % MOD;
  if (k % 2 == 0)
  {
    ll mod1 = (k / 2) % MOD;
    ll mod2 = (k - 1) % MOD;
    ll mod3 = mod1 * mod2 % MOD;
    ll mod4 = b * mod3 % MOD;
    ans += mod4;
  }
  else
  {
    ll mod1 = k % MOD;
    ll mod2 = (k - 1) / 2 % MOD;
    ll mod3 = mod1 * mod2 % MOD;
    ll mod4 = b * mod3 % MOD;
    ans += mod4;
  }

  ans %= MOD;

  cout << ans << endl;

  return 0;
}
