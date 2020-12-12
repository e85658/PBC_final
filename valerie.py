import tkinter as tk
from tkinter import ttk
from tkinter import *


'''--------------------- 頁面設定 ---------------------'''

StartPage = tk.Tk()
StartPage.title("今天可以吃多少？")
StartPage.geometry("400x200")

Frame2 = Frame(StartPage)
Frame2.place(width=400, height=200)

Frame1 = Frame(StartPage)  # 輸入基本資料的首頁
Frame1.place(width=400, height=200)


'''------------------ 點擊第一頁的「開始計算」 Button 後，要開始做的 Function '''
'''------------------ 抓取第一頁輸入的資料下去做後面所有的計算'''


def What2Eat(frame):
    frame.tkraise()  # 跳出新頁面

    ''' Step1. ======== 抓取資料 ======== '''
    Gender = GenderInput.get()
    AgeStr = AgeInput.get()
    Age = int(AgeStr)
    HeightStr = HeightInput.get()
    Height = int(HeightStr)
    WeightStr = WeightInput.get()
    Weight = int(WeightStr)
    Activity = ActivityInput.get()

    ''' Step2. ======== 開始計算 ======== '''

    # ----- 計算BMI
    BMI = Weight / (Height/100) ** 2

    # ----- 計算 TDEE
    if Gender == "生理女":
        TDEE = 9.6*Weight + 1.8*Height - 4.7*Age + 655
    else:  # 男生的 TDEE
        TDEE = 13.7 * Weight + 5.0 * Height - 6.8 * Age + 66

    # ----- 計算每日所需熱量 (CalNeeded)
    # 體重過輕
    if BMI < 18.5:
        if Activity == "低（經常久坐辦公室）":
            CalNeeded = 35 * Weight
        elif Activity == "中（需經常走動）":
            CalNeeded = 40 * Weight
        else:
            CalNeeded = 45 * Weight

    # 體重適中
    elif 18.5 < BMI < 24.9:
        if Activity == "低（經常久坐辦公室）":
            CalNeeded = 30 * Weight
        elif Activity == "中（需經常走動）":
            CalNeeded = 35 * Weight
        else:
            CalNeeded = 40 * Weight

    # 體重過重
    else:
        if Activity == "低（經常久坐辦公室）":
            CalNeeded = 22.5 * Weight
        elif Activity == "中（需經常走動）":
            CalNeeded = 30 * Weight
        else:
            CalNeeded = 35 * Weight

    ''' Step3. ======== 秀出結果(及排列) 在第二頁上 ======== '''

    # ----- BMI 結果
    LabelBMI = Label(Frame2, text='BMI =')  # 再加上過輕或過重的話
    LabelBMI.grid(column=0, row=1)
    #
    LabelBMIResult = Label(Frame2, text=str(BMI))
    LabelBMIResult.grid(column=1, row=1)

    # ----- TDEE 結果
    LabelTDEE = Label(Frame2, text='基礎代謝率 =')
    LabelTDEE.grid(column=0, row=2)

    LabelTDEEResult = Label(Frame2, text=str(TDEE))
    LabelTDEEResult.grid(column=1, row=2)

    # ----- 每日所需熱量 結果
    LabelCal = Label(Frame2, text='每日所需熱量 =')
    LabelCal.grid(column=0, row=3)

    LabelCalResult = Label(Frame2, text=str(CalNeeded))
    LabelCalResult.grid(column=1, row=3)

    # ===== 建議攝取熱量 結果

    ''' ======================================== '''


'''------------------- 基本資訊頁視窗（Frame1） ------------------'''

# =============
LabelOpening = tk.Label(Frame1, text="請填入以下基本資訊")
LabelOpening.grid(column=0, row=0, columnspan=2)


# ============= 性別的下拉式選單
LabelGenderInput = tk.Label(Frame1, text="性別")  # 性別 Label
LabelGenderInput.grid(column=0, row=1)              # Label 位子
GenderInput = ttk.Combobox(
    Frame1, values=["生理男", "生理女"])   # 性別下拉式選單
GenderInput.grid(column=1, row=1)                   # 欄位位子
GenderInput.current(0)                              # 下拉選單預設為男


# ============= 年齡的輸入欄
LabelAgeInput = tk.Label(Frame1, text="年齡")  # 年齡 Label
LabelAgeInput.grid(column=0, row=2)              # Label 位子
AgeInput = Entry(Frame1)                      # 年齡輸入欄位
AgeInput.grid(column=1, row=2)                   # 欄位位子


# ============= 身高的輸入欄
LabelHeightInput = tk.Label(Frame1, text="身高（cm）")  # 身高 Label
LabelHeightInput.grid(column=0, row=3)                   # Label位子
HeightInput = Entry(Frame1)                           # 身高輸入欄位
HeightInput.grid(column=1, row=3)                        # 欄位位子


# ============= 體重的輸入欄
LabelWeightInput = tk.Label(Frame1, text="體重（kg）")  # 體重 Label
LabelWeightInput.grid(column=0, row=4)                   # Label 位子
WeightInput = Entry(Frame1)                           # 輸入體重欄位
WeightInput.grid(column=1, row=4)                        # 欄位位子

# ============= 每日活動量的輸入欄
LabelActivityInput = tk.Label(Frame1, text="每日活動量")  # 每日活動量 Label
LabelActivityInput.grid(column=0, row=5)                   # 每日活動量 Label 位子
ActivityInput = ttk.Combobox(Frame1, values=[
    "低（經常久坐辦公室）",
    "中（需經常走動）",
    "高（需搬運重物之勞力工作）"])   # 活動量下拉式選單
ActivityInput.grid(column=1, row=5)  # 活動量下拉式選單位子
# Activity.current(1)             # 下拉式選單預設活動量為中


# ============= 輸入完成的計算鈕
BasicCount = tk.Button(Frame1, text="開始計算", command=lambda: What2Eat(Frame2))
BasicCount.grid(column=0, row=6, columnspan=2)


'''----------- 結果視窗頁編排 (Frame2) -----------'''

LabelOpening2 = Label(Frame2, text='你可以這樣吃！')
LabelOpening2.grid(column=0, row=0, columnspan=2)

Frame2.mainloop()
