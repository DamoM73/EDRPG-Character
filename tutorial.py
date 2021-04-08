from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('design.kv')

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    colour = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        colour = self.colour.text

        print(f'Hello {name} you like {pizza} pizza and your favourite colour is {colour}')
        #self.add_widget(Label(text=f'Hello {name} you like {pizza} pizza and your favourite colour is {colour}'))

        # Clear input
        self.name.text = ""
        self.pizza.text = ""
        self.colour.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()