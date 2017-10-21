output = [1,0,0]
expected = [0,0,1]
outputs_sum = 0
expected_sum = 0
for index, digit in enumerate(output):
    outputs_sum += (2**(len(output)-1-index))*digit
for index, digit in enumerate(expected):
    expected_sum += (2**(len(expected)-1-index))*digit

print abs(expected_sum-outputs_sum)
