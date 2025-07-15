#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
  long long m, n, N;

  cin >> m >> n >> N;

  long long ans = N;
  long long P = N;
  long long R = 0;
  long long sum = 0;

  while (P + R >= m)
  {
    sum = P + R;
    P = sum / m * n;
    R = sum % m;
    ans += P;
  }

  cout << ans << endl;

  return 0;
}