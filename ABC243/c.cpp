#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>

typedef long long ll;

using namespace std;

int main()
{
  ll n;
  cin >> n;

  vector<ll> x(n);
  vector<ll> y(n);

  for (ll i = 0; i < n; i++)
  {
    cin >> x[i];
    cin >> y[i];
  }

  string s;
  cin >> s;

  map<ll, ll> memor;
  map<ll, ll> memol;
  map<ll, bool> checkedl;
  map<ll, bool> checkedr;

  bool ans = false;

  for (ll i = 0; i < n; i++)
  {
    if (s[i] == 'R')
    {
      if (memol[y[i]] > x[i] && checkedl[y[i]])
      {
        ans = true;
        break;
      }

      if (!checkedr[y[i]] || x[i] < memor[y[i]])
      {
        memor[y[i]] = x[i];
        checkedr[y[i]] = true;
      }
    }

    if (s[i] == 'L')
    {
      if (memor[y[i]] < x[i] && checkedr[y[i]])
      {
        ans = true;
        break;
      }

      if (!checkedl[y[i]] || x[i] > memol[y[i]])
      {
        memol[y[i]] = x[i];
        checkedl[y[i]] = true;
      }
    }
  }

  if (ans)
  {
    cout << "Yes" << endl;
  }
  else
  {
    cout << "No" << endl;
  }

  return 0;
}
