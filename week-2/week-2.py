def calculate(min, max):
# 請用你的程式補完這個函式的區塊
    sum=0
    for x in range(min, max+1):
        sum=sum+x
    print(sum)
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

def avg(data):
# 請用你的程式補完這個函式的區塊
    sum=0
    a=data["count"]
    b=data["employees"]
    for c in b :
        sum = sum+c["salary"]
    answer = sum/a
    print(answer)
    
avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式

def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    a = len(nums)
    c = nums[0] *nums[1]
    for i in range(a):
        for j in range(i + 1, a):
            b = nums[i] * nums[j]
            if b > c :
                c=b

    print(c)


maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

def twoSum(nums, target):
# your code here
    a = len(nums)
    result = []
    for i in range(a):
        for j in range(i + 1, a):
            if (nums[i] + nums[j]) == target:
                result.append(i)
                result.append(j)
                return result                            

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
    a = 0
    b = 0
    for i in nums:
        if i == 0:
           b = b+1
           if a < b:
               a = b
        else:
            b=0
    print(a)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
