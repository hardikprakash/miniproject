import tkinter as tk
import main

def launchMain():
    pH, pR = prefHeadless.get(), prefRefresh.get()
    root.destroy()
    main.main(pH, pR)


root = tk.Tk()
root.title("Facenet Demo Launcher")

prefHeadless = tk.IntVar()
prefRefresh = tk.IntVar()

# Make a label saying "Choose launch options."

label = tk.Label(root, text="Choose launch options:")
checkBoxHeadless = tk.Checkbutton(root, text="Headless", variable=prefHeadless)
checkBoxRefresh = tk.Checkbutton(root, text="Refresh Database", variable=prefRefresh)
buttonLaunch = tk.Button(root, text="Launch", command=launchMain)

# Arrange these checkboxes in a grid, keep button below the checkboxes and keep the label at top.
label.grid(row=0, column=0)
checkBoxHeadless.grid(row=1, column=0)
checkBoxRefresh.grid(row=2, column=0)
buttonLaunch.grid(row=3, column=0)

# Create app loop.
root.mainloop()