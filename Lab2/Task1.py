from tkinter import *

window = Tk()

window.title('Sort and find')
window.geometry("900x600")
window.maxsize(1100, 700)  
window.minsize(600, 450)

class Logic:

    arr = []

    def BubbelSort(self):
        arr = list_entry.get()
        if arr == "":
            lbl_sort.configure(text=f"Error...")
            return
        arr = arr.split(",")
        arr_len = len(arr)
        if arr_len > 20:
            lbl_sort.configure(text=f"Do not input more than 20el...")
            return
        arr = [int(i) for i in arr]
        for i in range(arr_len):
            swapped = False
            for j in range(arr_len-i-1):
                if arr[j] > arr[j+1]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
                    swapped = True
            if not swapped:
                break
        lbl_sort.configure(text=f"Sorted list: {arr}")   
        self.arr = arr     

    def BinSearch(self):
        if not self.arr:
            lbl_find.configure(text="Input and sort arr at first...")
            return
        num = int(num_entry.get())
        arr_len = len(self.arr)
        l, r, m = 0, arr_len-1, arr_len//2
        while l <= r:
            m = l + (r - l) // 2
            if self.arr[m] == num:
                lbl_find.configure(text=f"Index: {m}")
                return
            elif self.arr[m] < num:
                l = m + 1
            else:
                r = m - 1
        lbl_find.configure(text="Can not find...")

program = Logic()

sort_button = Button(
    text="Sort!",
    height=1,
    command=program.BubbelSort,
)
sort_button.place(relx=0.7, rely=0.1, relwidth=0.2)

list_entry = Entry()
list_entry.place(relx=0.1, rely=0.1, relwidth=0.5)


lbl_sort = Label()
lbl_sort.bind('<Configure>', lambda e: lbl_sort.config(wraplength=lbl_sort.winfo_width(), justify="right"))
lbl_sort.place(rely=0.27, relx=0.1, relwidth=0.8)

find_button = Button(
    text="Find!",
    height=1,
    command=program.BinSearch,
)
find_button.place(relx=0.7, rely=0.6, relwidth=0.2)

num_entry = Entry()
num_entry.place(relx=0.1, rely=0.6, relwidth=0.5)


lbl_find = Label()
lbl_find.bind('<Configure>', lambda e: lbl_find.config(wraplength=lbl_sort.winfo_width(), justify="right"))
lbl_find.place(rely=0.8, relx=0.1, relwidth=0.8)

window.mainloop()