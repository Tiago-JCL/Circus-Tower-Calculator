from tkinter import *
import tkinter
import tkinter.messagebox
import customtkinter
#customtkinter is in 5.2.0, the latest version does not run it
from PIL import Image, ImageTk
import time

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Circus Tower Defense Tower Calculator")
        self.geometry("1100x580")
        self.iconbitmap("./imgs/ico_pory.ico")

        # Create sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.pack(side="left", fill="y")  # Pack to left side, fill vertically

        # Create sidebar widgets
        self.pory_images = []  # Store a list of CTkImages for each frame
        for i in range(60):  # There is 60 frames in the GIF
            image = Image.open(f"./imgs/poryframes/pory_{i}.gif")
            self.pory_images.append(customtkinter.CTkImage(
                light_image=image,
                dark_image=image,
                size=(90, 90)
            ))
        self.current_frame = 0
        self.pory_label = customtkinter.CTkLabel(self.sidebar_frame,text="", image=self.pory_images[0])
        self.menu_label = customtkinter.CTkLabel(self.sidebar_frame, text="Menu",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Main", command=self.show_maintab)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Characters",
                                                        command=self.show_characters)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Configs", command=self.show_configs)
        self.pory_label.pack(pady=(10, 10))
        self.menu_label.pack(pady=(20, 10))
        self.sidebar_button_1.pack(pady=10)
        self.sidebar_button_2.pack(pady=10)
        self.sidebar_button_3.pack(pady=10)
        self.animate_gif()  # Start the animation

        # Create central frame
        self.central_frame = customtkinter.CTkFrame(self)
        self.central_frame.pack(side="right", fill="both", expand=True)

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

    def animate_gif(self):
        self.pory_label.configure(image=self.pory_images[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.pory_images)  # Cycle through frames
        self.after(50, self.animate_gif)  # Call this function again after 50ms


if __name__ == "__main__":
    app = App()
    app.mainloop()