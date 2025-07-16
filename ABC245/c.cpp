#include <stdio.h>
#include <iostream>
#include <math.h>
#include <queue>
#include <vector>

using namespace std;

int main()
{
  long long n, k;

  cin >> n >> k;

  vector<long long> a(n);
  vector<long long> b(n);

  for (int i = 0; i < n; i++)
  {
    cin >> a[i];
  }

  for (int i = 0; i < n; i++)
  {
    cin >> b[i];
  }

  vector<bool> dp(n, false);
  vector<bool> ep(n, false);

  dp[0] = true;
  ep[0] = true;

  for (int i = 1; i < n; i++)
  {
    if (dp[i - 1] && abs(a[i] - a[i - 1]) <= k)
    {
      dp[i] = true;
    }

    if (ep[i - 1] && abs(a[i] - b[i - 1]) <= k)
    {
      dp[i] = true;
    }

    if (ep[i - 1] && abs(b[i] - b[i - 1]) <= k)
    {
      ep[i] = true;
    }

    if (dp[i - 1] && abs(b[i] - a[i - 1]) <= k)
    {
      ep[i] = true;
    }
  }

  if (dp[n - 1] || ep[n - 1])
  {
    cout << "Yes" << endl;
  }
  else
  {
    cout << "No" << endl;
  }

  return 0;
}
