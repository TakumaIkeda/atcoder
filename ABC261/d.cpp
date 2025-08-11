#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll n, m;
  cin >> n >> m;
  vector<ll> x(n + 10);

  for (ll i = 1; i <= n; i++)
  {
    cin >> x[i];
  }

  vector<ll> y(n + 10, 0);

  for (ll i = 0; i < m; i++)
  {
    ll c, y_tmp;
    cin >> c >> y_tmp;
    y[c] = y_tmp;
  }

  vector<vector<ll>> dp(n + 10, vector<ll>(n + 10, 0));
  dp[0][0] = 0;

  for (ll i = 1; i <= n; i++)
  {
    for (ll j = 1; j <= i; j++)
    {
      dp[i][j] = dp[i - 1][j - 1] + x[i] + y[j];
    }

    dp[i][0] = 0;
    for (ll j = 0; j < i; j++)
    {
      dp[i][0] = max(dp[i][0], dp[i - 1][j]);
    }
  }

  ll ans = 0;
  for (ll j = 0; j <= n; j++)
  {
    ans = max(ans, dp[n][j]);
  }

  cout << ans << endl;

  return 0;
}
