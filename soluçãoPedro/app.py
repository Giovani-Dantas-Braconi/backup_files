from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from datetime import datetime, timedelta
import calendar

class CalculadoraEstagioApp(App):
    
    def build(self):
        self.title = "Calculadora de Estágio"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.data_inicio_input = TextInput(hint_text="Digite a data de início (dd/mm/aaaa)", multiline=False)
        self.horas_trabalho_diario_input = TextInput(hint_text="Quantas horas por dia ele/ela trabalha?", multiline=False)
        self.meta_horas_input = TextInput(hint_text="Qual a carga horária total que deverá ser atingida?", multiline=False)
        self.dias_trabalho_input = TextInput(hint_text="Quantos dias por semana ele/ela trabalhará?", multiline=False)
        
        calcular_button = Button(text="Calcular Data de Término")
        calcular_button.bind(on_press=self.calcular_data_fim)
        
        layout.add_widget(self.data_inicio_input)
        layout.add_widget(self.horas_trabalho_diario_input)
        layout.add_widget(self.meta_horas_input)
        layout.add_widget(self.dias_trabalho_input)
        layout.add_widget(calcular_button)

        return layout

    def calcular_data_fim(self, instance):
        data_inicio_str = self.data_inicio_input.text
        horas_trabalho_diario = self.horas_trabalho_diario_input.text
        meta_horas = self.meta_horas_input.text
        dias_trabalho_semanais = self.dias_trabalho_input.text
        
        try:
            data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y")
            horas_trabalho_diario = int(horas_trabalho_diario)
            meta_horas = int(meta_horas)
            dias_trabalho_semanais = int(dias_trabalho_semanais)
        except ValueError:
            self.show_popup("Erro", "Por favor, preencha todos os campos corretamente.")
            return
        
        horas_trabalho_semanais = horas_trabalho_diario * dias_trabalho_semanais
        semanas_necessarias = meta_horas / horas_trabalho_semanais
        dias_necessarios = semanas_necessarias * 7
        data_fim = data_inicio
        
        while meta_horas > 0:
            if calendar.weekday(data_fim.year, data_fim.month, data_fim.day) < 5:
                meta_horas -= horas_trabalho_diario
            data_fim += timedelta(days=1)
        
        data_fim_str = data_fim.strftime("%d/%m/%Y")
        self.show_popup("Resultado", f"A data estimada para o fim do contrato é: {data_fim_str}.")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == "__main__":
    CalculadoraEstagioApp().run()
