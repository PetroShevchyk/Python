from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

# Базовий клас для сторінок, щоб уникнути повторення коду
class BaseScreen(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')

        # Додавання трьох звичайних кнопок
        for i in range(3):
            btn = Button(text=f'Button {i + 1}')
            layout.add_widget(btn)

        # Додавання кнопки для повернення на головну сторінку
        home_btn = Button(text='Home')
        home_btn.on_press = self.go_home
        layout.add_widget(home_btn)

        self.add_widget(layout)
    def go_home(self):
        self.manager.current = 'main'

# Головна сторінка з кнопками для навігації
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Створення кнопок для переходу на інші сторінки
        for i in range(1, 5):
            btn = Button(text=f'Page {i}')
            btn.on_press = lambda btn=btn: self.change_screen(btn.text)
            layout.add_widget(btn)

        self.add_widget(layout)

    def change_screen(self, button_text):
        self.manager.current = button_text.lower().replace(' ', '')

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        # Додавання 4 сторінок до менеджера екранів
        for i in range(1, 5):
            sm.add_widget(BaseScreen(name=f'page{i}'))
        return sm


MyApp().run()
