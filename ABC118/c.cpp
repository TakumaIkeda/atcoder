#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int gcd(int a, int b) {
  while (1) {
    if (a<b) swap(a, b);
    if (!b) break;
    a %= b;
  }

  return a;
}

int main() {
  int n, j;
  std::vector<int> a(n);

  std::cin >> n;


  for (int i = 0; i < n; i++) {
    std::cin >> j;
    a[i] = j;
  }

  int ans = a[0];
  for (int i = 1; i < n; i++) {
    ans = gcd(ans, a[i]);
  }

  std::cout << ans << std::endl;

  return 0;
}
