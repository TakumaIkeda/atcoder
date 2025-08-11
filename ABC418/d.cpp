#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll n;
  cin >> n;
  string t;
  cin >> t;

  vector<vector<ll>> dp(n + 1, vector<ll>(2, 0)); // dp[i][0]は0の数が偶数の部分文字列の数、dp[i][1]は0の数が奇数の部分文字列の数

  for (ll i = 1; i <= n; i++)
  {
    if (t[i - 1] == '0')
    {
      dp[i][0] = dp[i - 1][1];
      dp[i][1] = dp[i - 1][0] + 1;
    }
    else
    {
      dp[i][0] = dp[i - 1][0] + 1;
      dp[i][1] = dp[i - 1][1];
    }
  }

  ll ans = 0;

  for (ll i = 0; i < n + 1; i++)
  {
    ans += dp[i][0];
  }

  cout << ans << endl;

  return 0;
}
