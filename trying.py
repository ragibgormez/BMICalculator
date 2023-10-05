from tkinter import *



#Window
window = Tk()
window.title("BMI")
window.minsize(width=400, height=200)

#label
weight = Label(text="Enter Your Weight(kg)")
weight.pack()

#entry
weightEntry = Entry(width=10)
weightEntry.pack()

#label
height = Label(text="Enter Your Height(cm)")
height.pack()

#entry
heightEntry = Entry(width=10)
heightEntry.pack()

def calculated():
    entryKilo = weightEntry.get()
    entryBoy = heightEntry.get()

    try:
        kilo = float(entryKilo)
        boy = float(entryBoy)

        BMI = kilo / (boy/100) ** 2

        if BMI < 16:
            print("Severely Underweight")
        elif 16 <= BMI < 18.5:
            print("Underweight")
        elif 18.5 <= BMI < 25:
            print("Normal")
        elif 25 <= BMI < 30:
            print("Overweight")
        elif 30 <= BMI < 35:
            print("Moderately Obese")
        elif 35 <= BMI < 40:
            print("Severaly Obese")
        elif 40 <= BMI:
            print("Morbidly Obese")
    except ValueError:
        print("Geçersiz giriş. Lütfen geçerli bir ağırlık ve boy değeri girin.")

#button
button = Button(text="Calculate", command=calculated)
button.pack()

window.mainloop()
