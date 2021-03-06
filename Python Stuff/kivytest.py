from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial


class KivyButton(App):
	def disable(self, instance, *args):

		instance.disabled = True

	def update(self, instance, *args):

		instance.text = "I am Disabled!"

	def build(self):

		mybtn = Button(
			text="Click me to disable", pos=(300, 350), size_hint=(0.25, 0.18)
		)

		mybtn.bind(on_press=partial(self.disable, mybtn))

		mybtn.bind(on_press=partial(self.update, mybtn))

		return mybtn


KivyButton().run()
