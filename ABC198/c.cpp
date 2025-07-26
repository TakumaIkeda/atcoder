#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>

typedef long long ll;

using namespace std;

int main()
{
  ll r, x, y;

  cin >> r >> x >> y;

  ll distance_squared = x * x + y * y;

  ll ans = 0;

  if (distance_squared < r * r)
  {
    cout << 2 << endl;
    return 0;
  }

  while (distance_squared > (r * ans) * (r * ans))
  {
    ans++;
  }

  cout << ans << endl;

  return 0;
}
