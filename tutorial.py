import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infitnite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)

        # Set colums
        self.cols = 1

        # Create a second gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # Add widgets
        self.top_grid.add_widget(Label(text="Name: "))
        # Add Input Box
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Favorite Pizza: "))
        # Add Input Box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text="Favorite colour: "))
        # Add Input Box
        self.colour = TextInput(multiline=False)
        self.top_grid.add_widget(self.colour)

        # Add top grid
        self.add_widget(self.top_grid)

        # Create a Subit Button
        self.submit = Button(text="Submit", font_size=32)
        # Bind button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        colour = self.colour.text

        #print(f'Hello {name} you like {pizza} pizza and your favourite colour is {colour}')
        self.add_widget(Label(text=f'Hello {name} you like {pizza} pizza and your favourite colour is {colour}'))

        # Clear input
        self.name.text = ""
        self.pizza.text = ""
        self.colour.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()