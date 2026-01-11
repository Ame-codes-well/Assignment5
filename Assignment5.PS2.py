numbers=[]
for i in range(1,11):
    numbers.append(i)
print(f'original list: {numbers}')
L2=numbers[:5]
print(f'extracted 5 elements: {L2}')
print(f'reverse extracted 5 elements: {L2[::-1]}')