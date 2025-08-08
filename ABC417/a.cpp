#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll n, a, b;
  cin >> n >> a >> b;
  string s;
  cin >> s;

  for (ll i = 0; i < n; i++)
  {
    if (i >= a && i < n - b)
    {
      cout << s[i];
    }
  }

  cout << endl;

  return 0;
}
