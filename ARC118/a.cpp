#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

int main()
{
  int t, n;
  cin >> t >> n;

  ll b = 0;
  ll tmp = 0;
  vector<ll> memo;
  for (ll a = 1; a <= 100; a++)
  {
    tmp = b;
    b = (100 + t) * a / 100;
    if (a == 1)
    {
      continue;
    }

    if (b - tmp > 1)
    {
      for (ll i = tmp + 1; i < b; i++)
      {
        memo.push_back(i);
      }
    }
  }

  ll num = n / memo.size();
  ll mod = n % memo.size();

  // for (ll i = 0; i < memo.size(); i++)
  // {
  //   cout << memo[i] << endl;
  // }

  if (mod == 0)
  {
    cout << (100 + t) * (num - 1) + memo[memo.size() - 1] << endl;
    return 0;
  }
  cout << (100 + t) * num + memo[mod - 1] << endl;

  return 0;
}
