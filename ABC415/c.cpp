#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>

typedef long long ll;

using namespace std;

int pow(int a, int b)
{
  int result = 1;
  for (int i = 0; i < b; i++)
  {
    result *= a;
  }
  return result;
}

int main()
{
  ll t;
  ll n;
  string s;

  cin >> t;
  for (ll i = 0; i < t; i++)
  {
    cin >> n >> s;
    vector<bool> state(n, false);
    vector<bool> visited(1 << n, false);
    queue<vector<bool>> q;
    q.push(state);
    bool flag = false;

    while (!q.empty())
    {
      vector<bool> current = q.front();
      q.pop();

      // currentが全て1のときは終了
      bool allOne = true;
      for (int j = 0; j < n; j++)
      {
        if (!current[j])
        {
          allOne = false;
          break;
        }
      }

      if (allOne)
      {
        if (s[s.size() - 1] == '1')
        {
          break;
        }

        flag = true;
        break;
      }

      // currentは2進数なので、intに変換して、s[current]が0のとき処理をする
      int currentInt = 0;
      for (int j = 0; j < n; j++)
      {
        if (current[j])
        {
          currentInt += pow(2, j);
        }
      }

      if (currentInt == 0)
      {
        // qにcurrentから0を1つ1に変えたものを全て追加
        for (int j = 0; j < n; j++)
        {
          if (!current[j])
          {
            vector<bool> next = current;
            next[j] = true;
            int nextInt = currentInt + pow(2, j);
            if (!visited[nextInt])
            {
              visited[nextInt] = true;
              q.push(next);
            }
          }
        }
      }

      if (currentInt != 0 && s[currentInt - 1] == '0')
      {
        // qにcurrentから0を1つ1に変えたものを全て追加
        for (int j = 0; j < n; j++)
        {
          if (!current[j])
          {
            vector<bool> next = current;
            next[j] = true;
            int nextInt = currentInt + pow(2, j);
            // nextIntがvisitedに登録されていない場合のみ追加
            if (!visited[nextInt])
            {
              visited[nextInt] = true;
              q.push(next);
            }
            else
            {
              continue; // 既に訪れた状態はスキップ
            }
          }
        }
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
  }

  return 0;
}
