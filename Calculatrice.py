def button_press(touche) :
    number = [str(i) for i in range(10)]
    number.append(".")
    number.append("-")
    
    operations = ["+","-","x","÷","^"]
    if touche in number :
        treat_num(touche)
    elif touche in operations :
        treat_operations(touche)
    elif touche == '=' :
        execute_operation(current_operation)
    elif touche == "CE" :
        reset_calculator()
    elif touche == "del" :
        delete()

max_num = 9
liste = []


#Affichage du nombre courant
def update_screen(value=False) :
    if value :
        screen.configure(text=value[0:9])
    else :
        screen.configure(text = "0")
        
def get_num_as_text() :
    t = ""
    for num in liste :
        t += str(num)
    return t
    
def treat_num(num) :
    if len(liste) < max_num :
        if num == "." and "." in liste :
            return
        if num == "-" and "-" in liste :
            return 
        liste.append(num)
        update_screen(get_num_as_text())
        
## opérations à faire
current_num = False
current_operation = False

def treat_operations(operation) :
    global current_num, current_operation
    if current_num and current_operation :
        execute_operation(current_operation) 
    if not current_num :
        current_num = get_num_from_liste()
    current_operation = operation
    liste.clear()


def get_num_from_liste() :
    text = get_num_as_text()
    if '.' in liste or "-" in liste :
        return float(text)
    else :
        return int(text)

#fonction qui permet d'effacer les chiffres
def delete() :
    if liste :
        liste.pop()
        update_screen(get_num_as_text())
    else :
        update_screen()

#executer les opérations
#fonction qui calcule l'exposant d'un chiffre
def exposant(x:float, n : float) :
    return x**n

def execute_operation(operation) :
    global current_num
    if operation :
        nb2 = get_num_from_liste()
        result = 0
        if operation == "+" :
            result = current_num + nb2
        elif operation == "-" :
            result = current_num - nb2
        elif operation == "x" :
            result = current_num * nb2
        elif operation == "÷" :
            result = current_num / nb2
        elif operation  == "^" :
            result = exposant(current_num,nb2)
        
        current_num = result
        liste.clear()
        update_screen(str(current_num))
    

#fonction qui réinitialise la calaculatrice
def reset_calculator(): 
    global current_num, current_operation
    current_num = False
    current_operation = False

    liste.clear()
    update_screen()
    
    
###Importation de la libraire pour l'interface
import customtkinter
#apparance de la calculatice
customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title("Calculatrice")
##Dimensions de la calculatrice
app.geometry("380x600") 

screen_font = ('Courrier', 55, 'bold') #Police des écritures
screen = customtkinter.CTkLabel(app, text = "0", font = screen_font)

screen.grid(row = 0, column = 0, sticky = "E",padx = (10,10), pady = (20,30), columnspan = 4)
font_button = ("Arial",30,"bold")

btn_0 = customtkinter.CTkButton(app, text = "0", width = 75, height = 75, font = font_button, command = lambda : button_press("0"))
btn_1 = customtkinter.CTkButton(app, text = "1", width = 75, height = 75, font = font_button, command = lambda : button_press("1"))
btn_2 = customtkinter.CTkButton(app, text = "2", width = 75, height = 75, font = font_button, command = lambda : button_press("2"))
btn_3 = customtkinter.CTkButton(app, text = "3", width = 75, height = 75, font = font_button, command = lambda : button_press("3"))
btn_4 = customtkinter.CTkButton(app, text = "4", width = 75, height = 75, font = font_button, command = lambda : button_press("4"))
btn_5 = customtkinter.CTkButton(app, text = "5", width = 75, height = 75, font = font_button, command = lambda : button_press("5"))
btn_6 = customtkinter.CTkButton(app, text = "6", width = 75, height = 75, font = font_button, command = lambda : button_press("6"))
btn_7 = customtkinter.CTkButton(app, text = "7", width = 75, height = 75, font = font_button, command = lambda : button_press("7"))
btn_8 = customtkinter.CTkButton(app, text = "8", width = 75, height = 75, font = font_button, command = lambda : button_press("8"))
btn_9 = customtkinter.CTkButton(app, text = "9", width = 75, height = 75, font = font_button, command = lambda : button_press("9"))

btn_plus = customtkinter.CTkButton(app, text = "+", width = 75, height = 180, font = font_button, command = lambda : button_press("+"))
btn_moins = customtkinter.CTkButton(app, text = "-", width = 75, height = 75, font = font_button, command = lambda : button_press("-"))
btn_multiplier = customtkinter.CTkButton(app, text = "x", width = 75, height = 75, font = font_button, command = lambda : button_press("x"))
btn_diviser = customtkinter.CTkButton(app, text = "÷", width = 75, height = 75, font = font_button, command = lambda : button_press("÷"))
btn_point = customtkinter.CTkButton(app, text = ".", width = 75, height = 75, font = font_button, command = lambda : button_press("."))
btn_exposant = customtkinter.CTkButton(app, text = "^", width = 75, height = 75, font = font_button, command = lambda : button_press("^"))
btn_egal = customtkinter.CTkButton(app, text = "=", width = 75, height = 75, font = font_button, command = lambda : button_press("="))
btn_reset = customtkinter.CTkButton(app, text = "CE", width = 75, height = 75, font = font_button, command = lambda : button_press("CE"))
btn_del = customtkinter.CTkButton(app, text = "del", width = 75, height = 75, font = font_button, command = lambda : button_press("del"))
#placer sur la grille
btn_0.grid(row=5,column=0,padx=(10,10),pady=(10,10))
btn_1.grid(row=4,column=0,padx=(10,10),pady=(10,10))
btn_2.grid(row=4,column=1,padx=(10,10),pady=(10,10))
btn_3.grid(row=4,column=2,padx=(10,10),pady=(10,10))
btn_4.grid(row=3,column=0,padx=(10,10),pady=(10,10))
btn_5.grid(row=3,column=1,padx=(10,10),pady=(10,10))
btn_6.grid(row=3,column=2,padx=(10,10),pady=(10,10))
btn_7.grid(row=2,column=0,padx=(10,10),pady=(10,10))
btn_8.grid(row=2,column=1,padx=(10,10),pady=(10,10))
btn_9.grid(row=2,column=2,padx=(10,10),pady=(10,10))

btn_plus.grid(row=4,column=3,padx=(10,10),pady=(10,10),rowspan = 2)
btn_moins.grid(row=3,column=3,padx=(10,10),pady=(10,10))
btn_diviser.grid(row=1,column=3,padx=(10,10),pady=(10,10))
btn_multiplier.grid(row=2,column=3,padx=(10,10),pady=(10,10))
btn_point.grid(row=5,column=1,padx=(10,10),pady=(10,10))
btn_egal.grid(row=5,column=2,padx=(10,10),pady=(10,10))
btn_reset.grid(row=1,column=0,padx=(10,10),pady=(10,10))
btn_exposant.grid(row=1,column=1,padx=(10,10),pady=(10,10))
btn_del.grid(row=1,column=2,padx=(10,10),pady=(10,10))




app.mainloop()
