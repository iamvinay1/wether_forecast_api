from tkinter import *
from tkinter import ttk
import requests 



def data_get():
    city = cityname.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+ "&appid=1b664347b94201722b76e8f708f9a16d").json
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"][temp]-273.15)))
    pre_label1.config(text=data["main"]["pressure"])





win = Tk()
win.title('Weather Forecast')
win.config(bg='black')
win.geometry('500x570')

name_label = Label(win,text='Weather Forecast',font=('Times New Roman',32,'bold'))
name_label.place(x=25,y=50,height=50,width=450)
name_label = Label(win,text='Select State', font=('Times New Roman',20,'bold'))
name_label.place(x=150,y=110,height=25,width=200)

city_name = StringVar()
list_name = ("Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry")

com = ttk.Combobox(win,text='Weather Forecast', values=list_name,font=('Times New Roman',32,'bold'),textvariable='city_name')
com.place(x=25,y=150,height=50,width=450)

w_label = Label(win,text='Weather Climate',font=('Times New Roman',20,))
w_label.place(x=25,y=270,height=50,width=200)
w_label1 = Label(win,text='',font=('Times New Roman',18,))
w_label1.place(x=250,y=270,height=50,width=200)

wb_label = Label(win,text='Weather Description',font=('Times New Roman',18,))
wb_label.place(x=25,y=330,height=50,width=200)
wb_label1 = Label(win,text='',font=('Times New Roman',18,))
wb_label1.place(x=250,y=330,height=50,width=200)

temp_label = Label(win,text='Temperature',font=('Times New Roman',15,))
temp_label.place(x=25,y=390,height=50,width=200)
temp_label1 = Label(win,text='',font=('Times New Roman',15,))
temp_label1.place(x=250,y=390,height=50,width=200)

pre_label = Label(win,text='Pressure',font=('Times New Roman',15,))
pre_label.place(x=25,y=450,height=50,width=200)
pre_label1 = Label(win,text='',font=('Times New Roman',15,))
pre_label1.place(x=250,y=450,height=50,width=200)

done_button = Button(text='Done',font=('Times New Roman',20,'bold'),command=data_get)
done_button.place(x=200,y=210,height=30,width=100)
win.mainloop()