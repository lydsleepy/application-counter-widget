import tkinter as tk
from tkinter import messagebox
from counter import Counter
from config import *

class CounterWidget:
    # main widget window & ui components

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("WINDOW_TITLE")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.attributes('-topmost', ALWAYS_ON_TOP)
        
        # widget currently cant be resized by user
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)
        
        self.counter = Counter()
        self.create_ui()
    
    def setup_ui(self):
        # initializes ui components
        self._create_title()
        self._create_counter_section()
        self._create_remaining_label()
        self._create_settings_button()

    def _create_title(self):
        # creates title label
        title = tk.Label(self.root, text="LOCK IN",
                        font=TITLE_FONT, bg=BG_COLOR, fg=ACCENT_COLOR)

        # sets vertical padding - 15 px above, 5 px below
        title.pack(pady=(15,5))

    def _create_counter_section(self):
        # creates counter display with + and - buttons
        counter_frame = tk.Frame(self.root, bg=BG_COLOR)
        counter_frame.pack(pady=10)
        