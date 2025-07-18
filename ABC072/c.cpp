#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  long long n;
  cin >> n;

  vector<long long> a(n);
  vector<long long> count(1000000);

  for (long long i = 0; i < n; i++)
  {
    cin >> a[i];
    count[a[i]]++;
    count[a[i] + 1]++;
    count[a[i] + 2]++;
  }

  long long max_count = 0;

  for (long long i = 0; i < 1000000; i++)
  {
    if (count[i] > max_count)
    {
      max_count = count[i];
    }
  }

  cout << max_count << endl;

  return 0;
}
