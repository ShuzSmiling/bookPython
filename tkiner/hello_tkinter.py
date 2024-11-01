import tkinter
import tkinter.messagebox


class MyGUI:

    def __init__(self):
        # создать виджет главного окна
        self.main_windows = tkinter.Tk()
        
        # создать виджет Label, содержащий
        # надпись 'Привет мир!'
        self.label1 = tkinter.Label(self.main_windows,
                                   text='Привет мир!',
                                   borderwidth=1,
                                   relief='raised')
        self.label2 = tkinter.Label(self.main_windows,
                                    text='Это первый GUI',
                                    borderwidth=4,
                                    relief='sunken')
        
        # создание кнопки
        self.my_button = tkinter.Button(self.main_windows,
                                        text='Нажми меня!',
                                        command=self.do_something)
        
        # создание кнопки "Выход"
        self.quit_button = tkinter.Button(self.main_windows,
                                          text='Выход',
                                          command=self.main_windows.destroy)
        
        # показать заголовок
        self.main_windows.title('Hello_tk')
        
        # Вызвать метод pack виджета Label
        self.label1.pack(side='right', ipadx=20, ipady=20, padx=(40, 60), pady=20)
        self.label2.pack(ipadx=20, ipady=20, padx=(20, 40), pady=20)
        
        # Вызвать кнопку
        self.my_button.pack()
        self.quit_button.pack()
        
        
        # Войти в главный цикл tkinter
        tkinter.mainloop()
        
    
    def do_something(self):
        tkinter.messagebox.showinfo('Реакция',
                                    'Благодарю, что нажали кнопку')
        

if __name__ == '__main__':
    my_gui = MyGUI()
        