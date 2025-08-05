#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll h, w;

  cin >> h >> w;
  vector<vector<ll>> x(h + 10, vector<ll>(w + 10, 0));
  vector<vector<ll>> xsum(h + 10, vector<ll>(w + 10, 0));

  for (ll i = 1; i <= h; i++)
  {
    for (ll j = 1; j <= w; j++)
    {
      cin >> x[i][j];
    }
  }

  for (ll i = 1; i <= h; i++)
  {
    for (ll j = 1; j <= w; j++)
    {
      xsum[i][j] = x[i][j] + xsum[i][j - 1];
    }

    for (ll j = 1; j <= w; j++)
    {
      xsum[i][j] += xsum[i - 1][j];
    }
  }

  ll q;
  cin >> q;

  for (ll i = 0; i < q; i++)
  {
    ll a, b, c, d;
    cin >> a >> b >> c >> d;

    ll ans = xsum[c][d] - xsum[a - 1][d] - xsum[c][b - 1] + xsum[a - 1][b - 1];
    cout << ans << endl;
  }

  return 0;
}
