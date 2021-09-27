s1 = input()
s2 = input()
s3 = input()

s4 = list(filter(lambda x: not x in [s1, s2, s3], [
          'ABC', 'ARC', 'AGC', 'AHC']))

print(s4[0])
