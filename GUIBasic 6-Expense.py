#GUI Basic 2 - Expense
from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime


days={
	'Mon':'จันทร์',
	'Tue':'อังคาร',
	'Wed':'พุธ',
	'Thu':'พฤหัสบดี',
	'Fri':'ศุกร์',
	'Sat':'เสาร์',
	'Sun':'อาทิตย์'}

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย By Tim')
GUI.geometry('800x900+1100+0') #ขนาดกว้าง x, ขนาดกว้าง y + ห่างจากจอแกน x + ห่างจากจอแกน y

#B1 = Button(GUI,text=('Hello')) #ประกาศว่า B1 คือปุ่มชื่อ hello
#B1.pack() #ใส่ B1 เข้าไปใน GUI หลักเริม่จากบนสุดและจัดตำแหน่งกลาง
#B1.pack(ipadx=50,ipady=50)#ipadx กำหนดขนาดปุ่มแกน x,ipadY กำหนดขนาดปุ่มแกน Y 

### MENU ###
menubar = Menu(GUI)
GUI.config(menu = menubar)

#File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File', menu = filemenu)
filemenu.add_command(label = 'Import CSV')
filemenu.add_command(label = 'Export to Google sheet')
#Help menu
def About():
	messagebox.showinfo('About', 'สวัสดีครับ\nขอ')


helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help', menu = helpmenu)
helpmenu.add_command(label = 'About', command = About)
#Donate menu
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate', menu = donatemenu)





Tab = ttk.Notebook(GUI)
#T1 = Frame(Tab,width=400,height=400)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)

icon_t1=PhotoImage(file='v_expense.png')  #.sunsample(2) ย่อรูป
icon_t2=PhotoImage(file='v_expense_list.png')

Tab.add(T1, text=f'{"เพิ่มค่าใช้จ่าย":^{50}}',image=icon_t1,compound='top')
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด":^{50}}',image=icon_t2,compound='top')

F1=Frame(T1)
#F1=ttk.LabelFrame(GUI,text='test')
#F1.place(x=20,y=50)
F1.pack()

def Save(event=None):
	expense = v_expense.get() #ดึงมาจาก v_expense= StringVar()
	price = v_price.get()
	num = v_num.get()
	total = float(num)*float(price)
	

	if expense == '':
		print('No data')
		messagebox.showwarning('ผิดพลาด','กรุณากรอกข้อมูลรายการ')
		return
	elif price == '':
		messagebox.showwarning('ผิดพลาด','กรุณากรอกข้อมูลราคา')
		return
	elif num == '':
		messagebox.showwarning('ผิดพลาด','กรุณากรอกข้อมูลจำนวน')
		return

	try:
		print('รายการ: {} ราคา {} บาท'.format(expense,price))
		print('  จำนวน: {} ราคาทั้งหมด {} บาท'.format(num,total))
		text =	'รายการ: {} ราคา {} บาท\n'.format(expense,price)
		text = text + '  จำนวน: {} ราคาทั้งหมด {} บาท'.format(num,total)
		v_result.set(text)
		clearData()
	
		today = datetime.now().strftime('%a') #แปลง วันให้เป็นภาษาไทย
		stamp = datetime.now()
		dt = stamp.strftime('%Y-%m-%d %H:%M:%S')#.format(days[today])) #strftime กำหนดรูปแบบเวลา
		transactionid = stamp.strftime('%Y%m%d%H%M%S%f')
		dt = days[today] + '-' + dt


		#บันทึกข้อมูลลง csv 
		with open('savedata.csv', 'a', encoding='utf-8', newline='') as f: 
			#with สั่งเปิดไล์แล้วปิดอัตโนมัติ
			#'a' การบันทึกข้อมูลเพิ่มเติมจากของเก่า 'w'เขียนข้อมูลไฟล์นั้นใหม่ทั้งหมด
			#encoding='utf-8' ทำให้สามารถเซฟภาษาไทย
			#newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
			fw = csv.writer(f) #สร้างฟังก์ชั่นสำหรับเขียนข้อมูล
			#data=[expense,price,num,total,dt]
			data=[transactionid,dt,expense,price,num,total]
			fw.writerow(data)
		
		update_table()

	except:
		print('ErrOr')
		#messagebox.showerror('ผิดพลาด','ใส่ตัวเลขอย่างเดียว')
		#messagebox.showwarning('ผิดพลาด','ใส่ตัวเลขอย่างเดียว')
		messagebox.showinfo('ผิดพลาด','ใส่ตัวเลขอย่างเดียว')
		clearData()

def clearData():
	v_expense.set('') #กำหนด v_expense ให้เป็นช่องว่าง
	v_price.set('')
	v_num.set('')
	E1.focus()



#ทำให้กด enter
GUI.bind('<Return>',Save) #ต้องเพิ่ม ใน def Save(event=None)


FONT1=(None,20) #กำหนด font โดยกำหนดชื่อ font ตามด้วยขนาด
FONT2=(None,16)

#========IMAGE=============
main_icon = PhotoImage(file='bg_sex.png').subsample(3)
Mainicon = Label(F1,image=main_icon)
Mainicon.pack()



# --------text1
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense= StringVar() #stringVar เป็นตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1=ttk.Entry(F1,textvariable=v_expense,font=FONT1) #entry เป็นช่องสำหรับกรอกข้อมูล
E1.pack()
E1.focus()
# --------End text1

# --------text2
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT2).pack()
v_price= StringVar() #stringVar เป็นตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2=ttk.Entry(F1,textvariable=v_price,font=FONT2) 
E2.pack()
# --------End text2

# --------text2
L = ttk.Label(F1,text='จำนวน (ครั้ง)',font=FONT2).pack()
v_num= StringVar() #stringVar เป็นตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3=ttk.Entry(F1,textvariable=v_num,font=FONT2) 
E3.pack()
# --------End text2

#B2 = ttk.Button(F1,text=('Save'),command=Save) #ประกาศว่า B2 คือปุ่มชื่อ hello เปลี่ยนเป็นปุ่มอีกแบบโดยใช้ ttk.
#B2.pack(ipadx=50,ipady=50)

icon_b1=PhotoImage(file='b_save.png')

B2 = ttk.Button(F1,text=f'{"Save":>{10}}',image=icon_b1,compound='left',command=Save)
B2.pack(ipadx=50,ipady=20,pady=20)

v_result=StringVar()
v_result.set('------------ผลลัพท์----------')
result = ttk.Label(F1, textvariable=v_result,font=(None,15),foreground='green')
result.pack(pady=20)



################ TAB2 ###############


def read_csv():
	with open('savedata.csv', newline='', encoding='utf-8') as f:		
		fr = csv.reader(f)
		data = list(fr)
	return data


'''#แสดงข้อมูลเป็นข้อความ
def update_record():
	getdata = read_csv()
	v_allrecord.set('')
	text = ('')
	for d in getdata:
		txt = '{}---{}---{}---{}---{}\n'.format(d[0], d[1], d[2] ,d[3], d[4])
		text = text + txt

	v_allrecord.set(text)

v_allrecord = StringVar()
v_allrecord.set('-------- All record -----------')
Allrecord  = ttk.Label(T2,textvariable=v_allrecord,font=FONT2,foreground='green')
Allrecord.pack()
'''#จบแสดงข้อมูลเป็นข้อความ

L = ttk.Label(T2,text='ตารางแสดงผลลัพท์',font=FONT1).pack(pady=20)


header = ['รหัสรายการ', 'วัน-เวลา', 'รายการ', 'ค่าใช้จ่าย', 'จำนวน', 'รวม']
resulttable = ttk.Treeview(T2, column=header, show='headings', height=20)
resulttable.pack()

#for i in range(len(header)):
#	resulttable.heading(header[i], text=header[i])


for h in header:
	resulttable.heading(h, text=h)


#resulttable.column('วัน-เวลา',width=10)
#resulttable.column(header[0],width=10)
headerwidth = [150, 150, 170, 80, 80, 80]
for h,w in zip(header, headerwidth): #zip คือการจับคู่
	resulttable.column(h, width=w)

#ใส่ข้อมูลเอง
#resulttable.insert('', 'end', value=['จันทร์', 'Nat', 1000, 20, 20000]) #end ใส่ไว้สุดท้าย
#resulttable.insert('', 0, value=['จันทร์', 'Police', 1000, 20, 20000]) #0 ใส่ index แรก

alltransaction = {}


def UpdateCSV():
	with open('savedata.csv', 'w', newline='', encoding='utf-8') as f:		
		fw = csv.writer(f)
		#print('aaa ', alltransaction.value())
		#เตรียมข้อมูล alltransaction ให้เป็น list
		 
		data = list(alltransaction.values())
		fw.writerows(data) # multiple line from nested list
		print('TABLE was updated')
		update_table()

	

def DeleteRecord(event = None):
	check = messagebox.askyesno('Confirm?', 'คุณต้องการลบข้อมูลใช่หรือไม่')
	print('yes/no', check)

	if check == True:
		print('delete')
		select = resulttable.selection()
		print(select)
		data = resulttable.item(select)
		data = data['values']
		transactionid = data[0]
		print(transactionid)
		del alltransaction[str(transactionid)] #deleta data in dict
		UpdateCSV()
		update_table()
	else:
		print('cancle')

BDelete = ttk.Button(T2, text='delete', command=DeleteRecord)
BDelete.place(x=50, y=550)

resulttable.bind('<Delete>', DeleteRecord)


def update_table():
	resulttable.delete(*resulttable.get_children())
	try:
		data = read_csv()
		for d in data:
			#create transaction data
			alltransaction[d[0]] = d # d[0] = transactionid
			resulttable.insert('', 0, value=d)
			print('all transaction', alltransaction)

	except:
		print('no file')
		#messagebox.showinfo('ไม่มีไฟล์')

update_table()
#update_record()
#GUI.bind('<Tab>',Lambda x: E2.focus())
GUI.mainloop()
