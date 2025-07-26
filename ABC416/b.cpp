#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  string s;
  cin >> s;

  bool flg = true;

  for (ll i = 0; i < s.size(); i++)
  {
    if (s[i] == '.' && flg)
    {
      s[i] = 'o';
      flg = false;
    }

    if (s[i] == '#')
    {
      flg = true;
    }
  }

  cout << s << endl;

  return 0;
}
