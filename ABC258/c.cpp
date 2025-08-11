#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll n, q;
  cin >> n >> q;
  string s;
  cin >> s;
  ll head = 0;
  for (ll i = 0; i < q; i++)
  {
    ll t, x;
    cin >> t >> x;

    if (t == 1)
    {
      head = head - x;
      if (head < 0)
      {
        head += n;
      }
    }
    else
    {
      ll idx = (head + x - 1);
      if (idx >= n)
      {
        idx -= n;
      }
      cout << s[idx] << endl;
    }
  }

  return 0;
}
