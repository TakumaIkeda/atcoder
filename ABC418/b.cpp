#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

double solve(string partial_s)
{
  ll l = partial_s.size();
  if (partial_s[0] != 't' || partial_s[l - 1] != 't' || l < 3)
  {
    return 0.0;
  }

  double num_t = 0;
  for (ll i = 0; i < l; i++)
  {
    if (partial_s[i] == 't')
    {
      num_t++;
    }
  }

  return (num_t - 2) / (l - 2);
}

int main()
{
  string s;
  cin >> s;

  ll l = s.size();
  double max_result = 0.0;

  for (ll i = 0; i < l; i++)
  {
    for (ll j = i + 1; j < l; j++)
    {
      string partial_s = s.substr(i, j - i + 1);
      double result = solve(partial_s);
      if (result > max_result)
      {
        max_result = result;
      }
    }
  }

  printf("%.15f\n", max_result);

  return 0;
}
