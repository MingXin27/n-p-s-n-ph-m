lst1 = ["+) Rau xanh như bắp cải, cải bắp, cải xoong, bông cải xanh, rau mùi, và rau bina." , 
        "+) Thịt gà không da." , 
        "+) Hải sản: Các loại hải sản như cá hồi, cá trắng, tôm." , 
        "+) Quả lựu.",
        "+) Gạo lứt, lúa mì nguyên hạt, yến mạch nguyên hạt, và lúa mạch.",
        "+) Nước lọc."
        ]

lst2 = ["+) Thịt gà không da và các loại cá như cá hồi, cá trắng.",
        "+) Đậu hủ.",
        "+) Bơ đậu phộng và dầu ôliu, quả bơ.",
        "+) Sữa, sữa chua, và phô mai.",
        "+) Lúa mì nguyên hạt, gạo lứt, và các sản phẩm từ ngũ cốc nguyên hạt.",
        "+) Quả lựu, táo, cam."
        ]

lst3 = ["+) Thịt bò, thịt heo, thịt dê.",
        "+) Sữa, sữa chua, phô mai.",
        "+) Bơ đậu phộng và dầu ôliu, quả bơ.",
        "+) Bánh mì nguyên hạt, bánh mỳ, bánh quy.",
        "+) Khoai tây, bắp, và các loại ngũ cốc như lúa mạch, bánh mỳ.",
        "+) Thịt gà, cút, vịt."
        ]

print('*' * 34)
print("*        TDEE CALCULATOR         *")
print('*' * 34)

while True:
    print("A. Nam") 
    print("B. Nữ")
    choose1 = input("Chọn giới tính của bạn: ").upper()
    if choose1 == 'A':
        sex = "Nam"
        break
    elif choose1 == 'B':
        sex = "Nữ"
        break
    else:
        continue
print("=" * 60)
while True:
    age = int(input("Nhập tuổi của bạn: "))
    if age < 0:
        continue
    else:
        break
print("=" * 60)
while True:
    height = float(input("Nhập chiều cao(cm) của bạn: "))
    if height < 0:
        continue
    else:
        break
print("=" * 60)
while True:
    weight = float(input("Nhập cân nặng(kg) của bạn: " ))
    if weight < 0:
        continue
    else:
        break
print("=" * 60)
while True:
    print('A. Ít vận động (không tập luyện/nhân viên văn phòng)')
    print('B. Vận động nhẹ (Tập luyện 1-3 lần/tuần)')
    print('C. Vận động vừa (Tập luyện 3-5 ngày/tuần)')
    print('D. Vận động nhiều (Tập luyện 6-7 ngày/tuần)')
    print('E. Hoạt động cực nhiều (Ngày tập 2 lần/Là vận động viên)')
    choose2 = input("Chọn cường độ tập luyện của bạn: ").upper()
    if choose2 == 'A':
        R = 1.2
        break
    elif choose2 == 'B':
        R = 1.375
        break
    elif choose2 == 'C':
        R = 1.55
        break
    elif choose2 == 'D':
        R = 1.725
        break
    elif choose2 == 'E':
        R = 1.9
        break
    else:
        continue

if(sex == "Nam"):
    BMR = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    TDEE = int(BMR * R)
else:
    BMR = 665 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    TDEE = int(BMR * R)
    
print("=" * 60)
while True:
    print('A.Giảm cân')
    print('B.Duy trì hiện tại')     
    print('C.Tăng cân')  
    choose3 = input("Nhập mục tiêu của bạn: ").upper()
    if choose3 == 'A':
        print("- Nếu muốn giảm cân:Bạn nên ăn ít hơn", TDEE , "calo trong 1 ngày, chỉ nên cắt giảm từ 200 - 300 calo, không nên cắt giảm quá nhiều.")
        print("- Dưới đây là một số thực phẩm gợi ý cho bạn: ")
        for i in range(len(lst1)):
            print(lst1[i])
        break
    elif choose3 == 'B':
        print("- Nếu muốn duy trì cân nặng: Ăn bằng", TDEE ,"calo trong 1 ngày")
        print("- Dưới đây là một số thực phẩm gợi ý cho bạn: ")
        for i in range(len(lst2)):
            print(lst2[i])
        break
    elif choose3 == 'C':
        print("- Nếu muốn tăng cân: Phải ăn nhiều hơn so với",TDEE ,"calo trong 1 ngày")
        print("- Dưới đây là một số thực phẩm gợi ý cho bạn: ")
        for i in range(len(lst3)):
            print(lst3[i])
        break
    else:
        continue 
