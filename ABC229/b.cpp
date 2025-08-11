#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

typedef long long ll;

using namespace std;

// ll pow(ll a, ll b)

int main()
{
  ll a, b;
  cin >> a >> b;

  bool flg = true;

  for (ll i = 18; i >= 0; i--)
  {
    ll wari = pow(10, i);
    ll a_wari = a / wari;
    ll b_wari = b / wari;

    if (a_wari + b_wari >= 10)
    {
      flg = false;
      break;
    }

    a = a % wari;
    b = b % wari;
  }

  cout << (flg ? "Easy" : "Hard") << endl;

  return 0;
}
