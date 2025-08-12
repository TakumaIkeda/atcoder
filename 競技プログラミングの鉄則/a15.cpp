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

  vector<pair<ll, ll>> b(n); // firstにaのインデックス、secondにはa[i]==a[i-1]ならb[i-1]を、そうでなければb[i-1]+1を格納
  b[0].first = a[0].second;
  b[0].second = 1;
  for (ll i = 1; i < n; i++)
  {
    b[i].first = a[i].second;
    if (a[i].first == a[i - 1].first)
    {
      b[i].second = b[i - 1].second;
    }
    else
    {
      b[i].second = b[i - 1].second + 1;
    }
  }

  sort(b.begin(), b.end());

  for (ll i = 0; i < n; i++)
  {
    cout << b[i].second << " ";
  }

  cout << endl;

  return 0;
}
