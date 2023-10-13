import tkinter as tk
import random
import datetime

numbers=[]
def action(event,number,coordinates):
    print("Button clicked!",number)
    n=len(numbers)
    if n==0:
        if number==1:
            numbers.append(number)
            global time
            time=datetime.datetime.now()
        else:
            print('Error')
    else:
        if number-numbers[n-1]==1:
            print('Correct')
            x, y, _, _ = canvas.coords(buttons[n-1])
            canvas.create_line(coordinates[0], coordinates[1], x+10, y+10, fill="red")
            numbers.append(number)
            if len(numbers)==25:
                print('Test Complete')
                time2=datetime.datetime.now()
                final=(time2-time).seconds
                print('Start time',time)
                print('End time',time2)
                print('Time taken:',final,'seconds')
                print('Score:')
        else:
            print('Error')
    print('\n*********\n')
    
root = tk.Tk()
window_width = 720
window_height = 720

canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

def check_overlap(new_x, new_y, buttons):
    min_distance = 100  

    for button in buttons:
        x, y, _, _ = canvas.coords(button)
        distance = ((new_x - x) ** 2 + (new_y - y) ** 2) ** 0.5
        if distance < min_distance:
            return (True,x,y)
    
    return (False,0,0)

def create_button(buttons, number):
    button_size = 18

    while True:
        new_x = random.randint(button_size, window_width - button_size)
        new_y = random.randint(button_size, window_height - button_size)

        res=check_overlap(new_x, new_y, buttons)
        if res[0]==False:
            break

    button = canvas.create_oval(new_x - button_size, new_y - button_size,
                                new_x + button_size, new_y + button_size,
                                fill="blue", outline="white")
    text = canvas.create_text(new_x, new_y, text=str(number), fill="white",
                              font=("Arial", 12, "bold"))
    coordinates=(new_x,new_y,res[1],res[2])
    canvas.tag_bind(button, "<Button-1>", lambda event: action(event,number,coordinates))
    canvas.tag_bind(text, "<Button-1>", lambda event: action(event,number,coordinates))


    return button

buttons = []
for number in range(1, 26):
    button = create_button(buttons, number)
    buttons.append(button)
root.mainloop()
