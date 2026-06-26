from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class BankApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        label = Label(text='🏦 کیف پول بانکی', font_size='32sp')
        btn = Button(text='ورود', size_hint=(1, 0.3))
        layout.add_widget(label)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    BankApp().run()
