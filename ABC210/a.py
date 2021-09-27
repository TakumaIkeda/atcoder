N, A, X, Y = map(int, input().split())

if (A >= N):
  print(N * X)
else:
  print(A * X + (N - A) * Y)
