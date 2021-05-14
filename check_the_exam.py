def check_exam(arr1,arr2):
    x = sum([4 if x==y else 0 if not y else -1 for x,y in zip(arr1, arr2)])
    return x if x>0 else 0
  
