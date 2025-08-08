#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll h, w, n;
  cin >> h >> w >> n;
  vector<vector<ll>> grid(h + 10, vector<ll>(w + 10, 0));
  vector<vector<ll>> gridsum(h + 10, vector<ll>(w + 10, 0));

  for (ll i = 0; i < n; i++)
  {
    ll a, b, c, d;
    cin >> a >> b >> c >> d;

    grid[a][b]++;
    grid[a][d + 1]--;
    grid[c + 1][b]--;
    grid[c + 1][d + 1]++;
  }

  for (ll i = 1; i < h + 10; i++)
  {
    for (ll j = 1; j < w + 10; j++)
    {
      gridsum[i][j] = grid[i][j] + gridsum[i][j - 1];
    }
  }

  for (ll i = 1; i < h + 10; i++)
  {
    for (ll j = 1; j < w + 10; j++)
    {
      gridsum[i][j] = grid[i][j] + gridsum[i][j - 1];
    }
  }

  for (ll i = 1; i < h + 10; i++)
  {
    for (ll j = 1; j < w + 10; j++)
    {
      gridsum[i][j] += gridsum[i - 1][j];
    }
  }

  for (ll i = 0; i < h; i++)
  {
    for (ll j = 0; j < w; j++)
    {
      cout << gridsum[i + 1][j + 1] << " ";
    }

    cout << endl;
  }

  return 0;
}
