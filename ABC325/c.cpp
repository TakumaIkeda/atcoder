#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main()
{
  int H, W;
  cin >> H >> W;

  vector<string> S(H);
  for (int i = 0; i < H; ++i)
  {
    cin >> S[i];
  }

  int sensor_count = 0;

  for (int i = 0; i < H; i++)
  {
    for (int j = 0; j < W; j++)
    {
      queue<pair<int, int>> q;

      if (S[i][j] == '#')
      {
        sensor_count++;
        q.push(make_pair(i, j));
        S[i][j] = '.';

        while (!q.empty())
        {
          pair<int, int> p = q.front();
          q.pop();

          if (p.first > 0 && S[p.first - 1][p.second] == '#')
          {
            q.push(make_pair(p.first - 1, p.second));
            S[p.first - 1][p.second] = '.';
          }
          if (p.first < H - 1 && S[p.first + 1][p.second] == '#')
          {
            q.push(make_pair(p.first + 1, p.second));
            S[p.first + 1][p.second] = '.';
          }
          if (p.second > 0 && S[p.first][p.second - 1] == '#')
          {
            q.push(make_pair(p.first, p.second - 1));
            S[p.first][p.second - 1] = '.';
          }
          if (p.second < W - 1 && S[p.first][p.second + 1] == '#')
          {
            q.push(make_pair(p.first, p.second + 1));
            S[p.first][p.second + 1] = '.';
          }
          if (p.first > 0 && p.second > 0 && S[p.first - 1][p.second - 1] == '#')
          {
            q.push(make_pair(p.first - 1, p.second - 1));
            S[p.first - 1][p.second - 1] = '.';
          }
          if (p.first > 0 && p.second < W - 1 && S[p.first - 1][p.second + 1] == '#')
          {
            q.push(make_pair(p.first - 1, p.second + 1));
            S[p.first - 1][p.second + 1] = '.';
          }
          if (p.first < H - 1 && p.second > 0 && S[p.first + 1][p.second - 1] == '#')
          {
            q.push(make_pair(p.first + 1, p.second - 1));
            S[p.first + 1][p.second - 1] = '.';
          }
          if (p.first < H - 1 && p.second < W - 1 && S[p.first + 1][p.second + 1] == '#')
          {
            q.push(make_pair(p.first + 1, p.second + 1));
            S[p.first + 1][p.second + 1] = '.';
          }
        }
      }
    }
  }

  cout << sensor_count << endl;

  return 0;
}