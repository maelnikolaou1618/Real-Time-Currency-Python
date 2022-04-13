from tkinter import *
import requests, json

window=Tk()
window.geometry("300x210")
window.title('Currency Convertor')
window.config(bg="light blue")
var1= StringVar()
var2= StringVar()
var1.set("currency")
var2.set("currency")

def real_time_currency():
    global base_url
    global main_url

    from_currency = var1.get()
    to_currency = var2.get()
    api_key ="K3MQO5ISZGAYC6NI"
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key
    print(main_url)
    req_ob = requests.get(main_url)
    result = req_ob.json()
    print(result)
    exchange_rate = float(result['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    amount = float(amount1_field.get())
    new_amount = round(amount * exchange_rate, 3)
    amount2_field.insert(0, str(new_amount))

def clear():
    amount1_field.delete(0, END)
    amount2_field.delete(0, END)

if __name__ =="__main__":
    headlabel = Label(window, text='Welcome to Real Time Currency Convertor', fg='purple', font=('Calibri bold', 12), bg="light blue")
    lbl1= Label(window, text='Amount:', fg='dark blue', font=('Calibri', 12), bg="light blue")
    lbl2 = Label(window, text='From Currency:', fg='dark blue', font=('Calibri', 12), bg="light blue")
    lbl3 = Label(window, text='To Currency:', fg='dark blue', font=('Calibri', 12), bg="light blue")
    lbl4 = Label(window, text='Converted Amount:', fg='dark blue', font=('Calibri bold', 12), bg="light blue")
    headlabel.grid(row=0, column=0, columnspan=3)
    lbl1.grid(row=1, column=0)
    lbl2.grid(row=2, column=0)
    lbl3.grid(row=3, column=0)
    lbl4.grid(row=5, column=0)
    amount1_field = Entry(window, justify='center', width=10)
    amount2_field = Entry(window, justify='center', width=10)
    amount1_field.grid(row=1, column=1, ipadx='25')
    amount2_field.grid(row=5, column=1, ipadx='25')
    currencycode_list =['INR', 'USD', 'CAD', 'CNY', 'DKK', 'EUR']
    fromcurrency_opt = OptionMenu(window, var1, *currencycode_list)
    fromcurrency_opt.config(fg="dark blue", bg="light pink", font=('Calibri', 11))
    tocurrency_opt = OptionMenu(window, var2, *currencycode_list)
    tocurrency_opt.config(fg="dark blue", bg="light pink", font=('Calibri', 11))
    fromcurrency_opt.grid(row=2, column=1, ipadx=10)
    tocurrency_opt.grid(row=3, column=1, ipadx=10)
    btn1 = Button(window, text='Convert', bg='purple', fg='white', font=('Calibri', 11), command=real_time_currency)
    btn2 = Button(window, text='Clear', bg='purple', fg='white', font=('Calibri', 11), command=clear)
    btn1.grid(row=4, column=1)
    btn2.grid(row=6, column=1)

window.mainloop()