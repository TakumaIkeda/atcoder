#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

int main()
{
  string s1, s2;
  cin >> s1;
  cin >> s2;

  bool flg = true;

  if (s1[0] == '#')
  {
    if (s1[1] != '#' && s2[0] != '#')
    {
      flg = false;
    }
  }

  if (s1[1] == '#')
  {
    if (s1[0] != '#' && s2[1] != '#')
    {
      flg = false;
    }
  }

  if (s2[0] == '#')
  {
    if (s1[0] != '#' && s2[1] != '#')
    {
      flg = false;
    }
  }

  if (s2[1] == '#')
  {
    if (s1[1] != '#' && s2[0] != '#')
    {
      flg = false;
    }
  }

  cout << (flg ? "Yes" : "No") << endl;

  return 0;
}
