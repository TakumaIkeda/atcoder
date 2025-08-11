#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

typedef long long ll;

using namespace std;

int main()
{
  ll l, q;
  cin >> l >> q;

  set<ll> check;
  check.insert(0);
  check.insert(l);

  for (ll i = 0; i < q; i++)
  {
    ll c, x;
    cin >> c >> x;

    if (c == 1)
    {
      check.insert(x);
    }
    else
    {
      auto it = check.upper_bound(x);
      cout << -(*prev(it) - *it) << endl;
    }
  }

  return 0;
}
