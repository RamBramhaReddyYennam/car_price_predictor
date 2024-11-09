from tkinter import *
import joblib
import pandas as pd
master = Tk()
master.title("Used Car Price Prediction")
master.geometry("1200x1500")
master.config(bg= 'lightgreen')
def predict():
    p1 = float(e1.get())
    p2 = float(e2.get())
    p3 = float(e3.get())
    p4 = float(e4.get())
    p5 = float(e5.get())
    p6 = float(e6.get())
    p7 = float(e7.get())
    model = joblib.load('carpricepredictor')
    data_new = pd.DataFrame({
        'Present_Price':p1,
        'Kms_Driven':p2,
        'Fuel_Type':p3,
        'Seller_Type':p4,
        'Transmission':p5,
        'Owner':p6,
        'Age':p7
        },index=[0])
    result= model.predict(data_new)
    Label(master,text="car selling/purchasing price",font=("times",18,'bold')).place(x=200,y=700)
    Label(master,text=str(result[0]),font=("times",18,'bold')).place(x=500,y=700)
    print(result[0])
    
label = Label(text="Welcome to The Best Car Prediction App",bg='Yellow',fg='Black',font=("times",34,'bold'))
label.place(x=300,y=50)
Label(master,text='Present Price',font=("Calibri",20,'bold'),bg='lightgreen').place(x=200,y=160)
Label(master,text='KMS Driven',font=("Calibri",20,'bold'),bg='lightgreen').place(x=200,y=210)
Label(master,text='Fuel Type',font=("Calibri",20,'bold'),bg='lightgreen').place(x=200,y=260)
Label(master,text='Seller Type',font=("Calibri",20,'bold'),bg='lightgreen').place(x=200,y=310)
Label(master,text='Transmission',font=("Calibri",20,'bold'),bg='lightgreen').place(x=200,y=360)
Label(master,text='Owner',font=("Calibri",20,'bold'),bg='lightgreen').place(x=200,y=410)
Label(master,text='Age',font=("Calibri",20,'bold'),bg='lightgreen').place(x=200,y=460)
e1 = Entry(master,font=("Helvatica",20,'bold'))
e1.place(x=400,y=160)
e2 = Entry(master,font=("Helvatica",20,'bold'))
e2.place(x=400,y=210)
e3 = Entry(master,font=("Helvatica",20,'bold'))
e3.place(x=400,y=260)
e4 = Entry(master,font=("Helvatica",20,'bold'))
e4.place(x=400,y=310)
e5 = Entry(master,font=("Helvatica",20,'bold'))
e5.place(x=400,y=360)
e6 = Entry(master,font=("Helvatica",20,'bold'))
e6.place(x=400,y=410)
e7 = Entry(master,font=("Helvatica",20,'bold'))
e7.place(x=400,y=460)
Button(master,text='predict Price',command=predict,font =("times",20,'bold')).place(x=300,y=550)
Button(master,text = 'Exit',command=master.destroy,font =("times",20,'bold')).place(x=500,y=550)
mainloop()
