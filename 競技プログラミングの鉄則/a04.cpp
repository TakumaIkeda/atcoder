#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll n;
  cin >> n;

  for (ll i = 0; i < 10; i++)
  {
    if (n >= (1 << (9 - i)))
    {
      cout << 1;
      n -= (1 << (9 - i));
    }
    else
    {
      cout << 0;
    }
  }

  cout << endl;

  return 0;
}
