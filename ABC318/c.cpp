#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  long long n, d, p;

  cin >> n >> d >> p;

  vector<long long> f(n);

  for (int i = 0; i < n; i++)
  {
    cin >> f[i];
  }

  sort(f.begin(), f.end());

  vector<long long> s(n + 1, 0);

  for (int i = 0; i < n; i++)
  {
    s[i + 1] = s[i] + f[i];
  }

  long long ans = s[n];

  for (int i = 0; i * d < n + d; i++)
  {
    long long ans_i;

    if (n - i * d < 0)
    {
      ans_i = p * i;
      ans = (ans_i < ans) ? ans_i : ans;
      break;
    }

    ans_i = s[n - i * d] + p * i;
    ans = (ans_i < ans) ? ans_i : ans;
  }
  cout << ans << endl;

  return 0;
}