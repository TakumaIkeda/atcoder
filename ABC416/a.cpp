#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll n, l, r;
  cin >> n >> l >> r;
  string s;
  cin >> s;
  bool flg = true;

  for (ll i = l - 1; i < r; i++)
  {
    if (s[i] == 'x')
    {
      flg = false;
      break;
    }
  }

  if (flg)
  {
    cout << "Yes" << endl;
  }
  else
  {
    cout << "No" << endl;
  }

  return 0;
}
