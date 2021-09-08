import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import random

kivy.require('2.0.0')


class GameView(BoxLayout):
    def __init__(self):
        super(GameView, self).__init__()
        self.randomValue = random.randint(0, 1000)
    def check_number(self):
        if int(self.answer_input.text) == self.randomValue:
            self.result_label.text = "Congratulation !"
            self.result_label.color = "#00ef0b"
            self.randomValue = random.randint(0, 1000)
        elif int(self.answer_input.text) > self.randomValue:
            self.result_label.text = "Less"
            self.result_label.color = "#ef3e00"
        elif int(self.answer_input.text) < self.randomValue:
            self.result_label.text = "More"
            self.result_label.color = "#ef3e00"

class PascalApp(App):
    def build(self):
        return GameView()


pascalApp = PascalApp()

pascalApp.run()
