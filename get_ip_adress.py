import socket
from tkinter import * 

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


window = Tk()
window.iconbitmap("Root2.ico")
window.title("MEU IP - CPD v-01")
window.config(padx=30, pady=40)
window.resizable(False, False) #trava janela
text1_label = Label(text=f"MEU IP :{ip_address}", font=("Arial", 12, "bold"))
text1_label.grid(row=2, column=0)
text2_label = Label(text=f"HOST :{hostname}", font=("Arial", 12, "bold"))
text2_label.grid(row=3, column=0)

window.mainloop()


print(f"Seu endereço IP é: {ip_address}")
print(f"Seu endereço IP é: {hostname}")