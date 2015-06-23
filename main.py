app = input("Запустить в графическом режиме(y/n): ")
if (app == "y"):
    import gui.gui
else:
    import gui.terminal
