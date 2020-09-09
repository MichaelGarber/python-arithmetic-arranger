# Arrithmetic arranger
This program is based on [this project](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter). 

This program prompts the user to enter + or - math equations. You cna have a max of four equations, and the max number of digits  per number is 4. It enters the equations in the typical equestion format. 

## Variables

arr2 = The bottom part of the equation, including the operation(+,-) and the adjacent number

arr3 = The top part of the equation.

## Mistakes and decisions
- Iterated arr3 with i * 3 to get values of arr2, but it was out of range. Now, I will try the reverse
- Noticed alignment worked when comparing arr2 and 3 as which one is higher. 
- Used max function
- MovED arr2 moves too many spaces because it spaces operators and numbers.
- Forgot to change to len when comparing.


## Sources
[Remove space from string] (https://www.journaldev.com/23763/python-remove-spaces-from-string#:~:text=to%20remove%20spaces.-,strip(),remove%20leading%20and%20trailing%20whitespaces.&text=If%20you%20want%20to%20remove,or%20rstrip()%20function%20instead).
