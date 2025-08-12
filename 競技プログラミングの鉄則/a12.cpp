#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

// index が条件を満たすかどうか
bool isOK(int index, int key, vector<ll> &a)
{
  ll num = 0;

  for (ll i = 0; i < a.size(); i++)
  {
    num += index / a[i];
  }

  return num >= key;
}

// 汎用的な二分探索のテンプレ
int binary_search(int key, vector<ll> &a)
{
  int left = -1;       // 「index = 0」が条件を満たすこともあるので、初期値は -1
  int right = 1e9 + 1; // 「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

  /* どんな二分探索でもここの書き方を変えずにできる！ */
  while (right - left > 1)
  {
    int mid = left + (right - left) / 2;

    if (isOK(mid, key, a))
      right = mid;
    else
      left = mid;
  }

  /* left は条件を満たさない最大の値、right は条件を満たす最小の値になっている */
  return right;
}

int main()
{
  ll n, k;
  cin >> n >> k;

  vector<ll> a(n);

  for (ll i = 0; i < n; i++)
  {
    cin >> a[i];
  }

  sort(a.begin(), a.end());

  ll result = binary_search(k, a);
  cout << result << endl;

  return 0;
}
