import tkinter
import tkinter.messagebox
import customtkinter
#customtkinter is in 5.2.0, the latest version does not run it

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Circus Tower Defense Tower Calculator")
        self.geometry("1100x580")

        # Create sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.pack(side="left", fill="y")  # Pack to left side, fill vertically

        # Create sidebar widgets
        self.menu_label = customtkinter.CTkLabel(self.sidebar_frame, text="Menu",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Main", command=self.show_maintab)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Characters",
                                                        command=self.show_characters)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Configs", command=self.show_configs)
        self.menu_label.pack(pady=(20, 10))
        self.sidebar_button_1.pack(pady=10)
        self.sidebar_button_2.pack(pady=10)
        self.sidebar_button_3.pack(pady=10)

        # Create central frame
        self.central_frame = customtkinter.CTkFrame(self)
        self.central_frame.pack(side="right", fill="both", expand=True)  # Pack to right side, fill remaining space

        # Create initial content for the central frame
        self.maintab_label = customtkinter.CTkLabel(self.central_frame, text="Main Tab content here")
        self.maintab_label.pack()

        # Initially show maintab content
        self.show_maintab()

    def show_maintab(self):
        self.maintab_label.pack()
        if hasattr(self, "characters_label"):  # Check if label exists before hiding
            self.characters_label.pack_forget()
        if hasattr(self, "configs_label"):
            self.configs_label.pack_forget()

    def show_characters(self):
        self.characters_label = customtkinter.CTkLabel(self.central_frame, text="Characters content here")
        self.characters_label.pack()
        self.maintab_label.pack_forget()
        if hasattr(self, "configs_label"):
            self.configs_label.pack_forget()

    def show_configs(self):
        self.configs_label = customtkinter.CTkLabel(self.central_frame, text="Configs content here")
        self.configs_label.pack()
        self.maintab_label.pack_forget()
        if hasattr(self, "characters_label"):
            self.characters_label.pack_forget()


if __name__ == "__main__":
    app = App()
    app.mainloop()