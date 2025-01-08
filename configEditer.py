import json
import tkinter as tk
from tkinter import ttk


class JsonEditorApp:
    def __init__(self, root, json_data):
        self.root = root
        self.root.title("Game Parameter Editer")
        self.json_data = json_data
        self.widgets = {}

        self.create_ui()

    def create_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True)

        for category, settings in self.json_data.items():
            frame = ttk.Frame(notebook)
            notebook.add(frame, text=category)

            row = 0
            for setting, params in settings.items():
                self.add_setting_widgets(frame, category, setting, params, row)
                row += 1

    def add_setting_widgets(self, frame, category, setting, params, row):
        label = ttk.Label(frame, text=params["comment"])
        label.grid(row=row, column=0, padx=5, pady=5, sticky=tk.W)

        scale = ttk.Scale(
            frame,
            from_=params["min"],
            to=params["max"],
            orient=tk.HORIZONTAL,
            length=400,
        )
        scale.grid(row=row, column=1, padx=5, pady=5, sticky=tk.EW)
        scale.set(params["value"])

        if isinstance(params["max"], int):
            spinbox = ttk.Spinbox(
                frame, from_=params["min"], to=params["max"], increment=1, width=10
            )
            scale.configure(
                command=lambda v, sb=spinbox: sb.delete(0, tk.END)
                or sb.insert(0, int(float(v)))
            )
        else:
            spinbox = ttk.Spinbox(
                frame,
                from_=params["min"],
                to=params["max"],
                increment=0.001,
                width=10,
                format="%.3f",
            )
            scale.configure(
                command=lambda v, sb=spinbox: sb.delete(0, tk.END)
                or sb.insert(0, round(float(v), 3))
            )
        spinbox.grid(row=row, column=2, padx=5, pady=5)
        spinbox.set(params["value"])

        # Link scale and spinbox
        spinbox.bind("<Return>", lambda e, sc=scale: sc.set(float(spinbox.get())))

        self.widgets[(category, setting)] = {"scale": scale, "spinbox": spinbox}

    def save_json(self):
        for (category, setting), widget_dict in self.widgets.items():
            value = float(widget_dict["spinbox"].get())
            if isinstance(self.json_data[category][setting]["max"], int):
                value = int(value)
            self.json_data[category][setting]["value"] = value

        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(self.json_data, f, indent=4, ensure_ascii=False)

        print("Saved to output.json")


if __name__ == "__main__":
    with open("config.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)

    root = tk.Tk()
    app = JsonEditorApp(root, json_data)

    save_button = ttk.Button(root, text="Save", command=app.save_json)
    save_button.pack(pady=10)

    root.mainloop()
