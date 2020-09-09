

def arithmetic_arranger(arr, default=False):
  arr2 = []
  arr3 = []
  arranged_problems = ''

  # arr2 = list(group(arr, ' '))



  # if len(arr2) > 4:
  #   print("length: " + str(len(arr2))):
  #   return "Error: Too many problems."




# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

  for j in arr:
    arr2 += [j for j in j.split(" ") if j]
  
  count = 1

  arrlen = len(arr2)
  for i in range(0,len(arr2)):
    if (i + 1) % 3  == 1:
      arr3.append(arr2[i])
      arr2[i] = 'x'

  if (len(arr2) > 15 or len(arr3) > 5):
    
    return 'Error: Too many problems.'

  for a in arr2:
    if len(a)  > 4:
      
      return 'Error: Numbers cannot be more than four digits.'


  for a in arr3:
    if len(a)  >  4:
      
      return 'Error: Numbers cannot be more than four digits.'





  arrlen = len(arr2)
  for i in range(0,len(arr2)):
    if (i + 1) % 3  == 2:
         if arr2[i] != '+' and arr2[i] != '-':
           
           return  "Error: Operator must be '+' or '-'."
  i  = 0 
  for i in range(len(arr2)):
    arr2[i] = arr2[i].replace('x', "") #removed the space
    count += 1
  # del arr2[(i + 1) % 3 - (i)  == 1]
  # return arr2

  # arranged_problems += " " *  (5 - len(arr3[0]))
  # count = 1
  if (len(arr2[2])) > (len(arr3[0])):
        arranged_problems += " " * (len(arr2[2]) - len(arr3[0]) + 2)
  else:
      arranged_problems += " " * (len(arr2[2]) + len(arr3[0])-1)




  i = 0
  for i in range(len(arr3)):  
    j = i * 3

    arranged_problems += arr3[i]
    if i < len(arr3) - 1:
         if(len(arr3[i+1]) > 1 or len(arr3[i]) == 4): #not adding space
           arranged_problems +=  " " * 6 
         elif (len(arr3[i+1]) == 1):
           arranged_problems +=  " " * 9
    # arranged_problems +=("  " *(4  + (4 - len(a))) )+ a 
  arranged_problems += '\n'

  i = 0
  
  for i in range(0,len(arr2)):
    j = int(i / 3)
    if (i + 1) % 3 == 0:
      
        if (len(arr2[i]) > len(arr3[j])):
          arr2[i - 1] = arr2[i - 1].replace(arr2[i - 1],  
          arr2[i - 1] + " ")
        else:
          arr2[i - 1] = arr2[i - 1].replace(arr2[i - 1],
           arr2[i - 1] + " " * (
          abs(max(len(arr2[i]), len(arr3[j])) -
          min(len(arr2[i]), len(arr3[j])) + 1) 
        ) )          
        # arr2[i] = arr2[i].replace(arr2[i], ('   ' * 4 + arr2[i]))

         
  
  i = 0
  for i in range(len(arr2)):
    arranged_problems +=  arr2[i] 
    if (i + 1) % 3 == 0 and i < len(arr2) - 3 :
         arranged_problems +=  " " * 4
  #Added the spaces afte the numbers only
      
  
  arranged_problems += '\n'


  
  i = 0
  for i in range(0,len(arr2)):
    j = int(i / 3)
    if (i + 1) % 3  == 0:
        if(not(arr2[i].isnumeric() and arr3[j].isnumeric())):
          
          return 'Error: Numbers must only contain digits.'

  i = 0
  for i in range((len(arr2))):
    j = int(i / 3)
    if (i + 1) % 3  == 0:
       arranged_problems += '-' * (max(len(arr2[i]), len(arr3[j])) + 2)
       if(i < len(arr2) - 3):
         arranged_problems += ' ' * 4
  
  # arranged_problems += '\n'

  solutions = []
  
  i = 0
  if default == True:
    arranged_problems += '\n' +  ' ' 
    for i in range((len(arr2))):
      j = int(i / 3)
      if (i + 1) % 3  == 0:
         if (arr2[i - 1].strip() == '+'):
           solutions.append( int(arr2[i]) + int(arr3[j]))
         elif (arr2[i - 1].strip() == '-'):
           solutions.append( int(arr3[j]) - int(arr2[i]))
         if j == 0:
               arranged_problems += str(solutions[j])  
         if j > 0:
           if solutions[j] < 1:
              arranged_problems += "     " + str(solutions[j])  
           else:
              arranged_problems += "      " + str(solutions[j]) 
    return arranged_problems


  return arranged_problems


