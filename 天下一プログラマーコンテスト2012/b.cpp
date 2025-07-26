#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  string s;

  getline(cin, s);

  bool flag = true;
  for (ll i = 0; i < s.size(); i++)
  {
    if (s[i] != ' ')
    {
      flag = true;
      cout << s[i];
      continue;
    }

    if (flag)
    {
      cout << ",";
      flag = false;
    }
  }

  cout << endl;

  return 0;
}
