# import math
#
# def karatsuba(x,y):
#     if x<10 or y<10:
#         return x*y
#     else:
#         n=max(len(str(x)),len(str(y)))
#         nby=int(n/2)
#         a=int(math.floor(x/10**(nby)))
#         b=int(x%(10**nby))
#         c=int(math.floor(y/10**(nby)))
#         d=int(y%(10**nby))
#
#         ac=karatsuba(a,c)
#         bd=karatsuba(b,d)
#
#         ad_plus=karatsuba(a+b,c+d)-ac-bd
#         prod=int(ac * 10**(2*nby)+(ad_plus*10**nby)+bd)
#
#         return prod
#
# print(karatsuba(12,24))

# hashtable=[' ','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
#
# def printwordsutil(number,curr,output,n):
#     if curr>len(number)-1:
#         print(output)
#         return
#     for i in range(len(hashtable[number[curr]])):
#         output.append(hashtable[number[curr]][i])
#         printwordsutil(number,curr+1,output,n)
#         output.pop()
#
# def printwords(number,n):
#     printwordsutil(number,0,[],n)
#
# if __name__=='__main__':
#     number=[2,3,9]
#     n=len(number)
#     printwords(number,n)


# def isHappy(n):
#     def sumsqr(num):
#         result=0
#         while(num>0):
#             result=result+(num%10)*(num%10)
#             num=num//10
#         return result
#
#     seen=set()
#     while sumsqr(n) not in seen:
#         sum1=sumsqr(n)
#         if sum1==1:
#             return True
#         else:
#             seen.add(sum1)
#             n=sum1
#     return False
#
# print(isHappy(2))
#
# from collections import deque
#
#
# # Recursive function to print all distinct subsets of S
# # S   --> input set
# # out --> list to store subset
# # i   --> index of next element in set S to be processed
# def findPowerSet(S, out, i):
#
#     # if all elements are processed, print the current subset
#     if i < 0:
#         print(list(out))
#         return
#
#     # include current element in the current subset and recur
#     out.append(S[i])
#     findPowerSet(S, out, i - 1)
#
#     # exclude current element in the current subset
#     out.pop()       # backtrack
#
#     # remove adjacent duplicate elements
#     while i > 0 and S[i] == S[i - 1]:
#         i = i - 1
#
#     # exclude current element in the current subset and recur
#     findPowerSet(S, out, i - 1)
#
#
# # Program to generate all distinct subsets of given set
# if __name__ == '__main__':
#
#     S = [1, 3, 1]
#
#     # sort the set
#     S.sort()
#
#     # create an empty list to store elements of a subset
#     out = deque()
#     findPowerSet(S, out, len(S) - 1)

#1 2 1 5 2
# d=24
# p=2
# list1=[]
# list2=[]
# list3=[]
# for i in range(2,d):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         list1.append(i)
# print(list1)
# z=int(d/p)
# for i in range(len(list1)):
#     m=list1[i]+z
#     if m in list1:
#         list2.append(list1[i])
#         while(m<=list1[-1]):
#             list2.append(m)
#             m+=z
#         if len(list2)==p:
#             list3.append(list2)
#             list2=[]
# print(len(list3))

#finding second highest number without sorting  in even index and odd index and returning sum of even and odd number of second highest number

# def largesum(arr):
#     infi=-9999
#     second=-9999
#     third=-9999
#     fourth=-9999
#     for i in range(0,len(arr),2):     #3,2,1,7,5,4
#         if infi<arr[i]:
#             second=infi
#             infi=arr[i]
#         if second < arr[i] and second!=infi and infi>arr[i]:
#             second=arr[i]
#
#     for i in range(1,len(arr),2): #2,7,4
#         if third<arr[i]:
#             fourth=third
#             third=arr[i]
#         if fourth < arr[i] and fourth!=third and third >arr[i]:
#             fourth=arr[i]
#
#     return fourth+second
# arr=[1,8,0,2,3,5,6]
# print(largesum(arr))


def isValid(string,count):
        if string == 'yes':
            return count
        else:
            count=count+1
            return count



# t=int(input())
# for i in range(t):
#     m=int(input())
#     list1=list(map(int,input().split(' ')))
#     list2=list1.copy()
#     string='yes'
#     count,laso=0,0
#     laso1=0
#     for j in range(1,len(list1)-1,2):
#         if list1[j]>list1[j-1] and list1[j]>list1[j+1]:
#             laso=isValid(string,count)
#             list1[j]=list1[j-1]
#             string='no'
#
#     string='yes'
#     for j in range(0,len(list2)-1,2):
#         if j==0:
#             continue
#         else:
#             if list2[j]<list2[j-1] and list2[j]<list2[j+1]:
#                 laso1=isValid(string,count)
#                 list2[j]=list2[j-1]
#                 string='no'
#       #1 1 2 5 1
#     print(min(laso,laso1))

# def calculate(n,num,q,r):
#     p=''
#     while(q>0):
#         q=num//n
#         r=num%n
#         if r>9:
#             m=r%10
#             p=p+chr(65+m)
#         else:
#             p=p+str(r)
#         num=q
#     return p[::-1]
#
#
# quotient=99999
# remainder=-99999
# print(calculate(21,5678,quotient,remainder))


# def numberofcarries(num1,num2):
#     count=0
#     four=0
#     while(max(num1,num2)):          #451 %10=1   349%10=9  1+9=10 four=1
#         one=num1%10
#         num1=num1//10
#         two=num2%10
#         num2=num2//10
#         three=one+two
#         if four>0:
#             three=three+four
#         if three>9:
#             four= three//10
#             count+=1
#     return count
#
#
#
#
# print(numberofcarries(23,563))


#
# def stringchange(string,length,ch1,ch2):
#     string2=''
#     if string==None:
#         return 0
#     for i in range(len(string)):
#         if string[i]==ch1:
#             string2+=ch2
#         elif string[i]==ch2:
#             string2+=ch1
#         else:
#             string2+=string[i]
#     return string2
#
# print(stringchange('apples',len('apples'),'a','p'))

def palindromevalue(a,b):
    list1=[]
    for i in range(a,b+1):
       if str(i)== str(i)[::-1]:
           list1.append(i)
    return list1

print(palindromevalue(10,80))