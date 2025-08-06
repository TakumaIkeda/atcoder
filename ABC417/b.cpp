#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  ll n, m;
  cin >> n >> m;
  vector<ll> a(n);
  vector<ll> b(m);
  vector<bool> c(n, true);

  for (ll i = 0; i < n; i++)
  {
    cin >> a[i];
  }

  for (ll i = 0; i < m; i++)
  {
    cin >> b[i];

    for (ll j = 0; j < n; j++)
    {
      if (b[i] == a[j] && c[j])
      {
        c[j] = false;
        break;
      }
    }
  }

  for (ll i = 0; i < n; i++)
  {
    if (c[i])
    {
      cout << a[i] << " ";
    }
  }

  cout << endl;

  return 0;
}
