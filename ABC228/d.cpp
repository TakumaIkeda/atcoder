#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
  int q;
  cin >> q;
  int N = 1<<20;
  int n[N];
  int t;
  long long x;

  for (int i = 0; i < N; i++) {
    n[i] = -1;
  }

  int h;
  set<int> s;
  for (int i = 0; i < N; i++) {
    s.insert(i);
  }

  for (int i = 0; i < q; i++) {
    cin >> t >> x;
    if (t == 1) {
      h = x;
      if (n[h % N] == -1) {
        n[h % N] = x;
        s.erase(h % N);
      } else {
        auto key = s.upper_bound(h % N);
        if (n[*key % N] != -1) {

        }
        n[*key % N] = x;
        s.erase(*key % N);
      }
    } else {
      cout << n[x % N] << endl;
    }
  }
}
