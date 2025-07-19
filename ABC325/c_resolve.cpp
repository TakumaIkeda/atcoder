#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>

typedef long long ll;

using namespace std;

int main()
{
  ll h, w;
  cin >> h >> w;

  vector<string> s(h);

  for (ll i = 0; i < h; i++)
  {
    cin >> s[i];
  }

  queue<vector<ll>> q;
  ll ans = 0;

  for (ll i = 0; i < h; i++)
  {
    for (ll j = 0; j < w; j++)
    {
      if (s[i][j] == '#')
      {
        q.push({i, j});
        s[i][j] = '.';
        ans++;
      }

      while (!q.empty())
      {
        vector<ll> current = q.front();
        q.pop();

        if (current[0] != 0 && s[current[0] - 1][current[1]] == '#')
        {
          q.push({current[0] - 1, current[1]});
          s[current[0] - 1][current[1]] = '.';
        }

        if (current[0] != h - 1 && s[current[0] + 1][current[1]] == '#')
        {
          q.push({current[0] + 1, current[1]});
          s[current[0] + 1][current[1]] = '.';
        }

        if (current[1] != 0 && s[current[0]][current[1] - 1] == '#')
        {
          q.push({current[0], current[1] - 1});
          s[current[0]][current[1] - 1] = '.';
        }

        if (current[1] != w - 1 && s[current[0]][current[1] + 1] == '#')
        {
          q.push({current[0], current[1] + 1});
          s[current[0]][current[1] + 1] = '.';
        }

        if (current[0] != 0 && current[1] != 0 && s[current[0] - 1][current[1] - 1] == '#')
        {
          q.push({current[0] - 1, current[1] - 1});
          s[current[0] - 1][current[1] - 1] = '.';
        }

        if (current[0] != 0 && current[1] != w - 1 && s[current[0] - 1][current[1] + 1] == '#')
        {
          q.push({current[0] - 1, current[1] + 1});
          s[current[0] - 1][current[1] + 1] = '.';
        }

        if (current[0] != h - 1 && current[1] != 0 && s[current[0] + 1][current[1] - 1] == '#')
        {
          q.push({current[0] + 1, current[1] - 1});
          s[current[0] + 1][current[1] - 1] = '.';
        }

        if (current[0] != h - 1 && current[1] != w - 1 && s[current[0] + 1][current[1] + 1] == '#')
        {
          q.push({current[0] + 1, current[1] + 1});
          s[current[0] + 1][current[1] + 1] = '.';
        }
      }
    }
  }

  cout << ans << endl;

  return 0;
}
