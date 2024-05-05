# Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. 
# The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 
# 1) Only one disk can be moved at a time. 
# 2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack 
# i.e. a disk can only be moved if it is the uppermost disk on a stack. 
# 3) No disk may be placed on top of a smaller disk.

def toh(n,A,B,C):
    # Base condition
    if(n==1): 
        print("Move disk ",n,"from ",A,"to ",C)
        return

    else:
        # Recursive function-stack is used
        # Move n-1 disk from A to B
        toh(n-1,A,C,B)

        # Move last disk from A to C
        print("Move disk ",n,"from ",A,"to ",C)

        # Move n-1 disk from B to C
        toh(n-1,B,A,C)

n=int(input("Enter The number of disks:"))
toh(n,"A","B","C")

# OUTPUT
# PS C:\Users\Sanika\OneDrive\Desktop\IT\.vscode\AI\TowerOfHanoi> python a.py
# Enter The number of disks:3
# Move disk  1 from  A to  C
# Move disk  2 from  A to  B
# Move disk  1 from  C to  B
# Move disk  3 from  A to  C
# Move disk  1 from  B to  A
# Move disk  2 from  B to  C
# Move disk  1 from  A to  C