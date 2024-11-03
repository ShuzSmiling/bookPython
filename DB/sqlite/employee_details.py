import tkinter
import tkinter.messagebox
import sqlite3

class EmployeeDetails:
    def __init__(self):
        # создать главное окно
        self.main_window = tkinter.Tk()

        # скомпоновать содержимое главного окна
        self.__build_main_window()

        # Запустить главный цикл
        tkinter.mainloop()
    
    # скомпоновать главное окно 
    def __build_main_window(self):
        # создать надпись с подсказкой для пользователя
        self.__create_prompt_label()
        
        # Скомпоновать рамку виджета ListBox
        self.__build_listbox_frame()
        
        # создать кнопку Выйти
        self.__create_quit_button()
        
    
    # создать надпись с подсказкой для пользователя
    def __create_prompt_label(self):
        self.employee_prompt_label = tkinter.Label(
            self.main_window, text='Выберите сотрудника'
        )
        self.employee_prompt_label.pack(side='top', padx=5, pady=5)
        
    # Скомпоновать рамку, содержащую виджеты Listbox и Scrollbar
    def __build_listbox_frame(self):
        # создать рамку для виджетов ListBox и Scrollbar
        self.listbox_frame = tkinter.Frame(self.main_window)
        
        # Настроить виджет Listbox()
        self.__setup_listbox()
        
        # создать полосу прокрутки для просмотра элементов в виджете ListBox
        self.__create_scrollbar()
        
        # Заполнить виджет Lisbox именами сотрудников
        self.__populate_listbox()
        
        # Упаковать рамку виджета Listbox
        self.__populate_listbox()
        
    # Создать виджет ListBox для вывода имен сотрудников на экран
    def __setup_listbox(self):
        # создать виджет Listbox
        self.employee_lisbox = tkinter.Listbox(
            self.listbox_frame, selectmode=tkinter.SINGLE, height=6
        )
        
        # привязать виджет Listbox к функции обратного вызова
        self.employee_lisbox.bind(
            '<<ListboxSelect>>', self.__get_details
        )
        
        # Упаковать виджет
        self.employee_lisbox.pack(side='left', padx=5, pady=5)
        
    # Создать вертикальный Scrollbar для использования с listbox
    def __create_scrollbar(self):
        self.scrollbar = tkinter.Scrollbar(self.listbox_frame,
                                           orient=tkinter.VERTICAL)
        self.scrollbar.config(command=self.employee_lisbox.yview)
        self.employee_lisbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill=tkinter.Y)
        
    # Вывести на экран имена сотрудников в виджете Listbox
    def __populate_listbox(self):
        for employee in self.__get_employees():
            self.employee_lisbox.insert(tkinter.END, employee)
            
    # создать кнопку выхода из программы
    def __create_quit_button(self):
        self.quit_button = tkinter.Button(
            self.main_window, text='Выйти', 
            command=self.main_window.destroy
        )
        self.quit_button.pack(side='top', padx=10, pady=5)
        
    # получить список имен сотрудников из базы
    def __get_employees(self):
        employee_list = []
        conn = None
        try:
            conn = sqlite3.connect('./files/employees.db')
            cur = conn.cursor()
            cur.execute('SELECT Name FROM Employees')
            
            employee_list = [n[0] for n in cur.fetchall()]
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Ошибка БД', err)
        finally:
            if conn != None:
                conn.close()
            
            return employee_list
    
    # Получить информацию по выбранному сотруднику
    def __get_details(self, event):
        lisbox_index = self.employee_lisbox.curselection()[0]
        selected_emp = self.employee_lisbox.get(lisbox_index)
        
        conn = None
        try:
            conn = sqlite3.connect('./files/employee.db')
            cur = conn.cursor()
            
            cur.execute('''
                        SELECT
                            Employees.Name,
                            Employees.Postiton,
                            Departments.DepartmentName,
                            Locations.City
                        FROM
                            Employees, Departments, Locations
                        WHERE 
                            Employees.Name = ? AND
                            Employees.DepartmentID == DepartmentsID AND
                            Employees.LocationID == Locations.LocationId
                        ''', (selected_emp, ))
            result = cur.fetchone()
            self.__display_details(name=result[0], 
                                   position=result[1],
                                   department=result[2], 
                                   location=result[3])
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Ошибка БД', err)
        finally:
            if conn != None:
                conn.close()
                
    def __display_details(self, name, position, department, location):
        tkinter.messagebox.showinfo('Информация о сотруднике,'
                                    f'Имя: {name}\n'
                                    f'Должность: {position}\n'
                                    f'Отдел: {department}\n'
                                    f'Местоположение: {location}')
        
        
if __name__ == '__main__':
    employee_details = EmployeeDetails()