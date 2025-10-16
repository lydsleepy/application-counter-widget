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

        # minus button
        minus_btn = tk.Button(
            counter_frame,
            text="-",
            font=BUTTON_FONT,
            width=3,
            bg=BUTTON_COLOR,
            fg=FG_COLOR,
            activebackground=BUTTON_ACTIVE_COLOR,
            activeforeground=FG_COLOR,
            relief=tk.FLAT,
            command=self._on_decrement
        )
        minus_btn.pack(side=tk.LEFT, padx=5)

        # counter entry
        self.counter_var = tk.StringVar(value=self.counter.get_progress_text())
        self.counter_entry = tk.Entry(
            counter_frame,
            textvariable=self.counter_var,
            font=COUNTER_FONT,
            width=10,
            justify=tk.CENTER,
            bg=BUTTON_COLOR,
            fg=FG_COLOR,
            relief=tk.FLAT,
            insertbackground=ACCENT_COLOR
        )
        self.counter_entry.pack(side=tk.LEFT, padx=5)
        self.counter_entry.bind("<Return>", self._on_entry_update)
        self.counter_entry.bind("<FocusOut>", self._on_entry_update)

        # plus button
        plus_btn = tk.Button(
            counter_frame,
            text="+",
            font=BUTTON_FONT,
            width=3,
            bg=BUTTON_COLOR,
            fg=FG_COLOR,
            activebackground=BUTTON_ACTIVE_COLOR,
            activeforeground=FG_COLOR,
            relief=tk.FLAT,
            command=self._on_increment
        )
        plus_btn.pack(side=tk.LEFT, padx=5)

    def _create_remaining_label(self):
    # creates label showing the remaining count
        self.remaining_label = tk.Label(
            self.root,
            text=self.counter.get_remaining_text(),
            font=LABEL_FONT,
            bg=BG_COLOR,
            fg-FG_COLOR if self.counter.get_remaining() > 0 else ACCENT_COLOR
        )
        self.remaining_label.pack(pady=10)

    def _create_settings_button(self):
    # creates settings button
        settings_btn = tk.Button(
            self.root,
            text="⚙",
            font=SETTINGS_FONT,
            bg=BUTTON_COLOR,
            fg=FG_COLOR,
            activebackground=BUTTON_ACTIVE_COLOR,
            activeforeground=FG_COLOR,
            relief=tk.FLAT,
            command=self._open_settings
        )
        settings_btn.place(relx=0.95, rely-0.95, anchor=tk.SE)

    def _on_increment(self):
    # handles increment button click
        self.counter.increment()
        self._update_display()

    def _on_decrement(self):
    # handles decrement button click
        self.counter.decrement()
        self._update_display()

# incomplete