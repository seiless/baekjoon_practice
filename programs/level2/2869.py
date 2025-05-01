A, B, V = list(map(int,input().split()))

import math

climbed_date = math.ceil((V - B) / (A - B))
print(climbed_date)