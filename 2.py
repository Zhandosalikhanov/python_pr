#B = (μ0nI/2)(cos α1 - cos α2)
#w = 2000 (turns); R = 8,25.10-3 (m); ℓ = 0,047 (м); μ0 = 4π.10 -7 H/m. The cosinuses in the formula (14.5) are:
#cos (α1) = (x - ℓ/2)/√ (R2 + (x - ℓ/2)2). and 
#cos (α2) = (x + ℓ/2)/√ (R2 + (x + ℓ/2)2).

import math

x = list(map(lambda x: float(x), input().split()))
cons =((4 * math.pi * 0.0000007) * (2000 / 0.047) * 0.2) / 2
print("the const is:", cons, '\n')
R = 8.25 / 1000
for i in x:
    cos1 = (i - 0.047/2) / math.sqrt(R*R + pow(i - 1/2, 2))
    cos2 = (i + 0.047/2) / math.sqrt(R*R + pow(i + 1/2, 2))
    print(f'for x = {i}: {1000 * cons * (cos1 - cos2)}')