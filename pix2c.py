import numpy as np
import tkinter as tk
import sys

from matrix import Matrix

## App Start
root = tk.Tk()

pixel_matrix=None

def copy_code():
    m=pixel_matrix.get_matrix()

    bit = 0
    bytes=[]
    for p in np.nditer(m): 
        byte = np.floor(bit/8).astype(int)
        if bit%8 == 0:
            b = 1 if p else 0
            bytes.append(b)
        else:
            bytes[byte] |= 1<<(bit%8) if p else 0
        bit += 1

    str = '{'
    for i in range(0, len(bytes)):
        str += '0x{:02X}'.format(bytes[i])
        if i < len(bytes)-1:
            str+=', '

    str += '},'

    root.clipboard_clear()
    root.clipboard_append(str)
    root.update()
    print(str)

cols = 5
rows = 5
if len(sys.argv) == 3:
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])

pixel_matrix = Matrix(root, (rows, cols))
pixel_matrix.pack()

copy_button = tk.Button(text='Copy code', command=copy_code)
copy_button.pack()

root.mainloop()
