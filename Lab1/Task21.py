listComponent = [5, 10, 15, 20, 25, 30, 35]
listComponent.reverse()
print(listComponent)

middleNumber = int((len(listComponent)-1)/2)
print(middleNumber)
listComponent.pop(middleNumber)
print(listComponent)

print(sum(listComponent))
print(max(listComponent))
print(sum(listComponent)/(len(listComponent)))



