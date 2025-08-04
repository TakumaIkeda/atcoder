#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll n, k;
  cin >> n >> k;

  ll ans = 0;
  for (ll i = 1; i <= n; i++)
  {
    if (i > k - 2)
    {
      break;
    }

    for (ll j = 1; j <= n; j++)
    {
      if (j > k - 2)
      {
        break;
      }

      if (1 <= k - i - j && k - i - j <= n)
      {
        ans++;
      }

      // cout << "(" << i << ", " << j << " , " << (k - i - j) << ")" << endl;
    }
  }

  cout << ans << endl;

  return 0;
}
