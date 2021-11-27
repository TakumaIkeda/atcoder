#include <iostream>
#include <set>

using namespace std;

int main() {
  int n, x;
  cin >> n >> x;

  int a[n];
  for (int i = 0; i < n; i++) cin >> a[i];

  set<int> s;
  s.insert(1000000);

  while (1) {
    if (*(s.find(x)) == *(s.end())) {
      s.insert(x);
      x = a[x-1];
    } else {
      break;
    }
  }

  cout << s.size() - 1 << endl;
}
