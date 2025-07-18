#include <stdio.h>
#include <iostream>
#include <vector>

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

// index が条件を満たすかどうか
bool isOK_right(int index, int key, vector<ll> &a)
{
  if (a[index] > key)
    return true;
  else
    return false;
}

// 汎用的な二分探索のテンプレ
int binary_search_right(int key, vector<ll> &a)
{
  int left = -1;             // 「index = 0」が条件を満たすこともあるので、初期値は -1
  int right = (int)a.size(); // 「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

  /* どんな二分探索でもここの書き方を変えずにできる！ */
  while (right - left > 1)
  {
    int mid = left + (right - left) / 2;

    if (isOK_right(mid, key, a))
      right = mid;
    else
      left = mid;
  }

  /* left は条件を満たさない最大の値、right は条件を満たす最小の値になっている */
  return right;
}

int main()
{
  ll n;
  cin >> n;

  vector<ll> x(n);
  for (ll i = 0; i < n; i++)
  {
    cin >> x[i];
  }

  vector<ll> p(n);
  vector<ll> csum(n + 1, 0);

  for (ll i = 0; i < n; i++)
  {
    cin >> p[i];

    if (i == 0)
    {
      csum[i + 1] = p[i];
    }
    else
    {
      csum[i + 1] = csum[i] + p[i];
    }
  }

  ll q;
  cin >> q;

  ll l, r;
  for (ll i = 0; i < q; i++)
  {
    cin >> l >> r;

    ll left_index = binary_search(l, x);
    ll right_index = binary_search_right(r, x);

    // cout << left_index << " " << right_index << endl;

    ll ans = csum[right_index] - csum[left_index];
    cout << ans << endl;
  }

  return 0;
}
