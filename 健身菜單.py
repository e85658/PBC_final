import tkinter as tk
from tkinter import ttk
from tkinter import *
import xlrd  # for reading excel file
import random # to randomly pick from list of exercises

'''-----------開啟新的視窗作為健身菜單的首頁，默認MainWin是我們的大程式首頁-----------'''
SecondWin = tk.Tk()  # 運動菜單的首頁
SecondWin.geometry('400x200')
SecondWin.title("健身菜單")

SecondFrame = Frame(SecondWin)
SecondFrame.place(width=200, height=400)

FirstFrame = Frame(SecondWin)
FirstFrame.place(width=200, height=400)

'''--------------------讀取包含所有健身動作的excel----------------------'''
loc = "C:\\Users\\IVA\\Desktop\\test.xlsx"  # 根據自己的path做更改
AllExercise = xlrd.open_workbook(loc)
SheetIndex = {'強': 0, '中': 1, '弱': 2}
ColIndex = {'腿部': 0, '胸部': 1, '背部': 2}  # 之後補齊7個

'''----------------在新的frame展示推薦給使用者的隨機菜單------------------'''
def Menu(frame):
    frame.tkraise()  # 開啟新frame（即SecondFrame）
    
    TargetPart = BodyParts.get()  # 使用者選擇的肌群
    TargetIntensity = Intensity.get()  # 使用者選擇的運動強度

    sheet = AllExercise.sheet_by_index(SheetIndex[TargetIntensity])  # 根據運動強度開啟的excel分頁
    Exercise = sheet.col_values(ColIndex[TargetPart])  # 根據肌群選擇讀取的column data
    Exercise = Exercise[1:]  # 去掉第一行的header
    RecommendedExercise = random.sample(Exercise, k=4)  # 隨機的演算法
    # print(RecommendedExercise)
    ResultList.delete('0', 'end')  # 要先清空原先output裡有的推薦菜單，因為使用者可能會按‘回到上一頁’來重新選擇肌群&強度
    for i in RecommendedExercise:
        ResultList.insert(0, i)  # 輸出output


def BacktoFirstFrame(frame):  # 回到上一頁的button function
    frame.tkraise()


'''----------------------肌群的下拉式選單---------------------------'''
labelBodyParts = tk.Label(FirstFrame,
                    text = "今天想練哪個部位？")
labelBodyParts.grid(column=0, row=0)  # 肌群label的位置

BodyParts = ttk.Combobox(FirstFrame, 
                            values=[
                                    "腿部", 
                                    "胸部",
                                    "背部",
                                    "腹部",
                                    "肩部",
                                    "手部",
                                    "全身"])

# print(dict(BodyParts))  # 可以看想要改什麼東西（字體、大小、顏色之類的）
BodyParts.grid(column=0, row=1)  # 下拉式選單的位置
BodyParts.current(6)  # 下拉式選單初始show出來的肌群(全身)

# print(BodyParts.current(), BodyParts.get())  # 只是看看初始的肌群是哪一個

'''---------------------運動強度的下拉式選單--------------------------'''
LabelIntensity = tk.Label(FirstFrame,
                    text = "請選擇運動強度")
LabelIntensity.grid(column=0, row=3)  # 運動強度label的位置

Intensity = ttk.Combobox(FirstFrame, 
                            values=[
                                    "強", 
                                    "中",
                                    "弱"])

# print(dict(Intensity))  # 可以看想要改什麼東西（字體、大小、顏色之類的）
Intensity.grid(column=0, row=4)  # 下拉式選單的位置
Intensity.current(1)  # 下拉式選單初始show出來的強度(中)

# print(Intensity.current(), Intensity.get())  # 只是看看初始的強度是哪一個

'''--------------------使用者輸入完畢後的button-------------------------'''
ButtonStart1 = tk.Button(FirstFrame, text = "動起來!", command=lambda:Menu(SecondFrame))
ButtonStart1.grid(column=0, row=7)

# print(dict(ButtonStart1))  # 可以看想要改什麼東西（字體、大小、顏色之類的）

'''----------------進入第二個frame（展示運動菜單的地方）----------------------------'''
LabelMenu = Label(SecondFrame, text='健身菜單')
LabelMenu.grid(column=0, row=0)

ResultList = tk.Listbox(SecondFrame)  # 這裡還要加上gif、語錄、進度bar、倒數時鐘等等
ResultList.place(x=10, y=20, width=380, height=150)

BackButton = tk.Button(SecondFrame, text = "回到上一頁", command=lambda:Menu(FirstFrame))
BackButton.place(x=130, y=170)

SecondWin.mainloop()
