#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

int main()
{
  ll n;
  cin >> n;

  vector<pair<ll, ll>> a(n);
  for (ll i = 0; i < n; i++)
  {
    cin >> a[i].first; // firstには値を、secondにはインデックスを格納
    a[i].second = i;
  }

  sort(a.begin(), a.end());

  vector<ll> b(n + 10);
  b[a[0].second] = 1;
  for (ll i = 1; i < n; i++)
  {
    if (a[i].first == a[i - 1].first)
    {
      b[a[i].second] = b[a[i - 1].second];
    }
    else
    {
      b[a[i].second] = b[a[i - 1].second] + 1;
    }
  }

  for (ll i = 0; i < n; i++)
  {
    cout << b[i] << " ";
  }

  cout << endl;

  return 0;
}
