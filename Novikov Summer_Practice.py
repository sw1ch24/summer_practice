import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod


class Plant(ABC):
    def __init__(self, name):
        self.name = name
        self.stage = self.stages[0]
        self.health = 100
        self.alive = True

    @abstractmethod
    def grow(self, conditions):
        pass

class Grass(Plant):
    stages = ["Семя", "Росток", "Молодая трава", "Зрелая трава"]

    def grow(self, conditions):
        if self.alive:
            if 15 <= conditions['temperature'] <= 25 and 40 <= conditions['humidity'] <= 60 and 30 <= conditions['light'] <= 70:
                current_stage = self.stages.index(self.stage)
                if current_stage < len(self.stages) - 1:
                    self.stage = self.stages[current_stage + 1]
            else:
                self.health -= 10
            if self.health <= 0:
                self.alive = False
                self.stage = "Умерло"

class Dwarf_Shrub(Plant):
    stages = ["Семя", "Проросток", "Молодой кустарничек", "Цветущий кустарничек"]

    def grow(self, conditions):
        if self.alive:
            if 10 <= conditions['temperature'] <= 20 and 30 <= conditions['humidity'] <= 50 and 40 <= conditions['light'] <= 80:
                current_stage = self.stages.index(self.stage)
                if current_stage < len(self.stages) - 1:
                    self.stage = self.stages[current_stage + 1]
            else:
                self.health -= 10
            if self.health <= 0:
                self.alive = False
                self.stage = "Умерло"

class Shrub(Plant):
    stages = ["Семя", "Саженец", "Молодой куст", "Зрелый куст"]

    def grow(self, conditions):
        if self.alive:
            if 18 <= conditions['temperature'] <= 28 and 50 <= conditions['humidity'] <= 70 and 50 <= conditions['light'] <= 90:
                current_stage = self.stages.index(self.stage)
                if current_stage < len(self.stages) - 1:
                    self.stage = self.stages[current_stage + 1]
            else:
                self.health -= 10
            if self.health <= 0:
                self.alive = False
                self.stage = "Умерло"

class Tree(Plant):
    stages = ["Семя", "Саженец", "Молодое дерево", "Зрелое дерево"]

    def grow(self, conditions):
        if self.alive:
            if 15 <= conditions['temperature'] <= 30 and 60 <= conditions['humidity'] <= 80 and 60 <= conditions['light'] <= 100:
                current_stage = self.stages.index(self.stage)
                if current_stage < len(self.stages) - 1:
                    self.stage = self.stages[current_stage + 1]
            else:
                self.health -= 10
            if self.health <= 0:
                self.alive = False
                self.stage = "Умерло"

class Laboratory:
    def __init__(self):
        self.plants = []
        self.conditions = {'temperature': 22, 'humidity': 50, 'light': 50}

    def add_plant(self, plant):
        self.plants.append(plant)

    def remove_plant(self, plant):
        self.plants.remove(plant)

    def update(self):
        for plant in self.plants:
            plant.grow(self.conditions)


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Биологическая лаборатория")
        self.geometry("800x600")
        self.lab = Laboratory()
        self.create_widgets()

    def create_widgets(self):
        add_frame = ttk.LabelFrame(self, text="Добавить растение")
        add_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        ttk.Label(add_frame, text="Тип растения:").grid(row=0, column=0, padx=5, pady=5)
        self.plant_type = ttk.Combobox(add_frame, values=["Трава", "Кустарничек", "Кустарник", "Дерево"])
        self.plant_type.grid(row=0, column=1, padx=5, pady=5)
        self.plant_type.current(0)

        ttk.Label(add_frame, text="Название:").grid(row=1, column=0, padx=5, pady=5)
        self.plant_name = ttk.Entry(add_frame)
        self.plant_name.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(add_frame, text="Добавить", command=self.add_plant).grid(row=2, column=0, columnspan=2, pady=5)

        self.plants_frame = ttk.LabelFrame(self, text="Растения в лаборатории")
        self.plants_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

        conditions_frame = ttk.LabelFrame(self, text="Условия в лаборатории")
        conditions_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="ne")

        ttk.Label(conditions_frame, text="Температура:").grid(row=0, column=0, padx=5, pady=5)
        self.temp_scale = ttk.Scale(conditions_frame, from_=0, to=40, orient="horizontal", command=self.update_temperature)
        self.temp_scale.set(22)
        self.temp_scale.grid(row=0, column=1, padx=5, pady=5)
        self.temp_label = ttk.Label(conditions_frame, text="22°C")
        self.temp_label.grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(conditions_frame, text="Влажность:").grid(row=1, column=0, padx=5, pady=5)
        self.humid_scale = ttk.Scale(conditions_frame, from_=0, to=100, orient="horizontal", command=self.update_humidity)
        self.humid_scale.set(50)
        self.humid_scale.grid(row=1, column=1, padx=5, pady=5)
        self.humid_label = ttk.Label(conditions_frame, text="50%")
        self.humid_label.grid(row=1, column=2, padx=5, pady=5)

        ttk.Label(conditions_frame, text="Освещение:").grid(row=2, column=0, padx=5, pady=5)
        self.light_scale = ttk.Scale(conditions_frame, from_=0, to=100, orient="horizontal", command=self.update_light)
        self.light_scale.set(50)
        self.light_scale.grid(row=2, column=1, padx=5, pady=5)
        self.light_label = ttk.Label(conditions_frame, text="50%")
        self.light_label.grid(row=2, column=2, padx=5, pady=5)

        info_frame = ttk.LabelFrame(self, text="Информация об условиях роста")
        info_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="sw")

        info_text = """
        Трава: температура 15-25°C, влажность 40-60%, освещение 30-70%
        Кустарничек: температура 10-20°C, влажность 30-50%, освещение 40-80%
        Кустарник: температура 18-28°C, влажность 50-70%, освещение 50-90%
        Дерево: температура 15-30°C, влажность 60-80%, освещение 60-100%
        """
        ttk.Label(info_frame, text=info_text).pack(padx=5, pady=5)

        ttk.Button(self, text="Обновить", command=self.update_lab).grid(row=3, column=0, columnspan=2, pady=10)

    def add_plant(self):
        plant_type = self.plant_type.get()
        plant_name = self.plant_name.get()

        if not plant_name:
            messagebox.showerror("Ошибка", "Введите название растения")
            return

        if plant_type == "Трава":
            new_plant = Grass(plant_name)
        elif plant_type == "Кустарничек":
            new_plant = Dwarf_Shrub(plant_name)
        elif plant_type == "Кустарник":
            new_plant = Shrub(plant_name)
        elif plant_type == "Дерево":
            new_plant = Tree(plant_name)
        else:
            messagebox.showerror("Ошибка", "Выберите тип растения")
            return

        self.lab.add_plant(new_plant)
        self.update_plants_display()
        self.plant_name.delete(0, tk.END)

    def update_plants_display(self):
        for widget in self.plants_frame.winfo_children():
            widget.destroy()

        for i, plant in enumerate(self.lab.plants):
            frame = ttk.Frame(self.plants_frame)
            frame.grid(row=i, column=0, sticky="w", padx=5, pady=2)

            ttk.Label(frame, text=f"{plant.name} ({type(plant).__name__})").grid(row=0, column=0, sticky="w")
            ttk.Label(frame, text=f"Стадия: {plant.stage}").grid(row=0, column=1, padx=10)
            ttk.Label(frame, text=f"Здоровье: {max(plant.health, 0)}%").grid(row=0, column=2, padx=10)
            ttk.Button(frame, text="Удалить", command=lambda p=plant: self.remove_plant(p)).grid(row=0, column=3, padx=5)

    def remove_plant(self, plant):
        self.lab.remove_plant(plant)
        self.update_plants_display()

    def update_temperature(self, value):
        self.lab.conditions['temperature'] = int(float(value))
        self.temp_label.config(text=f"{int(float(value))}°C")

    def update_humidity(self, value):
        self.lab.conditions['humidity'] = int(float(value))
        self.humid_label.config(text=f"{int(float(value))}%")

    def update_light(self, value):
        self.lab.conditions['light'] = int(float(value))
        self.light_label.config(text=f"{int(float(value))}%")

    def update_lab(self):
        self.lab.update()
        self.update_plants_display()

if __name__ == "__main__":
    app = Application()
    app.mainloop()