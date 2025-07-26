#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <map>

typedef long long ll;

using namespace std;

int main()
{
  string s;

  cin >> s;

  queue<pair<string, int>> q;
  map<string, bool> visited;

  q.push({s, 0});
  visited[s] = true;

  int ans = 0;

  while (!q.empty())
  {
    auto [current, steps] = q.front();
    q.pop();

    if (current == "atcoder")
    {
      ans = steps;
      break;
    }

    for (int i = 0; i < current.size() - 1; i++)
    {
      string next = current;
      swap(next[i], next[i + 1]);

      if (!visited[next])
      {
        visited[next] = true;
        q.push({next, steps + 1});
      }
    }
  }

  cout << ans << endl;

  return 0;
}
