from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label  # Importing the Label widget

# Sample list of names
names = ["John", "Alice", "Bob", "Emily", "David"]


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        layout = self.root.ids.main  # Accessing the main BoxLayout defined in the KV file
        for name in names:
            label = Label(text=name)  # Creating a Label widget
            layout.add_widget(label)  # Adding the Label widget to the main layout


DynamicLabelsApp().run()
