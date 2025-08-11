#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

// index が条件を満たすかどうか
bool isOK(int index, int key, vector<ll> &a)
{
  if (a[index] >= key)
    return true;
  else
    return false;
}

// 汎用的な二分探索のテンプレ
int binary_search(int key, vector<ll> &a)
{
  int left = -1;             // 「index = 0」が条件を満たすこともあるので、初期値は -1
  int right = (int)a.size(); // 「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

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
  ll n, q;
  cin >> n >> q;
  vector<ll> a(n);
  vector<ll> asum(n, 0);
  for (ll i = 0; i < n; i++)
  {
    cin >> a[i];
  }

  sort(a.begin(), a.end());

  for (ll i = 0; i < n; i++)
  {
    if (i == 0)
      asum[i] = a[i];
    else
      asum[i] = asum[i - 1] + a[i];
  }

  for (ll i = 0; i < q; i++)
  {
    ll b;
    cin >> b;
    ll idx = binary_search(b, a);
    if (idx == 0)
    {
      cout << (n - idx) * (b - 1) + 1 << endl;
      continue;
    }
    // cout << "n-idx: " << n - idx << endl;
    ll ans = asum[idx - 1] + (n - idx) * (b - 1) + 1;
    if (ans <= asum[n - 1])
      cout << ans << endl;
    else
      cout << -1 << endl;
  }

  return 0;
}
