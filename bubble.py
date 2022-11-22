nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def bubbleSort(anArray):
    
  for i in range(len(anArray)):

    for n in range(len(anArray) - i - 1):
        
      if anArray[n] > anArray[n + 1]:
        store = anArray[n]
        anArray[n] = anArray[n+1]
        anArray[n+1] = store

bubbleSort(nums)
print(nums)