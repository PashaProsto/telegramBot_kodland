class Car:
    def __init__(self, color, brand, model=None):
        self.color = color
        self.brand = brand
        self.model = model or "стандартная модель"
        self.speed = 0
        self.engine_started = False
    
    def info(self):
        status = "заведена" if self.engine_started else "заглушена"
        return f"Автомобиль: {self.brand} {self.model}\nЦвет: {self.color}\nСостояние: {status}\nСкорость: {self.speed} км/ч"
    
    def start_engine(self):
        self.engine_started = True
        return f"Двигатель {self.brand} заведен!"
    
    def stop_engine(self):
        self.engine_started = False
        self.speed = 0
        return f"Двигатель {self.brand} заглушен"
    
    def accelerate(self, kmh=20):
        if self.engine_started:
            self.speed += kmh
            return f"Скорость увеличена до {self.speed} км/ч!"
        else:
            return "Сначала заведите двигатель!"