import tkinter
from string import digits, ascii_lowercase, ascii_uppercase, punctuation
import password
from int_spin_box import IntSpinBox
import customtkinter
from PIL import Image


class MessageError(customtkinter.CTkToplevel):
    """
    Сообщение об ошибке, если длина пароля равна нулю.
    """

    def __init__(self):
        super().__init__()

        self.title('Предупреждение!')
        self.geometry('400x100+150+150')
        self.resizable(False, False)
        self.grab_set()

        self.label = customtkinter.CTkLabel(self,
                                            text_color="red",
                                            text="Не выбраны наборы символов для создания пароля!")
        self.label.pack(side="top", pady=20)

        self.button = customtkinter.CTkButton(self, text="OK", command=self.button_click)
        self.button.pack(side="bottom", pady=(0, 10))

    def button_click(self):
        self.destroy()


class App(customtkinter.CTk):
    """
    Основная форма генератора пароля.
    """

    def __init__(self):
        super().__init__()

        self.geometry("520x400+100+100")
        self.title("Генератор пароля")
        self.resizable(False, False)

        self.logo = customtkinter.CTkImage(dark_image=Image.open("passwordgenerator_image.png"),
                                           size=(460, 150))
        self.logo_label = customtkinter.CTkLabel(self,
                                                 text="",
                                                 image=self.logo)
        self.logo_label.grid(row=0,
                             column=0,
                             padx=(0, 0),
                             pady=(0, 0),
                             sticky="nsew")

        self.password_frame = customtkinter.CTkFrame(self,
                                                     fg_color="transparent")
        self.password_frame.grid(row=1,
                                 column=0,
                                 padx=(20, 20),
                                 pady=(20, 20),
                                 sticky="nsew")

        self.entry_password = customtkinter.CTkEntry(self.password_frame,
                                                     width=320)
        self.entry_password.grid(row=0,
                                 column=0,
                                 padx=(0, 20),
                                 pady=(0, 0))

        self.btn_generate = customtkinter.CTkButton(self.password_frame,
                                                    text="Создать",
                                                    command=self.set_password)
        self.btn_generate.grid(row=0,
                               column=1,
                               padx=(0, 0),
                               pady=(0, 0))

        self.settings_frame = customtkinter.CTkFrame(self)
        self.settings_frame.grid(row=2,
                                 column=0,
                                 padx=(20, 20),
                                 pady=(10, 10),
                                 sticky="nsew")

        self.int_spinbox_label = customtkinter.CTkLabel(self.settings_frame,
                                                        text="Символов в пароле:")
        self.int_spinbox_label.grid(row=0,
                                    column=0,
                                    columnspan=2,
                                    padx=20)
        self.int_spinbox = IntSpinBox(self.settings_frame,
                                      width=150,
                                      step_size=1)
        self.int_spinbox.grid(row=0,
                              column=2,
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew")

        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = customtkinter.CTkCheckBox(self.settings_frame,
                                                   text="0-9",
                                                   variable=self.cb_digits_var,
                                                   onvalue=digits,
                                                   offvalue="")
        self.cb_digits.grid(row=2,
                            column=0,
                            padx=(10, 10),
                            pady=(10, 10))

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = customtkinter.CTkCheckBox(self.settings_frame,
                                                  text="a-z",
                                                  variable=self.cb_lower_var,
                                                  onvalue=ascii_lowercase,
                                                  offvalue="")
        self.cb_lower.grid(row=2,
                           column=1,
                           padx=(10, 10))

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = customtkinter.CTkCheckBox(self.settings_frame,
                                                  text="A-Z",
                                                  variable=self.cb_upper_var,
                                                  onvalue=ascii_uppercase,
                                                  offvalue="")
        self.cb_upper.grid(row=2,
                           column=2,
                           padx=(10, 10))

        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = customtkinter.CTkCheckBox(self.settings_frame,
                                                   text="&#$%",
                                                   variable=self.cb_symbol_var,
                                                   onvalue=punctuation,
                                                   offvalue="")
        self.cb_symbol.grid(row=2,
                            column=3,
                            padx=(10, 10))

        self.appearance_mode_option_menu = customtkinter.CTkOptionMenu(self.settings_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=3,
                                              column=0,
                                              columnspan=4,
                                              pady=(10, 20))

        self.int_spinbox.set(10)
        self.cb_digits.select(0)
        self.appearance_mode_option_menu.set("System")
        self.toplevel_window = None

    def get_characters(self):
        """Генератор строки символов для создания пароля"""
        chars = "".join(self.cb_digits_var.get() +
                        self.cb_lower_var.get() +
                        self.cb_upper_var.get() +
                        self.cb_symbol_var.get())
        return chars

    def message_error(self):
        """Создание сообщения об ошибке"""
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = MessageError()

    def set_password(self):
        """Заполнение строки генератора пароля"""
        top = self.cb_digits.get() + self.cb_lower.get() + self.cb_upper.get() + self.cb_symbol.get()
        if len(top) == 0:
            self.message_error()
        elif len(top) > 0:
            self.entry_password.delete(0, "end")
            self.entry_password.insert(0, password.create_new(lenght=int(self.int_spinbox.get()),
                                                              characters=self.get_characters()))

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode):
        """Смена темы"""
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
