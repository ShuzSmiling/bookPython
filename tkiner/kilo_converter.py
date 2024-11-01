import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        
        # создать главное окно
        self.main_windows = tkinter.Tk()
        
        # создать две рамки, что бы сгруппировать виджеты
        self.top_frame = tkinter.Frame(self.main_windows)
        self.bottom_frame = tkinter.Frame(self.main_windows)
        
        # создать виджеты для верхней рамки
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Введите расстояние в километрах:')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width=10)
        
        # Упаковать виджеты верхней рамки
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')
        
        # созадть виджеты для нижней рамки
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Преобразовать',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                          command=self.main_windows.destroy)
        
        # Упаковать кнопки
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        # Упаковать рамки
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
        
    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        
        # показать результаты
        tkinter.messagebox.showinfo('Результаты',
                                    str(kilo) + 
                                    ' километров эквивалентно ' + 
                                    str(miles) + ' милям')
        

if __name__ == '__main__':
    kilo_convert = KiloConverterGUI()