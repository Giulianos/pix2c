import tkinter as tk
import numpy as np

class Matrix(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pixels = np.array([[False for i in range(0,5)] for j in range(0,5)])
        print(self.pixels)

        self.buttons = []
        for row in range(0, 5):
            self.buttons.append([])
            for col in range(0, 5):
                button = tk.Button(self, text=' ', bg='black', command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row].append(button)
    
    def on_click(self, row, col):
        value = self.pixels[row][col]
        if value:
            self.pixels[row][col] = False
            self.buttons[row][col].configure(bg='black')
        else:
            self.pixels[row][col] = True
            self.buttons[row][col].configure(bg='white')

    def get_matrix(self):
        return self.pixels.copy()


