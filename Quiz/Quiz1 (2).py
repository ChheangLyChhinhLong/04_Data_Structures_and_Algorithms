# 1. នៅពេលអ្នកកើត ម្តាយរបស់អ្នកបានបង្កើតគណនីមួយសម្រាប់អ្នកដែលមានទឹកប្រាក់ចំនួន$5000 ដោយធនាគារផ្តល់ការប្រាក់ក្នុងអត្រា6% ដែលគិតលើទឹកប្រាក់សរុបដែលសល់តិចបំផុត បើមានការ ដកប្រាក់(Withdraw)។ នៅរាល់ខួបកំណើតអ្នកម្ដងៗម្តាយរបស់អ្នកបានដាក់ប្រាក់បន្ថែម$500។ ចូរបង្កើតកម្មវិធីដោយប្រើ Python programming ដើម្បីរកទឹកប្រាក់សរុបនៅពេលអ្នកមាន អាយុ n ឆ្នាំ ?
age = int(input("Enter age n: "))

balance = 5000.0
interest_rate = 0.06

for i in range(1, age + 1):
    interest = balance * interest_rate
    
    balance = balance + interest + 500

print(f"Total balance at age {age} = ${balance:,.2f}")