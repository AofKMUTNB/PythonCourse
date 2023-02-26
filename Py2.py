name = 'Anirut'
type(name)
name.lower()            #ตัวหนังสือพิมเล็กหมด
friend = 'สมชาย'
print('สวัสดี'+friend)
money = 10

print(friend + 'ยืมเงิน ' + str(money) + ' บาท')   #เนื่องจากmoneyประเภทเป็นintจึงจำเป็นต้องแปลงเป็นข้อความ(str)ก่อน
print('{}ยืมเงิน {} บาท'.format(friend,money))      #ตัวแปรFriend,maneyในformatจะถูกนำไปใส่ในปีกกาทั้ง2
print(f'{friend}ยืมเงิน {money} บาท')              # f มาจากคำว่า format

money = 14500020492
print(f'{money:,.2f}')

import math
math.pi