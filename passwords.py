import math
import os
import random
import re
import sys


def getRegistrationStatus(passwords, k):
    # Write your code here
    password_count = {}
    results =  []
    
    for password in passwords: 
        if password not in password_count:
            password_count[password] = 0
         
        if password_count[password] < k:
            results.append("ACCEPT")
            password_count[password] += 1
        else:
            results.append("REJECT")
        
    return results
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    passwords_count = int(input().strip())

    passwords = []

    for _ in range(passwords_count):
        passwords_item = input()
        passwords.append(passwords_item)

    k = int(input().strip())

    result = getRegistrationStatus(passwords, k)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()