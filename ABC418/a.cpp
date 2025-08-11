#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll n;
  cin >> n;

  string s;
  cin >> s;

  ll l = s.size();

  if (l < 3)
  {
    cout << "No" << endl;
    return 0;
  }

  if (s[l - 3] == 't' && s[l - 2] == 'e' && s[l - 1] == 'a')
  {
    cout << "Yes" << endl;
  }
  else
  {
    cout << "No" << endl;
  }

  return 0;
}
