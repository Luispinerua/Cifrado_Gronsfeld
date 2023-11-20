from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatIconButton

Window.keybord_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"
Window.size = (400,620)

class Screen(MDRelativeLayout):

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        background_image = Image(source='Fondo.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(background_image)
        
        layout2 = GridLayout(cols=2, row_force_default=True, row_default_height=40, pos_hint = {"center_x":0.5, "center_y":0.2})
        self.clave = MDTextField(hint_text="Ingrese la clave", helper_text= "Debe especificar una clave", helper_text_mode= "on_error",
                                 mode= "round",icon_right= "key-variant", input_filter= "int")
        layout2.add_widget(MDLabel(text="Clave:", theme_text_color="Custom",font_style='H5',text_color= (202, 100, 61),size_hint_x=None, background="1"))
        layout2.add_widget(self.clave)
        
        self.mytext = TextInput(hint_text = "Ingrese el texto", pos_hint = {"center_x":0.5,"center_y":0.43},multiline= True, size_hint= (0.95,.2), 
                            cursor_color= (56/255,182/255,1,1), foreground_color = (56/255,182/255,1,1))
        self.text = TextInput(pos_hint = {"center_x":0.5,"center_y":0.20},multiline= True, size_hint= (0.95,.2), 
                              cursor_color= (56/255,182/255,1,1), foreground_color = (56/255,182/255,1,1))
        
        self.button = MDFillRoundFlatIconButton(text="Cifrar Texto", icon="lock", pos_hint = {"center_x":0.3, "center_y":0.58},md_bg_color= (1,1,1,0), 
                                               size_hint=(.3,.05), on_press = self.cifrar)
        
        self.button2 = MDFillRoundFlatIconButton(text="Descifrar Texto", icon="lock-open", pos_hint = {"center_x":0.7, "center_y":0.58},md_bg_color= (1,1,1,0), 
                                               size_hint=(.3,.05), on_press = self.descifrar)
        
        
        self.add_widget(layout2)
        self.add_widget(self.button)
        self.add_widget(self.button2)
        self.add_widget(self.mytext)
        self.add_widget(self.text)
        
        
    def cifrar(self, instance): 
        self.button.md_bg_color = (1,1,1,0)
        self.button2.md_bg_color = (1,1,1,0)
        self.button.md_bg_color = (56/255,182/255,1,1)
        self.text._set_text(" ")
        self.mytext._set_text(" ")
        self.clave.unbind(text=self.descifrado_gronsfeld)
        self.mytext.unbind(text=self.descifrado_gronsfeld)
        self.clave.bind(text = self.cifrado_gronsfeld)
        self.mytext.bind(text = self.cifrado_gronsfeld)

    def descifrar(self, instance): 
        self.button.md_bg_color = (1,1,1,0)
        self.button2.md_bg_color = (1,1,1,0)
        self.button2.md_bg_color = (56/255,182/255,1,1)
        self.text._set_text(" ")
        self.mytext._set_text(" ")
        self.mytext.unbind(text=self.cifrado_gronsfeld)
        self.mytext.bind(text = self.descifrado_gronsfeld)

    def cifrado_gronsfeld(self, instance, text):
        try:
            texto = self.mytext.text
            clave = int(self.clave.text)
            texto_resultado = ''
            clave = [int(digit) for digit in str(clave)] 
            clave_index = 0
            for char in texto:
                if char.isalpha():
                    shift = clave[clave_index % len(clave)]
                    clave_index += 1
                    if char.isupper():
                        texto_resultado += chr((ord(char) + shift - 65) % 26 + 65)
                    else:
                        texto_resultado += chr((ord(char) + shift - 97) % 26 + 97)
                else:
                    texto_resultado += char
            return self.text._set_text(texto_resultado)
        except:
            self.clave.unbind(text=self.descifrado_gronsfeld)
            self.mytext.unbind(text=self.descifrado_gronsfeld)
            self.text._set_text(" ")
            self.clave.error = True
            
    def descifrado_gronsfeld(self,instance, text):
        try:
            texto = self.mytext.text
            clave = int(self.clave.text)
            texto_resultado = ''
            clave = [int(digit) for digit in str(clave)]
            clave_index = 0
            for char in texto:
                if char.isalpha():
                    shift = clave[clave_index % len(clave)]
                    clave_index += 1
                    if char.isupper():
                        texto_resultado += chr((ord(char) - shift - 65) % 26 + 65)
                    else:
                        texto_resultado += chr((ord(char) - shift - 97) % 26 + 97)
                else:
                    texto_resultado += char
            return self.text._set_text(texto_resultado)
        except:
            self.clave.unbind(text=self.descifrado_gronsfeld)
            self.mytext.unbind(text=self.descifrado_gronsfeld)
            self.text._set_text(" ")
            self.clave.error = True

class MyApp(MDApp):

    def build(self):
        return Screen()

if __name__ == '__main__':
    MyApp().run()
