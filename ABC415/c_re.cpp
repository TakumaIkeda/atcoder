#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>

typedef long long ll;

using namespace std;

int main()
{
  ll t;
  cin >> t;

  for (ll i = 0; i < t; i++)
  {
    ll n;
    string s;

    cin >> n;
    cin >> s;

    queue<ll> q;
    vector<bool> visited(1 << n, false);
    q.push(0);
    visited[0] = true;
    bool flag = false;

    if (s[s.size() - 1] == '1')
    {
      cout << "No" << endl;
      continue;
    }

    while (!q.empty())
    {
      ll current = q.front();
      q.pop();

      if (current == (1 << n) - 1)
      {
        cout << "Yes" << endl;
        flag = true;
        break;
      }

      for (ll j = 0; j < n; j++)
      {
        ll next = current | (1 << j);
        if (!visited[next] && s[next - 1] == '0')
        {
          visited[next] = true;
          q.push(next);
        }
      }
    }

    if (!flag)
    {
      cout << "No" << endl;
    }
  }

  return 0;
}