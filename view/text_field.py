from tkinter import Entry


class TextField(Entry):
    def __init__(self, master=None):
        
        self._entry_config = {
            "bd": 0,
            "font": ("Arial", 20),
        }

        super().__init__(master)
