#include <stdio.h>
#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
  int n;

  cin >> n;

  vector<int> a(n);

  for (int i = 0; i < n; i++)
  {
    cin >> a[i];
  }

  int x;

  cin >> x;

  bool flag = false;

  for (int i = 0; i < n; i++)
  {
    if (a[i] == x)
    {
      flag = true;
      break;
    }
  }

  if (flag)
  {
    cout << "Yes" << endl;
  }
  else
  {
    cout << "No" << endl;
  }

  return 0;
}
