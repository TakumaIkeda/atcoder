#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  string s;

  cin >> s;

  int out_count = 0;
  int idx = 0;

  for (int i = 0; i < s.size(); i++)
  {
    if (s[i] == '#' && out_count == 0)
    {
      out_count++;
      idx = i + 1;
      continue;
    }

    if (s[i] == '#' && out_count == 1)
    {
      out_count = 0;
      cout << idx << "," << i + 1 << endl;
    }
  }

  return 0;
}
