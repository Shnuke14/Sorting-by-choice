a = [-9, 19, 3, -7, 42, 11]
N = len(a)

for i in range(N - 1):
  m = a[i]
  p = i
  for j in range(i + 1, N):
    if m > a[j]:
      m = a[j]
      p = j

  if p != i:
    t = a[i]
    a[i] = a[p]
    a[p] = t

print(a)