#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int h, w;

  cin >> h >> w;

  vector<string> s(h);

  for (int i = 0; i < h; i++)
  {
    cin >> s[i];
  }

  bool ans = true;

  for (int i = 0; i < h; i++)
  {
    for (int j = 0; j < w; j++)
    {
      bool ok = false;
      if (s[i][j] == '#')
      {
        if (i != 0 && s[i - 1][j] == '#')
        {
          ok = true;
        }

        if (i != h - 1 && s[i + 1][j] == '#')
        {
          ok = true;
        }

        if (j != 0 && s[i][j - 1] == '#')
        {
          ok = true;
        }

        if (j != w - 1 && s[i][j + 1] == '#')
        {
          ok = true;
        }

        if (!ok)
        {
          ans = false;
          cout << "No" << endl;
          return 0;
        }
      }
    }
  }

  cout << "Yes" << endl;

  return 0;
}
