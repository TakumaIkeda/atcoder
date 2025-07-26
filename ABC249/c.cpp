#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>

typedef long long ll;

using namespace std;

int main()
{
  ll n, k;

  cin >> n >> k;

  vector<string> s(n);

  for (ll i = 0; i < n; i++)
  {
    cin >> s[i];
  }

  ll ans = 0;

  for (ll bit = 0; bit < (1 << n); bit++)
  {
    map<char, ll> cnt;
    for (ll i = 0; i < n; i++)
    {
      if (bit & (1 << i))
      {
        for (char c : s[i])
        {
          cnt[c]++;
        }
      }
    }

    // cntの値がkと一致している数をカウント
    ll current = 0;
    for (auto &p : cnt)
    {
      if (p.second == k)
      {
        current++;
      }
    }

    ans = max(ans, current);
  }

  cout << ans << endl;

  return 0;
}
