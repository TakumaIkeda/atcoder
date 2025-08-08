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

  vector<ll> a(n);
  vector<ll> sum(n);
  vector<ll> diff(n);
  map<ll, ll> sum_map;
  map<ll, ll> diff_map;

  for (ll i = 0; i < n; i++)
  {
    cin >> a[i];
    sum[i] = i + a[i] + 1;
    diff[i] = i - a[i] + 1;
    sum_map[sum[i]]++;
    diff_map[diff[i]]++;
  }

  ll cnt = 0;
  for (auto &pair : sum_map)
  {
    ll key = pair.first;
    ll value = pair.second;

    // sum_mapとdiff_mapのキーが同じ場合、valueの積をcntに加算
    if (diff_map.find(key) != diff_map.end())
    {
      cnt += value * diff_map[key];
    }
  }

  cout << cnt << endl;

  return 0;
}
