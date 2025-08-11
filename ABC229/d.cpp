#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

int main()
{
  string s;
  ll k;

  cin >> s;
  cin >> k;

  vector<ll> dotcnt(s.size() + 1, 0);

  for (ll i = 0; i < s.size(); i++)
  {
    dotcnt[i + 1] = dotcnt[i] + (s[i] == '.' ? 1 : 0);
  }

  ll ans = 0;
  ll right = 0;

  for (ll left = 0; left <= s.size(); left++)
  {
    if (right < left)
    {
      right = left;
    }

    while (right <= s.size())
    {
      ll numdot = dotcnt[right] - dotcnt[left];
      if (numdot > k)
      {
        break;
      }

      if (numdot <= k)
      {
        ans = max(ans, right - left);
      }

      // cout << "left: " << left << ", right: " << right << ", numdot: " << numdot << ", ans: " << ans << endl;

      right++;
    }
  }

  cout << ans << endl;

  return 0;
}
