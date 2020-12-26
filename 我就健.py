#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
import xlrd  # for reading excel file
import random # to randomly pick from list of exercises
from PIL import Image  # to play gif file
import tkmacosx  # 為了設定按鈕顏色
from tkmacosx import Button
import tkinter.font as tkFont
import pandas as pd
from PIL import ImageTk

'''------------------ 建立視窗們 -------------------'''
MainWin = tk.Tk()
MainWin.geometry('850x700')
MainWin.title("我就健")

SeventhFrame = Frame(MainWin)  # 今天好想健結果頁
SeventhFrame.place(width=850, height=700)
SeventhFrame["bg"] = "#fbf1e9"

SixthFrame = Frame(MainWin)  # 今天好想健首頁
SixthFrame.place(width=850, height=700)
SixthFrame["bg"] = "#fbf1e9"

FifthFrame = Frame(MainWin)  # 吃得健不健結果頁
FifthFrame.place(width=850, height=700)
FifthFrame["bg"] = "#fbf1e9"

FourthFrame = Frame(MainWin)  # 吃得健不健首頁
FourthFrame.place(width=850, height=700)
FourthFrame["bg"] = "#fbf1e9"

ThirdFrame = Frame(MainWin)  # 看看你多健結果頁
ThirdFrame.place(width=850, height=700)
ThirdFrame["bg"] = "#fbf1e9"

SecondFrame = Frame(MainWin)  # 看看你多健首頁
SecondFrame.place(width=850, height=700)
SecondFrame["bg"] = "#fbf1e9"

FirstFrame = Frame(MainWin)  # 首頁的frame
FirstFrame.place(width=400, height=600)

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝看看你多健＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝#
'''------------------- 看看你多健的基本資訊頁視窗（SecondFrame） ------------------'''
def BMIapp(frame):
    global GenderInput
    global AgeInput
    global HeightInput
    global WeightInput
    global ActivityInput
    global TargetWeightInput
    global DaysInput
    frame.tkraise()

    BackButton = Button(frame, text="←", command=lambda: SwitchFrame(SecondFrame, FirstFrame))
    BackButton.grid(column=0, row=0, sticky='WS')  # 回到上一頁的button

    # ============= 頁面標題
    LabelOpening = tk.Label(SecondFrame, text="看看你多健！", font=('Helvetica', 25), bg="#fbf1e9", fg='#f8872e')
    LabelOpening.grid(column=0, row=1, ipady=20, columnspan=2)

    # ============= 性別的下拉式選單
    LabelGenderInput = tk.Label(SecondFrame, text="性別", fg='#f8872e', bg="#fbf1e9")  # 性別 Label
    LabelGenderInput.grid(column=0, row=2, ipady=5)  # Label 位子
    GenderInput = ttk.Combobox(SecondFrame, values=["生理男", "生理女"])  # 性別下拉式選單
    GenderInput.grid(column=1, row=2)  # 欄位位子
    GenderInput.current(0)  # 下拉選單預設為男

    # ============= 年齡的輸入欄
    LabelAgeInput = tk.Label(SecondFrame, text="年齡", fg='#f8872e', bg="#fbf1e9")  # 年齡 Label
    LabelAgeInput.grid(column=0, row=3, ipady=5)  # Label 位子
    AgeInput = Entry(SecondFrame)  # 年齡輸入欄位
    AgeInput.grid(column=1, row=3)  # 欄位位子

    # ============= 身高的輸入欄
    LabelHeightInput = tk.Label(SecondFrame, text="身高（cm）", fg='#f8872e', bg="#fbf1e9")  # 身高 Label
    LabelHeightInput.grid(column=0, row=4, ipady=5)  # Label位子
    HeightInput = Entry(SecondFrame)  # 身高輸入欄位
    HeightInput.grid(column=1, row=4)  # 欄位位子

    # ============= 體重的輸入欄
    LabelWeightInput = tk.Label(SecondFrame, text="體重（kg）", fg='#f8872e', bg="#fbf1e9")  # 體重 Label
    LabelWeightInput.grid(column=0, row=5, ipady=5)  # Label 位子
    WeightInput = Entry(SecondFrame)  # 輸入體重欄位
    WeightInput.grid(column=1, row=5)  # 欄位位子

    # ============= 每日活動量的輸入欄
    LabelActivityInput = tk.Label(SecondFrame, text="每日活動量", fg='#f8872e', bg="#fbf1e9")  # 每日活動量 Label
    LabelActivityInput.grid(column=0, row=6, ipady=5)  # 每日活動量 Label 位子
    ActivityInput = ttk.Combobox(SecondFrame, values=[
        "低（經常久坐辦公室）",
        "中（需經常走動）",
        "高（需搬運重物之勞力工作）"])  # 活動量下拉式選單
    ActivityInput.grid(column=1, row=6)  # 活動量下拉式選單位子
    ActivityInput.current(1)

    # 加入分隔線
    ttk.Separator(SecondFrame, orient=HORIZONTAL).grid(row=7, columnspan=2, sticky="ew", padx=30, pady=30)

    # ============= 目標體重輸入欄
    LabelTargetWeightInput = tk.Label(SecondFrame, text="期望達到的目標體重", fg='#f8872e', bg="#fbf1e9")  # 目標體重 Label
    LabelTargetWeightInput.grid(column=0, row=8, ipady=5)  # Label 位子
    TargetWeightInput = Entry(SecondFrame)  # 輸入目標體重欄位
    TargetWeightInput.grid(column=1, row=8)  # 欄位位子

    # ============= 期望達到期限輸入欄
    LabelDaysInput = tk.Label(SecondFrame, text="你希望在幾天內達到目標體重", fg='#f8872e', bg="#fbf1e9")  # 目標天數 Label
    LabelDaysInput.grid(column=0, row=9, ipady=5)  # Label 位子
    DaysInput = Entry(SecondFrame)  # 輸入目標天數
    DaysInput.grid(column=1, row=9)  # 欄位位子

    # 加入分隔線
    # ttk.Separator(SecondFrame, orient=HORIZONTAL).grid(row=9, columnspan=2, sticky="ew", padx=30, pady=30)

    # ============= 輸入完成的計算鈕
    BasicCount = Button(SecondFrame, text="看看我多健！", bg='#f8872e', fg="white", bd=3, command=lambda: CheckBlank())
    BasicCount.grid(column=0, row=11, columnspan=2, padx=5, pady=30, ipady=5, sticky="ew")


'''------------------ 檢查有沒有空白資訊，如果空白跳出 messagebox ----------'''
'''------------------ 如果沒有問題就進行 ThirdFrame ---------------------'''

def CheckBlank():
    try:
        Gender = GenderInput.get()
        AgeStr = AgeInput.get()
        Age = int(AgeStr)
        HeightStr = HeightInput.get()
        Height = int(HeightStr)
        WeightStr = WeightInput.get()
        Weight = int(WeightStr)
        Activity = ActivityInput.get()
        TarWeightStr = TargetWeightInput.get()
        TarWeight = int(TarWeightStr)
        TarDaysStr = DaysInput.get()
        TarDays = int(TarDaysStr)

    # 檢查是不是空白的
    except ValueError:
        tk.messagebox.showinfo(title='錯誤', message='留空嗎！？這樣我怎麼算你多健？')
    else:
        if Weight == 0 or Height == 0 or Age == 0:
            tk.messagebox.showinfo(title='錯誤', message='怎麼有 0 呢？難道你是幽靈！？')
        elif TarWeight == 0:
            tk.messagebox.showinfo(title='錯誤', message='目標體重 0？ 你想成仙嗎？')
        elif Weight != TarWeight and TarDays == 0:
            tk.messagebox.showinfo(title='錯誤', message='你想在一夕之間改變體重嗎！？投胎比較快！')
        else:
            What2Eat(ThirdFrame)


'''------------------ 點擊第一頁的「開始計算」 Button 後，要開始做的 Function ------------------'''
'''--------------------------- 抓取第一頁輸入的資料下去做後面所有的計算 -------------------------'''
GenderInput = None
AgeInput = None
HeightInput = None
WeightInput = None
ActivityInput = None
TargetWeightInput = None
DaysInput = None

def What2Eat(frame):
    frame.tkraise()  # 跳出新頁面
    
    ''' Step1. ======== 抓取資料 ======== '''
    global GenderInput
    global AgeInput
    global HeightInput
    global WeightInput
    global ActivityInput
    global TargetWeightInput
    global DaysInput
    
    # try:
    Gender = GenderInput.get()
    AgeStr = AgeInput.get()
    Age = int(AgeStr)
    HeightStr = HeightInput.get()
    Height = int(HeightStr)
    WeightStr = WeightInput.get()
    Weight = int(WeightStr)
    Activity = ActivityInput.get()
    TarWeightStr = TargetWeightInput.get()
    TarWeight = int(TarWeightStr)
    TarDaysStr = DaysInput.get()
    TarDays = int(TarDaysStr)

    ''' Step2. ======== 開始計算 ======== '''

    # ----- 計算BMI
    BMI = Weight / (Height/100) ** 2

    # ----- 計算 女生的TDEE
    if Gender == "生理女":
        TDEE = 9.6*Weight + 1.8*Height - 4.7*Age + 655
    else:  # 男生的 TDEE
        TDEE = 13.7 * Weight + 5.0 * Height - 6.8 * Age + 66

    # ----- 計算每日所需熱量 (CalNeeded)
    # 體重過輕
    if BMI < 18.5:
        if Activity == 1:
            CalNeeded = 35 * Weight
        elif Activity == 2:
            CalNeeded = 40 * Weight
        else:
            CalNeeded = 45 * Weight

    # 體重適中
    elif 18.5 < BMI < 24.9:
        if Activity == "低":
            CalNeeded = 30 * Weight
        elif Activity == "中":
            CalNeeded = 35 * Weight
        else:
            CalNeeded = 40 * Weight

    # 體重過重
    else:
        if Activity == 1:
            CalNeeded = 22.5 * Weight
        elif Activity == 2:
            CalNeeded = 30 * Weight
        else:
            CalNeeded = 35 * Weight

    # ------ 計算如果要減肥應該攝取的熱量
    if Weight == TarWeight and TarDays == 0:
        TarDays = 1
    Cal2Eat = CalNeeded-((Weight-TarWeight)*7700/TarDays)
    if Cal2Eat <= TDEE:  # 如果比基礎代謝率還低
        CalNeeded = TDEE
    elif TDEE < Cal2Eat <= CalNeeded:
        CalNeeded = Cal2Eat

    # ------ 建議每日攝取營養素
    if CalNeeded <= 1200:
        WholeGrains = 1.5
        Protein = 3
        Diary = 1.5
        Vegetable = 3
        Fruit = 2
        Oil = 4
    elif 1200 < CalNeeded <= 1500:
        WholeGrains = 2.5
        Protein = 4
        Diary = 1.5
        Vegetable = 3
        Fruit = 2
        Oil = 4
    elif 1500 < CalNeeded <= 1800:
        WholeGrains = 3
        Protein = 5
        Diary = 1.5
        Vegetable = 3
        Fruit = 2
        Oil = 5
    elif 1800 < CalNeeded <= 2000:
        WholeGrains = 3
        Protein = 6
        Diary = 1.5
        Vegetable = 4
        Fruit = 3
        Oil = 6
    elif 2000 < CalNeeded <= 2200:
        WholeGrains = 3.5
        Protein = 6
        Diary = 1.5
        Vegetable = 4
        Fruit = 3.5
        Oil = 6
    elif 2200 < CalNeeded <= 2500:
        WholeGrains = 4
        Protein = 7
        Diary = 1.5
        Vegetable = 5
        Fruit = 4
        Oil = 7
    else:
        WholeGrains = 4
        Protein = 8
        Diary = 2
        Vegetable = 5
        Fruit = 4
        Oil = 8

    ''' Step3. ======== 秀出結果(及排列)在第二頁上 ======== '''
    BackButton = Button(frame, text="←",
                        command=lambda: SwitchFrame(ThirdFrame, SecondFrame))
    BackButton.grid(column=0, row=0, sticky='WS')  # 回到上一頁的button
    
    HomeButton = Button(frame, text="⌂",
                        command=lambda: SwitchFrame(ThirdFrame, FirstFrame))
    HomeButton.grid(column=1, row=0, sticky='WS')  # 回到首頁的button

    # ------ BMI 結果
    LabelBMI = Label(ThirdFrame, text='BMI =', fg='#f8872e', bg="#fbf1e9")
    LabelBMI.grid(column=0, row=3)

    LabelBMIResult = Label(ThirdFrame, text=round(BMI, 1), fg='#f8872e', bg="#fbf1e9")
    LabelBMIResult.grid(column=1, row=3)
    
    # ------ 再加上過輕或過重的話
    if BMI < 18.5:
        LabelFatorThin = Label(ThirdFrame, text='你現在過輕囉！', bg="#fbf1e9", fg="gray", font=('Helvetica', 10))
        LabelFatorThin.grid(column=1, row=4)
    elif BMI > 24.9:
        LabelFatorThin = Label(ThirdFrame, text='你現在過重囉！', bg="#fbf1e9", fg="gray", font=('Helvetica', 10))
        LabelFatorThin.grid(column=1, row=4)
    else:
        LabelFatorThin = Label(ThirdFrame, text='不錯呦～繼續保持！', bg="#fbf1e9", fg="gray", font=('Helvetica', 10))
        LabelFatorThin.grid(column=1, row=4)

    # ------- 每日所需熱量 結果
    LabelCal = Label(ThirdFrame, text='你應攝取 =', fg='#f8872e', bg="#fbf1e9")
    LabelCal.grid(column=0, row=5)

    LabelCalResult = Label(ThirdFrame, text=str(round(CalNeeded, 1))+' 大卡', fg='#f8872e', bg="#fbf1e9")
    LabelCalResult.grid(column=1, row=5)

    LabelOpening2 = Label(ThirdFrame, text='這樣吃最健！', font=('Helvetica', 25), fg='#f8872e', bg="#fbf1e9")
    LabelOpening2.grid(column=0, row=6, columnspan=2, pady=20)
    
    # ------- 建議每日攝取營養素 結果
    LabelWholeGrains = Label(ThirdFrame, text='全榖雜糧類=', fg='#f8872e', bg="#fbf1e9")
    LabelWholeGrains.grid(column=0, row=8)

    LabelWholeGrainsResult = Label(ThirdFrame, text=str(WholeGrains)+' 碗', fg='#f8872e', bg="#fbf1e9")
    LabelWholeGrainsResult.grid(column=1, row=8)

    LabelProtein = Label(ThirdFrame, text='蛋豆魚肉類=', fg='#f8872e', bg="#fbf1e9")
    LabelProtein.grid(column=0, row=9)

    LabelProteinResult = Label(ThirdFrame, text=str(Protein)+' 份', fg='#f8872e', bg="#fbf1e9")
    LabelProteinResult.grid(column=1, row=9)

    LabelDiary = Label(ThirdFrame, text='乳品類=', fg='#f8872e', bg="#fbf1e9")
    LabelDiary.grid(column=0, row=10)

    LabelDiaryResult = Label(ThirdFrame, text=str(Diary)+' 杯', fg='#f8872e', bg="#fbf1e9")
    LabelDiaryResult.grid(column=1, row=10)

    LabelVegetable = Label(ThirdFrame, text='蔬菜類=', fg='#f8872e', bg="#fbf1e9")
    LabelVegetable.grid(column=0, row=11)

    LabelVegetableResult = Label(ThirdFrame, text=str(Vegetable)+' 份', fg='#f8872e', bg="#fbf1e9")
    LabelVegetableResult.grid(column=1, row=11)

    LabelFruit = Label(ThirdFrame, text='水果類=', fg='#f8872e', bg="#fbf1e9")
    LabelFruit.grid(column=0, row=12)

    LabelFruitResult = Label(ThirdFrame, text=str(Fruit)+' 份', fg='#f8872e', bg="#fbf1e9")
    LabelFruitResult.grid(column=1, row=12)

    LabelOil = Label(ThirdFrame, text='油脂與堅果種子類=', fg='#f8872e', bg="#fbf1e9")
    LabelOil.grid(column=0, row=13)

    LabelOilResult = Label(ThirdFrame, text=str(Oil)+' 份', fg='#f8872e', bg="#fbf1e9")
    LabelOilResult.grid(column=1, row=13)

    # 加入分隔線
    ttk.Separator(ThirdFrame, orient=HORIZONTAL).grid(row=14, columnspan=2, sticky="ew", padx=30, pady=30)

    # -------- 建議每日攝取營養素 定義
    LabelNulDef = Label(ThirdFrame, text='*六大營養素代換份量*', fg='#f8872e', bg="#fbf1e9")
    LabelNulDef.grid(column=0, row=15, columnspan=2, sticky=N+S)

    LabelWholeGrainsDef = Label(ThirdFrame, text='全榖雜糧類 1 碗：約 160-200 公克', fg='#f8872e', bg="#fbf1e9")
    LabelWholeGrainsDef.grid(column=0, row=16, columnspan=2, sticky=N+S)

    LabelProteinDef = Label(ThirdFrame, text='蛋豆魚肉類 1 份：約 37.5 公克', fg='#f8872e', bg="#fbf1e9")
    LabelProteinDef.grid(column=0, row=17, columnspan=2, sticky=N+S)

    LabelDiaryDef = Label(ThirdFrame, text='乳品類 1 杯：約 240 毫升', fg='#f8872e', bg="#fbf1e9")
    LabelDiaryDef.grid(column=0, row=18, columnspan=2, sticky=N+S)

    LabelVegetableDef = Label(ThirdFrame, text='蔬菜類 1 份：約 100 公克', fg='#f8872e', bg="#fbf1e9")
    LabelVegetableDef.grid(column=0, row=19, columnspan=2, sticky=N+S)

    LabelFruitDef = Label(ThirdFrame, text='水果類 1 份：約 80-120 公克', fg='#f8872e', bg="#fbf1e9")
    LabelFruitDef.grid(column=0, row=20, columnspan=2, sticky=N+S)

    LabelFruitDef = Label(ThirdFrame, text='油脂與堅果種子類 1 份：約 5 公克', fg='#f8872e', bg="#fbf1e9")
    LabelFruitDef.grid(column=0, row=21, columnspan=2, sticky=N+S)


def SwitchFrame(currframe, frame):  # 回到上一頁的button function
    for widget in currframe.winfo_children():
        widget.destroy()  # 將此視窗內的所有widget全部毀掉
    currframe.pack_forget()  # unpack現在的frame
    frame.tkraise()


#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝吃的健不健＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝#
'''-------------------------------- 參數設定 -----------------------------------'''
name_len = 65
data_len = 30
foodname = "食物".center(name_len-len("食物".encode('utf8')))
kcal = "熱量(kcal)".center(data_len-len("熱量(kcal)".encode('utf8')))
protein = "蛋白質(g)".center(data_len-len("蛋白質(g)".encode('utf8')))
fat = "脂肪(g)".center(data_len-len("脂肪(g)".encode('utf8')))
carbohydrate = "碳水化合物(g)".center(data_len-len("碳水化合物(g)".encode('utf8')))
sodium = "鈉(mg)".center(data_len-len("鈉(mg)".encode('utf8')))
line1 = "==="*29
line2 = "------"*21
lb_width = 90
lb_height = 25

'''-------------------------------- 導入圖庫以及清單 -----------------------------------'''
# 這邊要改路徑！！！！ PATHPATH
imageOmelette1 = ImageTk.PhotoImage(file="omelette.png")
imageRice1 = ImageTk.PhotoImage(file="rice.png")
imageFastfood1 = ImageTk.PhotoImage(file="fastfood.png")
imagePasta1 = ImageTk.PhotoImage(file="pasta.png")
imageNoodles1 = ImageTk.PhotoImage(file="noodles.png")
imageFruits1 = ImageTk.PhotoImage(file="fruits.png")
imageCake1 = ImageTk.PhotoImage(file="cake.png")
imageDrink1 = ImageTk.PhotoImage(file="drink.png")

FoodImage = {"早點": imageOmelette1, "中式": imageRice1,
             "速食": imageFastfood1, "義式": imagePasta1,
             "日式": imageNoodles1, "水果": imageFruits1,
             "甜點": imageCake1, "飲料": imageDrink1}

# 用mac的之後把 "C：\\...food\\" 都刪掉才能讀到excel檔 PATHPATH
# FoodList = {"早點": '早點.xlsx', "中式": '中式.xlsx',
#             "速食": '速食.xlsx', "義式": '義式.xlsx',
#             "日式": '日式.xlsx', "水果": '水果.xlsx',
#             "甜點": '點心.xlsx', "飲料": '飲料.xlsx'}
FoodList = {"早點": '/Users/kaipingwang/Desktop/GitHub/PBC_final/早點.xls', "中式": '/Users/kaipingwang/Desktop/GitHub/PBC_final/中式.xls',
            "速食": '/Users/kaipingwang/Desktop/GitHub/PBC_final/速食.xls', "義式": '/Users/kaipingwang/Desktop/GitHub/PBC_final/義式.xls',
            "日式": '/Users/kaipingwang/Desktop/GitHub/PBC_final/日式.xls', "水果": '/Users/kaipingwang/Desktop/GitHub/PBC_final/水果.xls',
            "甜點": '/Users/kaipingwang/Desktop/GitHub/PBC_final/點心.xls', "飲料": '/Users/kaipingwang/Desktop/GitHub/PBC_final/飲料.xls'}


'''--------------------------- 主頁面(FourthFrame)設定 ----------------------------'''


def FOODapp(frame):
    frame.tkraise()

    BackButton = tk.Button(frame, text="←", command=lambda: SwitchFrame(FourthFrame, FirstFrame))
    BackButton.grid(column=0, row=0, sticky='WS')  # 回到上一頁的button

    # 字體
    f1 = tkFont.Font(size=40, family="Helvetica")
    f2 = tkFont.Font(size=15, family="Helvetica")

    # 標題
    lalNun1 = tk.Label(FourthFrame, text="吃得健不健？", font='f1', bg="#fbf1e9", fg='#f8872e')
    lalNun1.grid(column=0, row=1, columnspan=4, padx=300, pady=10, sticky=tk.NE + tk.SW)

    # imageSearch = ImageTk.PhotoImage(file = "search1.png")
    # btnNum1 = tk.Label(FourthFrame, image = imageSearch)
    # btnNum1.grid(column = 0,row = 1, padx= 50, sticky = tk.W)

    # lalNun2 = tk.Label(FourthFrame, text = "選擇食物類別 : ", font = f2, bg="#fbf1e9", fg='#f8872e')
    # lalNun2.grid(column = 0,row = 1, padx= 300, sticky = tk.NW)

    # 個類別按鈕
    btnNumA = tk.Label(FourthFrame)
    btnNumA.grid(column=0, row=3)

    # PATHPATH 536-574
    # imageOmelette = ImageTk.PhotoImage(file = "早點1.png")
    # 把 text='Breafast' 用 image = imageOmelette 取代
    btnNum1 = tk.Button(FourthFrame, text='Breakfast', command=lambda: FoodCalories("早點"))
    btnNum1.grid(column=0, row=2, padx=160, sticky=tk.W)

    # imageRice = ImageTk.PhotoImage(file = "中式1.png")
    # image = imageRice
    btnNum2 = tk.Button(FourthFrame, text='Rice', command=lambda: FoodCalories("中式"))
    btnNum2.grid(column=1, row=2, sticky=tk.W)

    # imageFastfood = ImageTk.PhotoImage(file = "速食1.png")
    # image = imageFastfood
    btnNum3 = tk.Button(FourthFrame, text='Fastfood', command=lambda: FoodCalories("速食"))
    btnNum3.grid(column=0, row=3, padx=160, pady=15, sticky=tk.W)

    # imagePasta = ImageTk.PhotoImage(file = "義式1.png")
    # image = imagePasta
    btnNum4 = tk.Button(FourthFrame, text='Pasta', command=lambda: FoodCalories("義式"))
    btnNum4.grid(column=1, row=3, pady=15, sticky=tk.W)

    # imageNoodles = ImageTk.PhotoImage(file = "日式1.png")
    # image = imageNoodles
    btnNum5 = tk.Button(FourthFrame, text='Japanese', command=lambda: FoodCalories("日式"))
    btnNum5.grid(column=0, row=4, padx=160, pady=15, sticky=tk.W)

    # imageFruits = ImageTk.PhotoImage(file = "水果1.png")
    # image = imageFruits
    btnNum6 = tk.Button(FourthFrame, text='Fruits', command=lambda: FoodCalories("水果"))
    btnNum6.grid(column=1, row=4, pady=15, sticky=tk.W)

    # imageCake = ImageTk.PhotoImage(file = "點心1.png")
    # image = imageCake
    btnNum7 = tk.Button(FourthFrame, text='Cake', command=lambda: FoodCalories("甜點"))
    btnNum7.grid(column=0, row=5, padx=160, pady=15, sticky=tk.W)

    # imageDrink = ImageTk.PhotoImage(file = "飲品1.png")
    # image = imageDrink
    btnNum8 = tk.Button(FourthFrame, text='Drink', command=lambda: FoodCalories("飲料"))
    btnNum8.grid(column=1, row=5, pady=15, sticky=tk.W)

'''--------------------- 次頁面(FifthFrame)設定 ---------------------'''


# 早餐按鈕按下後的頁面設定
def FoodCalories(FoodCategory):   
    global imageOmelette1
    global imageRice1
    global imageFastfood1
    global imagePasta1
    global imageNoodles1
    global imageFruits1
    global imageCake1
    global imageDrink1
    FifthFrame.tkraise()

    # 回到上一頁的button
    BackButton = tk.Button(FifthFrame, text="←", command=lambda: SwitchFrame(FifthFrame, FourthFrame))
    BackButton.grid(column=0, row=0, sticky='WS')

    # 回到首頁的button
    HomeButton = tk.Button(FifthFrame, text="⌂", command=lambda: SwitchFrame(FifthFrame, FirstFrame))
    HomeButton.grid(column=1, row=0, sticky='WS')
    
    blankLabel = tk.Label(FifthFrame)
    blankLabel.grid(row = 0)
    titlePic = tk.Label(FifthFrame, image=FoodImage[FoodCategory])
    titlePic.grid(column = 0,row = 1, columnspan = 3, sticky = tk.E)
    
    titleText = tk.Label(FifthFrame, text=FoodCategory, font = 'f1', bg="#fbf1e9", fg='#f8872e')
    titleText.grid(column = 3, row = 1, columnspan = 3, sticky = tk.SW)
    
    file = FoodList[FoodCategory]
    dataframe = pd.read_excel(file)
    set_data_with_scrollbar(dataframe)


# 傳入所要excel檔案中資料，並用scrollbar顯示出來
def set_data_with_scrollbar(dataframe):
    index = tk.Label(FifthFrame, 
                     text=foodname+kcal+protein+fat+carbohydrate+sodium,
                     bg="#f8872e",
                     fg="white")
    index.grid(column=0, row=2, columnspan=6, padx=7, sticky=tk.W+E)
    
    data = tk.Label(FifthFrame)
    sb = Scrollbar(data)
    sb.pack(side=RIGHT, fill=Y)
    lb = Listbox(data, yscrollcommand= sb.set, width=lb_width, height=lb_height)    
    lb.insert(END, "")
    for i in range(len(dataframe)):
        str_data = ""
        for j in range(6):
            gap = len(str(dataframe.iloc[i, j]).encode('utf8'))
            if j == 0:
                str_data += str(dataframe.iloc[i, j]).center(name_len-gap)
            else:
                str_data += str(dataframe.iloc[i, j]).center(data_len-2-gap)
        lb.insert(END, str_data)
        if i == len(dataframe)-1:
            lb.insert(END, "")
        else:
            lb.insert(END, line2)
    lb.pack(side=RIGHT)
    sb.config(command=lb.yview)
    data.grid(column=0, row=3, columnspan=6, padx=7, sticky=tk.NE + tk.SW)


#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝今天好想健＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝#
'''-----------------------------宣告元件們-----------------------------'''
alarm_id = None
paused = False  # 是否有按暫停鍵
starttime = 60  # 從1分鐘開始倒數計時
BodyParts = None
Intensity = None

def WORKOUTapp(frame):
    frame.tkraise()
    
    BackButton = tk.Button(frame, text="←", width=5, height=1,
                        command=lambda: SwitchFrame(SixthFrame, FirstFrame))
    BackButton.grid(column=0, row=0, sticky='WS')  # 回到上一頁的button
    
    '''----------------------今天好想健title---------------------------'''
    labelTitle3 = tk.Label(SixthFrame, text = "今天好想健！", font=('Helvetica', 25), bg="#fbf1e9", fg='#f8872e')
    labelTitle3.grid(column=0, row=1, ipady=20)


    '''----------------------肌群的下拉式選單---------------------------'''
    global BodyParts
    labelBodyParts = tk.Label(SixthFrame,
                        text = "選擇想健的部位", fg='#f8872e', bg="#fbf1e9")
    labelBodyParts.grid(column=0, row=2, ipady=5)  # 肌群label的位置

    BodyParts = ttk.Combobox(SixthFrame,
                                values=[
                                        "腿部",
                                        "胸部",
                                        "背部",
                                        "腹部",
                                        "肩部",
                                        "手部",
                                        "全身"])

    # print(dict(BodyParts))  # 可以看想要改什麼東西（字體、大小、顏色之類的）
    BodyParts.grid(column=0, row=3)  # 下拉式選單的位置
    BodyParts.current(6)  # 下拉式選單初始show出來的肌群(全身)

    # print(BodyParts.current(), BodyParts.get())  # 只是看看初始的肌群是哪一個

    '''---------------------運動強度的下拉式選單--------------------------'''
    global Intensity
    LabelIntensity = tk.Label(SixthFrame, text="選擇想健的強度", fg='#f8872e', bg="#fbf1e9")
    LabelIntensity.grid(column=0, row=5, ipady=5)  # 運動強度label的位置

    Intensity = ttk.Combobox(SixthFrame,
                                values=[
                                        "強",
                                        "中",
                                        "弱"])

    # print(dict(Intensity))  # 可以看想要改什麼東西（字體、大小、顏色之類的）
    Intensity.grid(column=0, row=6)  # 下拉式選單的位置
    Intensity.current(1)  # 下拉式選單初始show出來的強度(中)

    # print(Intensity.current(), Intensity.get())  # 只是看看初始的強度是哪一個

    '''--------------------使用者輸入完畢後的button-------------------------'''
    ButtonStart1 = tk.Button(SixthFrame, text="健起來!", bg='#f8872e', fg="black", bd=3, command=lambda: Menu(SeventhFrame))
    ButtonStart1.grid(column=0, row=8, columnspan=2, padx=5, pady=30, ipady=5, sticky="ew")

    # print(dict(ButtonStart1))  # 可以看想要改什麼東西（字體、大小、顏色之類的）

'''--------------------讀取包含所有健身動作的excel----------------------'''
# loc = "C:\\Users\\IVA\\Desktop\\exercise.xlsx"  # PATHPATH
loc = '/Users/kaipingwang/Desktop/GitHub/PBC_final/exercise.xls'
AllExercise = xlrd.open_workbook(loc)  # 開啟excel檔案
SheetIndex = {'強': 0, '中': 1, '弱': 2}
ColIndex = {'腿部': 0, '胸部': 1, '背部': 2, '腹部': 3, '肩部': 4, '手部': 5, '全身': 6}

'''--------------------讀取語錄txt----------------------'''
# with open('C:\\Users\\IVA\\Desktop\\語錄們.txt', 'r', encoding='UTF-8') as file:  # PATHPATH
with open('/Users/kaipingwang/Desktop/GitHub/PBC_final/語錄們.txt', 'r', encoding='UTF-8') as file:  # 將語錄放進lines清單中
    lines = []
    for line in file:  # 把語錄放入list中
        line = line.strip('\n')
        lines.append(line)

LineNumber = 0

'''----------------在新的frame展示推薦給使用者的隨機菜單------------------'''


def Menu(frame):
    '''----------------------隨機健身菜單首頁-------------------------'''
    global RecommendedExercise  # 從global叫回隨機健身菜單
    global BodyParts
    global Intensity
    frame.tkraise()  # 開啟新frame（即SecondFrame）

    # 回到上一頁的button
    BackButton = tk.Button(frame, text="←", width=5, height=1, command=lambda: SwitchFrame(SeventhFrame, SixthFrame))
    BackButton.grid(column=0, row=0, sticky='WS')

    # 回到首頁的button
    HomeButton = tk.Button(frame, text="⌂", width=5, height=1, command=lambda: SwitchFrame(SeventhFrame, FirstFrame))
    HomeButton.grid(column=1, row=0, sticky='WS')
    
    TargetPart = BodyParts.get()  # 使用者選擇的肌群
    TargetIntensity = Intensity.get()  # 使用者選擇的運動強度

    sheet = AllExercise.sheet_by_index(SheetIndex[TargetIntensity])  # 根據運動強度開啟的excel分頁
    Exercise = sheet.col_values(ColIndex[TargetPart])  # 根據肌群選擇讀取的column data
    Exercise = Exercise[1:]  # 去掉第一行的header
    RecommendedExercise = random.sample(Exercise, k=4)  # 隨機的演算法算出四個運動
    
    LabelMenu = Label(frame, text='這樣動最健！', font=('Helvetica', 25), bg="#fbf1e9", fg='#f8872e')  # 隨機菜單名稱
    LabelMenu.grid(column=0, row=3, ipady=20)
    
    WorkoutTips = Label(frame, 
                        text='每個動作做一分鐘，一個動作做兩組，\n 組間休息15秒，總共加起來就是10分鐘嘍！', fg='#f8872e', bg="#fbf1e9")
    WorkoutTips.grid(column=0, row=4, ipady=5)
    
    FirstButton = tk.Button(frame, text = str(RecommendedExercise[0]), command=lambda :PlayGif(0))
    FirstButton.grid(column=0, row=6, ipady=5)  # 第一個動作的button

    SecondButton = tk.Button(frame, text = str(RecommendedExercise[1]), command=lambda :PlayGif(1))
    SecondButton.grid(column=0, row=8, ipady=5)  # 第二個動作的button
    
    ThirdButton = tk.Button(frame, text = str(RecommendedExercise[2]), command=lambda :PlayGif(2))
    ThirdButton.grid(column=0, row=10, ipady=5)  # 第三個動作的button
    
    FourthButton = tk.Button(frame, text = str(RecommendedExercise[3]), command=lambda :PlayGif(3))
    FourthButton.grid(column=0, row=12, ipady=5)  # 第四個動作的button


RecommendedExercise = []


# 回到上一頁的button function
def SwitchFrame(currframe, frame):
    for widget in currframe.winfo_children():
       widget.destroy()  # 將此視窗內的所有widget全部毀掉
    
    currframe.pack_forget()  # unpack現在的frame
    
    frame.tkraise()

def PlayGif(i):
    '''----------------------跳出第三個視窗（play GIF）-------------------------'''
    GifWin = tk.Toplevel(MainWin)  # 打開新的視窗
    GifWin.geometry('1000x600')
    GifWin.title(str(RecommendedExercise[i]))
    GifWin["bg"] = "#fbf1e9"

    '''----------------------開始倒數計時-------------------------'''
    labelvariable = StringVar()
    labelvariable.set("01:00")  # 螢幕顯示起始時間

    countdown = tk.Label(GifWin, textvariable = labelvariable,font=('Helvetica',50), bg="#fbf1e9")  # 顯示時間的label
    countdown.pack()
    
    global paused  # 從global叫出暫停
    global alarm_id
    global startTime
        
    if alarm_id is not None:
        GifWin.after_cancel(alarm_id)
        alarm_id = None
        paused = True

    '''----------------------gif的圖片切分-------------------------'''
    GifFile = '/Users/kaipingwang/Desktop/GitHub/PBC_final'  # PATHPATH
    GifFile = RecommendedExercise[i]
    GifFile += '.gif'
    # GifFile = RecommendedExercise[i] + '.gif'
    info = Image.open(GifFile)
    frames = info.n_frames
    im = [tk.PhotoImage(file=GifFile,format='gif -index %i' %(i)) for i in range(frames)]
    
    gif_label = tk.Label(GifWin, image=im[0])
    gif_label.pack()
    
    quote = tk.Label(GifWin, text='預備備......開始！', bg="#fbf1e9")
    quote.pack()

    quo = None
    anim = None
    count = 0

    '''----------------------開始所有function的function-------------------------'''
    def StartEverything(count):
        global paused
        global alarm_id
        global startTime

        '''----------------------時間開始倒數-------------------------'''
        paused = False
        if alarm_id is None:
            Countdown(starttime)

        '''----------------------GIF開始播放-------------------------'''
        def gifplayer(count):
            global anim
            im2 = im[count]
            gif_label.configure(image=im2)

            count += 1
            if count == frames:
                count = 0

            anim = GifWin.after(50, lambda :gifplayer(count))

        '''----------------------語錄開始播放-------------------------'''
        def RunQuote():
            global lines
            global LineNumber
            global quo
            if LineNumber < len(lines)-1:
                quote.configure(text=lines[LineNumber])
                LineNumber += 1
            elif LineNumber == len(lines)-1:
                quote.configure(text=lines[LineNumber])
                LineNumber = 0
            quo = GifWin.after(3000, RunQuote)

        gifplayer(count)
        RunQuote()

    '''----------------------暫停所有function的function-------------------------'''
    def StopEverything():
        global anim
        global paused
        global alarm_id

        '''----------------------GIF停止播放-------------------------'''
        GifWin.after_cancel(anim)

        '''----------------------時間停止倒數-------------------------'''
        if alarm_id is not None:
            paused = True

        '''----------------------語錄停止播放-------------------------'''
        global quo
        GifWin.after_cancel(quo)


    '''-----------------------倒數計時的function-------------------------'''
    def Countdown(timeInSeconds, start=True):
        global paused
        global alarm_id
        global startTime
        
        if start:
            starttime = timeInSeconds
        if paused:
            alarm_id = GifWin.after(1000, Countdown, timeInSeconds, False)
        else:
            if timeInSeconds >= 0:
                mins, secs = divmod(timeInSeconds, 60)
                timeformat = "{0:02d}:{1:02d}".format(mins, secs)
                labelvariable.set(timeformat)
                alarm_id = GifWin.after(1000, Countdown, timeInSeconds-1, False)
            elif timeInSeconds == -1:
                StopEverything()
                tk.messagebox.showinfo(title='我就健!', message='恭喜完成一組！休息15秒再繼續健！')

    '''----------------------所有按鈕的建置-------------------------'''
    # Start Button
    start = tk.Button(GifWin, text='▶', width=10, height=2, command=lambda: StartEverything(count))
    start.pack()
    
    # Stop Button
    stop = tk.Button(GifWin, text='| |', width=10, height=2, command=lambda: StopEverything())
    stop.pack()


#————————————————————————-———————————首頁設計————————————————————————————————————————————
MainTitleLbl = tk.Label(FirstFrame, text="我就健！")
MainTitleLbl.pack()

BMIappBtn = tk.Button(FirstFrame,
                      text="看看你多健!\nBMI與每日應攝取熱量計算",
                      height=5,
                      width=20,
                      command=lambda: BMIapp(SecondFrame))
BMIappBtn.pack()

FOODappBtn = tk.Button(FirstFrame,
                       text="吃得健不健？\n常見食物熱量表",
                       height=5,
                       width=20,
                       command=lambda: FOODapp(FourthFrame))
FOODappBtn.pack()

WORKOUTappBtn = tk.Button(FirstFrame,
                          text="今天好想健！\n居家運動推薦",
                          height=5,
                          width=20,
                          command=lambda: WORKOUTapp(SixthFrame))
WORKOUTappBtn.pack()

MainWin.mainloop()
