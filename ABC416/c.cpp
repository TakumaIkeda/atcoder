#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

ll pow(ll a, ll b)
{
  ll res = 1;
  for (ll i = 0; i < b; i++)
  {
    res *= a;
  }
  return res;
}

void recursive(ll rec_count, ll k, ll n, vector<string> s, vector<string> tmp, vector<string> *memo)
{
  if (rec_count == k)
  {
    string str = "";
    for (ll i = 0; i < tmp.size(); i++)
    {
      str += tmp[i];
    }
    memo->push_back(str);
    return;
  }

  for (ll i = 0; i < n; i++)
  {
    tmp.push_back(s[i]);
    recursive(rec_count + 1, k, n, s, tmp, memo);
    tmp.pop_back();
  }
}

int main()
{
  ll n, k, x;
  cin >> n >> k >> x;
  vector<string> s(n);
  for (ll i = 0; i < n; i++)
  {
    cin >> s[i];
  }

  vector<string> memo(0);
  vector<string> tmp(0);
  recursive(0, k, n, s, tmp, &memo);
  sort(memo.begin(), memo.end());

  cout << memo[x - 1] << endl;

  return 0;
}
