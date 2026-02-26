import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(ft.Row(ft.Text("Calculadora de propinas", size=25), alignment=ft.MainAxisAlignment.CENTER))
    
    cuenta = ft.TextField(text_align=ft.TextAlign.CENTER, width=200, value = "0")
    page.add(ft.Row(cuenta, alignment=ft.MainAxisAlignment.CENTER))
    
    page.add(ft.Row(ft.Text("Cuanto dejara de propina", size=25), alignment=ft.MainAxisAlignment.CENTER))
    
    propina = ft.Slider(min=5, max=25, value = 5, divisions=8, label="{value}%", width=360)
    page.add(ft.Row(propina, alignment=ft.MainAxisAlignment.CENTER))
    
    def agregar(e):
        salva = float(cuenta.value or "0")
        salva_propi = float(propina.value)
        agrega.value = str(round(salva* (salva_propi/ 100),2))
        monto.value = str(round(salva + salva * (salva_propi/ 100),2))
        page.update()
    
    cuenta.on_change = agregar
    propina.on_change = agregar
    
    monto = ft.Text("0", text_align=ft.TextAlign.CENTER, size=20)
    agrega = ft.Text("0", text_align=ft.TextAlign.CENTER, size=20)
    
    page.add(ft.Row(ft.Text("Propina agregada"), alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row(agrega, alignment=ft.MainAxisAlignment.CENTER))
    
    page.add(ft.Row(ft.Text("Total a pagar"), alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row(monto, alignment=ft.MainAxisAlignment.CENTER))
    

ft.app(target=main)
