#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>

typedef long long ll;

using namespace std;

int main()
{
  ll n, m, h, k;
  cin >> n >> m >> h >> k;
  string s;
  cin >> s;

  set<pair<ll, ll>> xyset;

  for (ll i = 0; i < m; i++)
  {
    ll x, y;
    cin >> x >> y;
    xyset.insert({x, y});
  }

  ll posx = 0, posy = 0;
  ll energy = h;

  for (ll i = 0; i < n; i++)
  {
    if (s[i] == 'R')
      posx++;
    else if (s[i] == 'L')
      posx--;
    else if (s[i] == 'U')
      posy++;
    else if (s[i] == 'D')
      posy--;

    energy--;

    if (energy < 0)
    {
      cout << "No" << endl;
      return 0;
    }

    if (energy < k && xyset.count({posx, posy}) > 0)
    {
      energy = k;
      xyset.erase({posx, posy});
    }
  }

  cout << "Yes" << endl;

  return 0;
}
