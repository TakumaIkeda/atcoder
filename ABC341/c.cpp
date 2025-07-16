#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
  long long h, w, n;
  string t;

  cin >> h >> w >> n;
  cin >> t;

  vector<string> s(h);

  for (int i = 0; i < h; i++)
  {
    cin >> s[i];
  }

  int ans = 0;

  // 行数
  for (int i = 0; i < h; i++)
  {
    // 列数
    for (int j = 0; j < w; j++)
    {
      if (s[i][j] == '#')
      {
        continue;
      }

      bool is_ans = true;
      int dest[2] = {i, j};
      // tの長さ
      for (int k = 0; k < n; k++)
      {
        if (t[k] == 'L')
        {
          dest[1]--;
        }

        if (t[k] == 'R')
        {
          dest[1]++;
        }

        if (t[k] == 'U')
        {
          dest[0]--;
        }

        if (t[k] == 'D')
        {
          dest[0]++;
        }

        if (dest[0] < 0 || dest[1] < 0 || dest[0] >= h || dest[1] >= w)
        {
          is_ans = false;
          break;
        }

        if (s[dest[0]][dest[1]] == '#')
        {
          is_ans = false;
          break;
        }
      }

      if (is_ans)
      {
        ans++;
      }
    }
  }

  cout << ans << endl;

  return 0;
}
