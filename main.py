from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager


class testApp(Screen):
    def __int__(self, **kwargs):
        super().__int__(**kwargs)


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        welcome_label = Label(text='Welcome to the Home Screen!')

        layout.add_widget(welcome_label)
        self.add_widget(layout)


class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'

        self.screen_manager = ScreenManager()
        self.login_screen = testApp(name='login')
        self.home_screen = HomeScreen(name='home')
        self.screen_manager.add_widget(self.login_screen)
        self.screen_manager.add_widget(self.home_screen)

        return self.screen_manager




    def verify_data(self, email, pwd):
        from firebase import firebase

        firebase = firebase.FirebaseApplication('https://asymmetric-ray-385413-default-rtdb.firebaseio.com/', None)

        # data = {
        # 'Email': Email,
        # 'Password': pwd
        # }

        # post data

        # firebase.post('asymmetric-ray-385413-default-rtdb/Users',data)

        result = firebase.get('asymmetric-ray-385413-default-rtdb/Users', '')

        for i in result.keys():
            if result[i]['Email'] == email:
                if result[i]['Password'] == pwd:
                    self.screen_manager.current = 'home'


if __name__ == "__main__":
    Window.size = (350, 700)
    Builder.load_file("main.kv")
    MyApp().run()
