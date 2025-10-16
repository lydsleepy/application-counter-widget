import tkinter as tk
from tkinter import messagebox
from counter import Counter
from config import *

class CounterWidget:
    # main widget window & ui components

    def __init__(self):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.attributes('-topmost', ALWAYS_ON_TOP)
        
        # widget currently cant be resized by user
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)
        
        self.counter = Counter()
        self.setup_ui()
    
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
        self.current_var = tk.StringVar(value=str(self.counter.current))
        current_entry = tk.Entry(
            counter_frame,
            textvariable=self.current_var,
            font=COUNTER_FONT,
            width=4,
            justify=tk.CENTER,
            bg=BUTTON_COLOR,
            fg=FG_COLOR,
            relief=tk.FLAT,
            insertbackground=ACCENT_COLOR
        )
        current_entry.pack(side=tk.LEFT, padx=2)
        current_entry.bind("<Return>", self._on_current_update)
        current_entry.bind("<FocusOut>", self._on_current_update)

        # slash label
        slash_label = tk.Label(
            counter_frame,
            text="/",
            font=COUNTER_FONT,
            bg=BG_COLOR,
            fg=FG_COLOR
        )
        slash_label.pack(side=tk.LEFT)

        # total counter entry
        self.total_var = tk.StringVar(value=str(self.counter.total))
        total_entry = tk.Entry(
            counter_frame,
            textvariable=self.total_var,
            font=COUNTER_FONT,
            width=4,
            justify=tk.CENTER,
            bg=BUTTON_COLOR,
            fg=FG_COLOR,
            relief=tk.FLAT,
            insertbackground=ACCENT_COLOR
        )
        total_entry.pack(side=tk.LEFT, padx=2)
        total_entry.bind("<Return>", self._on_total_update)
        total_entry.bind("<FocusOut>", self._on_total_update)

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
            fg=FG_COLOR if self.counter.get_remaining() > 0 else ACCENT_COLOR
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
        settings_btn.place(relx=0.95, rely=0.95, anchor=tk.SE)

    def _on_increment(self):
    # handles increment button click
        self.counter.increment()
        self._update_display()

    def _on_decrement(self):
    # handles decrement button click
        self.counter.decrement()
        self._update_display()

    def _on_current_update(self, event=None):
    # handles current value updates
        self.counter.set_current(self.current_var.get())
        self._update_display()

    def _on_total_update(self, event=None):
    # handles total value updates
        self.counter.set_total(self.total_var.get())
        self._update_display()

    def _update_display(self):
    # handles updating the display
    # aka refreshing all of the display elements
        self.current_var.set(str(self.counter.current))
        self.total_var.set(str(self.counter.total))
        self.remaining_label.config(
            text=self.counter.get_remaining_text(),
            fg=ACCENT_COLOR if self.counter.get_remaining() == 0 else FG_COLOR
        )
    
    def _open_settings(self):
    # opens the settings... yeah
        settings_win = tk.Toplevel(self.root)
        settings_win.title("Settings")
        settings_win.geometry("300x150")
        settings_win.configure(bg=BG_COLOR)
        settings_win.transient(self.root)
        settings_win.grab_set()

        tk.Label(
            settings_win,
            text="Set total goal:",
            font=SETTINGS_FONT,
            bg=BG_COLOR,
            fg=FG_COLOR,
        ).pack(pady=20)

        total_var = tk.StringVar(value=str(self.counter.total))
        total_entry = tk.Entry(
            settings_win,
            textvariable=total_var,
            font=("Consolas", 14),
            width=10,
            justify=tk.CENTER,
            bg=BUTTON_COLOR,
            fg=FG_COLOR
        )
        total_entry.pack(pady=10)

        # nested function!!!
        def save_settings():
            if self.counter.set_total(total_var.get()):
                self._update_display()
                settings_win.destroy()
            else:
                messagebox.showerror("ERROR", "Please enter a number greater than 0")

        tk.Button(
            settings_win,
            text="Save",
            font=("Consolas", 11),
            bg=ACCENT_COLOR,
            fg="#000000",
            activebackground="#00cc6a",
            relief=tk.FLAT,
            command=save_settings
        ).pack(pady=10)
        
    def run(self):
    # runs / starts the widget
        self.root.mainloop()