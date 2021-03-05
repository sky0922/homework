#作業一
def calculate(min, max):

    #設定結果初始為 0
    result = 0

    for i in range(min, max+1, 1):
        result = result + i
        #print(i, result)
    print(result)
    return

# 請用你的程式補完這個函式的區塊
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30



#作業二
def avg(data):

    #看資料有沒有近來
    #print(data)

    #看員工數量、資料類型
    #print(data['count'], type(data['count']))

    #看員工明細，資料類型
    #print(data['employees'], type(data['employees']))

    #把 empolyees 的 list 資料丟給變數
    employees=data['employees']

    #看看 list 第一筆資料是什麼
    #print(employees[0])

    #員工數量丟給變數
    staff_total=data['count']

    #設定薪水總和初始值
    sum = 0
    
    #開始跑所有員工薪水資料
    for i in range(staff_total):
        dict_employees = dict(employees[i])
        #確認每一筆資料及資料類型
        #print(dict_employees['salary'],type(dict_employees['salary']))

        #薪水加總
        sum = sum + dict_employees['salary']
        #print(sum)

    #計算平均
    avgsum = sum/staff_total
    print(avgsum)

    return avgsum

    # 請用你的程式補完這個函式的區塊

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



#作業三
def maxProduct(nums):

    #排序做法
    #sortnums = sorted(nums,reverse=True) #將 list 由大到小排序
    #print(sortnums) #印出來看看對不對
    #最大 sortnums[0]*sortnums[1] 跟最小 sortnums[-1]*sortnums[-2]
    #比較結果，輸出大的值

    #非排序做法
    #抓取 List 中的最大及最小值
    max_nums = max(nums)
    min_nums = min(nums)
    
    #先把要比較的數字設定為最小
    key_nums = min(nums)

    #找次大
    for i in range(len(nums)):
        #print("目前 i", i, max_nums, nums[i], min_nums, key_nums)
        if max_nums > nums[i] > min_nums:
            if nums[i] > key_nums:
                key_nums = nums[i]
    
    #陣列最大兩數字相乘結果為變數 a
    a = (max_nums*key_nums)

    #先把要比較的數字設定為最大
    key_nums = max(nums)

    #找次小
    for i in range(len(nums)):
        if max_nums > nums[i] > min_nums:
            if nums[i] < key_nums:
                key_nums = nums[i]

    #陣列最小兩數字相乘結果為變數 b
    b = (min_nums*key_nums)

    #兩個變數比較後輸出結果
    if a > b:
        print(a)
    else:
        print(b)

    return

maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值



#作業四
def twoSum(nums, target):

    #print(nums, target, len(nums))

    #所有位置兩兩相加
    for i in range(len(nums)-1):
        for j in range(1, len(nums)):
            sum = nums[i]+nums[j]

            #如果數字加總等於目標數字，傳回結果，跳出迴圈
            if sum == target:
                #print("---------",i, j, nums[i], nums[j], nums[i]+nums[j], sum)
                result = [i, j]
                #將 LIST 結果，由小到大排序
                result = sorted(result)
                #print(result)
                break

    return result

# your code here
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9



#作業五
#構想 取得 list 元素個數
#使用迴圈，判斷元素是否為 0，是的話計數 +1，繼續迴圈
#不是的話，計數清空重算
#跑完迴圈後，重新排列 LIST 取出最大值

def maxZeros(nums):

    #將陣列存入變數
    input_list = nums

    #看一下陣列數量
    #print(len(input_list))

    #給予兩個變數初始值
    repeat_times=0
    list_repeat_times = [0]

    for i in range(len(input_list)):
        
        if input_list[i] == 0:
            #如果陣列數字為 0，計數加一，把結果增加進陣列中 
            repeat_times = repeat_times + 1
            list_repeat_times.append(repeat_times)
        else:
            #如果陣列數字不是 0，計數清空
            repeat_times=0
        
    #排序陣列，從大到小
    list_repeat_times = sorted(list_repeat_times, reverse=True)
    #印出排序過後的陣列看看
    #print(list_repeat_times)
    #印出重複最大的次數
    print(list_repeat_times[0])


# 請用你的程式補完這個函式的區塊
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
