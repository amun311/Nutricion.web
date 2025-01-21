import flet as ft
import math,time


indice_masa_corporal=''
peso=''
altura=''

edad=''
ingesta_calorica=''
def main(page: ft.Page):
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = 'Cálculo dietético'   
    page.theme_mode = ft.ThemeMode.LIGHT
    page.spacing=1
    page.scroll=ft.ScrollMode.ADAPTIVE
    page.window.icon = 'icon.ico'
    theme = ft.Theme(text_theme=ft.TextStyle(weight='Bold',color=ft.Colors.BLUE),use_material3=True)
    theme.page_transitions.android = ft.PageTransitionTheme.FADE_UPWARDS
    theme.page_transitions.linux = ft.PageTransitionTheme.NONE
    theme.page_transitions.windows = ft.PageTransitionTheme.FADE_UPWARDS
    page.theme=theme
    #page.bgcolor = ft.colors.WHITE
    
    
    #page.window_full_screen=True
    page.window.maximized=True
    page.update()
    
    container_calculos= ft.Container()
    container_back=ft.Container()
    
    
    def display(e): 
        container_calculos.content=ft.Column([
                                    ft.Image(src='info/nutrientes.jpeg',height=830)#width =1190, height=1290
                                    ])
        
        container_calculos.update()
    back= ft.IconButton(icon=ft.Icons.HOME,on_click=display)
    container_back.content=ft.Row([back],ft.MainAxisAlignment.START)
    #calculo de indice de masa corporal
    def imc_clicked(e):
        
        def imc_calc(e):
            if field_peso.value == '' or field_altura.value == '' :
               page.open(ft.SnackBar(ft.Text('Tienes que introducir mas datos',color = 'white'), bgcolor='red')) 
            else:
                imc = round(float(field_peso.value) / (float((float(field_altura.value)/100) ** 2)),1)
                if imc < 18.5 : field_imc.value = f'Insuficiencia ponderal, IMC: {imc}'
                elif 18.5<=imc<=24.9: field_imc.value = f'Intervalo normal, IMC: {imc}'
                elif 25<=imc<=29.9 : field_imc.value = f'Sobrepeso, Preobesidad, IMC: {imc}'
                elif 30<=imc<=34.9 : field_imc.value = f'Obesidad de clase I, IMC: {imc}' 
                elif 35<=imc<=39.9 : field_imc.value = f'Obesidad de clase II, IMC: {imc}' 
                elif imc>=40 : field_imc.value = f'Obesidad de clase III, IMC: {imc}' 
                globals()['indice_masa_corporal']=field_imc.value
                container_calculos.update()
        clc = ft.ElevatedButton('Calcula IMC', on_click=imc_calc,color ='white',bgcolor='blue')
        field_peso = ft.TextField(suffix_text='kilogramos',text_align=ft.TextAlign.CENTER,label='Peso',value=peso,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]|^]", replacement_string=""),width = 300)
        field_altura = ft.TextField(suffix_text='centimetros',text_align=ft.TextAlign.CENTER,label='Altura',value=altura,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_imc = ft.TextField(label = 'Índice de masa corporal',read_only=True,width = 300, color = 'blue')
        
        container_calculos.content= ft.Column([
                                            ft.Row([ft.Text('Cálculo de índice de masa corporal',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Divider(height=2, color = 'black'),
                                            ft.Row([field_peso,field_altura],ft.MainAxisAlignment.CENTER),
                                            ft.Row([clc],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_imc],ft.MainAxisAlignment.CENTER)
                                                ])
        container_calculos.update()
    #calculo riesgo diabete circumferencia abdominal
    def cabd_clicked(e):
        
        def cabd_calc(e):
            if field_circumferencia_abdominal_in.value == '' :
               page.open(ft.SnackBar(ft.Text('Tienes que introducir mas datos',color = 'white'), bgcolor='red')) 
            else:
                cabd = float(field_circumferencia_abdominal_in.value)
                if hombre_mujer.value== 0:
                    if cabd <= 93 : field_circumferencia_abdominal_out.value = 'Riesgo bajo'
                    elif 93<cabd<102 : field_circumferencia_abdominal_out.value = 'Riesgo incrementado'
                    elif cabd>=102 : field_circumferencia_abdominal_out.value = 'Riesgo alto'
                elif hombre_mujer.value ==1:
                    if cabd <= 79 : field_circumferencia_abdominal_out.value = 'Riesgo bajo'
                    elif 79<cabd<88 : field_circumferencia_abdominal_out.value = 'Riesgo incrementado'
                    elif cabd>=88 : field_circumferencia_abdominal_out.value = 'Riesgo alto'
                container_calculos.update()
        clc = ft.ElevatedButton('Calcula riesgo diabetes', on_click=cabd_calc,color ='white',bgcolor='blue')
        field_circumferencia_abdominal_in = ft.TextField(suffix_text='centimetros',text_align=ft.TextAlign.CENTER,label='Circumferencia abdominal',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_circumferencia_abdominal_out=ft.TextField(label = 'Riesgo diabete' ,read_only=True,width =300, color = 'blue')
        hombre_mujer = ft.Slider(min=0, max=1, divisions=1,active_color='blue', inactive_color='red',thumb_color='green', width=20,value = 0,on_change=cabd_calc)
        
       
        container_calculos.content= ft.Column([
                                        ft.Row([ft.Text('Cálculo riesgo diabete en funcion de circumferencia abdominal',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                        ft.Divider(height=2, color = 'black'),
                                        ft.Row([field_circumferencia_abdominal_in],ft.MainAxisAlignment.CENTER),
                                        ft.Row([clc],ft.MainAxisAlignment.CENTER),
                                        ft.Row([ft.Text('Hombre  '),hombre_mujer,ft.Text('  Mujer')],ft.MainAxisAlignment.CENTER),
                                        ft.Row([field_circumferencia_abdominal_out],ft.MainAxisAlignment.CENTER),
                                        ])
        container_calculos.update()
    #indice de cintura y cadera
    def icc_clicked(e):
        
        def icc_calc(e):
            if field_perimetro_cadera.value == '' or field_perimetro_cintura.value == '' or field_edad.value == '':
               page.open(ft.SnackBar(ft.Text('Tienes que introducir mas datos',color = 'white'), bgcolor='red')) 
            else:
                icc = round(float(field_perimetro_cintura.value) / float(field_perimetro_cadera.value),2)
                
                if hombre_mujer.value==0:
                    if 20 <= int(field_edad.value) <29:
                        if  icc < 0.83: field_icc.value = f'Riesgo BAJO, ICC: {icc}' 
                        elif 0.83 <= icc <= 0.88: field_icc.value = f'Riesgo MODERADO, ICC: {icc}'  
                        elif 0.89 <= icc <= 0.94: field_icc.value = f'Riesgo ALTO, ICC: {icc}'
                        elif icc  > 0.94: field_icc.value = f'Riesgo MUY ALTO, ICC: {icc}'
                    elif 30 <= int(field_edad.value) <39:
                        if  icc < 0.84: field_icc.value = f'Riesgo BAJO, ICC: {icc}' 
                        elif 0.84 <= icc <= 0.91: field_icc.value = f'Riesgo MODERADO, ICC: {icc}'  
                        elif 0.92 <= icc <= 0.96: field_icc.value = f'Riesgo ALTO, ICC: {icc}'
                        elif icc  > 0.96: field_icc.value = f'Riesgo MUY ALTO, ICC: {icc}'
                    elif 40 <= int(field_edad.value) <49:
                        if  icc < 0.88: field_icc.value = f'Riesgo BAJO, ICC: {icc}' 
                        elif 0.88 <= icc <= 0.95: field_icc.value = f'Riesgo MODERADO, ICC: {icc}'  
                        elif 0.96 <= icc <= 1: field_icc.value = f'Riesgo ALTO, ICC: {icc}'
                        elif icc  > 1: field_icc.value = f'Riesgo MUY ALTO, ICC: {icc}'
                    elif 50 <= int(field_edad.value) <59:
                        if  icc < 0.9: field_icc.value = f'Riesgo BAJO, ICC: {icc}' 
                        elif 0.9 <= icc <= 0.96: field_icc.value = f'Riesgo MODERADO, ICC: {icc}'  
                        elif 0.97 <= icc <= 1.02: field_icc.value = f'Riesgo ALTO, ICC: {icc}'
                        elif icc  > 1.02: field_icc.value = f'Riesgo MUY ALTO, ICC: {icc}'
                    elif 60 <= int(field_edad.value) <69:
                        if  icc < 0.91: field_icc.value = f'Riesgo BAJO, ICC: {icc}' 
                        elif 0.91 <= icc <= 0.98: field_icc.value = f'Riesgo MODERADO, ICC: {icc}'  
                        elif 0.99 <= icc <= 1.03: field_icc.value = f'Riesgo ALTO, ICC: {icc}'
                        elif icc  > 1.03: field_icc.value = f'Riesgo MUY ALTO, ICC: {icc}'
                elif hombre_mujer.value==1:
                    if 20 <= int(field_edad.value) <29:
                        if  icc < 0.71: field_icc.value = f'Riesgo BAJO, ICC: {icc}' 
                        elif 0.71 <= icc <= 0.77: field_icc.value = f'Riesgo MODERADO, ICC: {icc}'  
                        elif 0.78 <= icc <= 0.82: field_icc.value = f'Riesgo ALTO, ICC: {icc}'
                        elif icc  > 0.82: field_icc.value = f'Riesgo MUY ALTO, ICC: {icc}'
                    elif 30 <= int(field_edad.value) <39:
                        if  icc < 0.72: field_icc.value = f'Riesgo BAJO, ICC: {icc}' 
                        elif 0.72 <= icc <= 0.78: field_icc.value = f'Riesgo MODERADO, ICC: {icc}'  
                        elif 0.79 <= icc <= 0.84: field_icc.value = f'Riesgo ALTO, ICC: {icc}'
                        elif icc  > 0.84: field_icc.value = f'Riesgo MUY ALTO, ICC: {icc}'
                    elif 40 <= int(field_edad.value) <49:
                        if  icc < 0.73: field_icc.value = f'Riesgo BAJO, ICC: {icc}' 
                        elif 0.73 <= icc <= 0.79: field_icc.value = f'Riesgo MODERADO, ICC: {icc}'  
                        elif 0.8 <= icc <= 0.87: field_icc.value = f'Riesgo ALTO, ICC: {icc}'
                        elif icc  > 0.87: field_icc.value = f'Riesgo MUY ALTO, ICC: {icc}'
                    elif 50 <= int(field_edad.value) <59:
                        if  icc < 0.74: field_icc.value = f'Riesgo BAJO, ICC: {icc}' 
                        elif 0.74 <= icc <= 0.81: field_icc.value = f'Riesgo MODERADO, ICC: {icc}'  
                        elif 0.82 <= icc <= 0.88: field_icc.value = f'Riesgo ALTO, ICC: {icc}'
                        elif icc  > 0.88: field_icc.value = f'Riesgo MUY ALTO, ICC: {icc}'
                    elif 60 <= int(field_edad.value) <69:
                        if  icc < 0.76: field_icc.value = f'Riesgo BAJO, ICC: {icc}' 
                        elif 0.76 <= icc <= 0.83: field_icc.value = f'Riesgo MODERADO, ICC: {icc}'  
                        elif 0.84 <= icc <= 0.9: field_icc.value = f'Riesgo ALTO, ICC: {icc}'
                        elif icc  > 0.9: field_icc.value = f'Riesgo MUY ALTO, ICC: {icc}'
            
            container_calculos.update()            
        def ca_calc(e):
            if field_perimetro_cintura.value == '' :
               page.open(ft.SnackBar(ft.Text('Tienes que introducir mas datos',color = 'white'), bgcolor='red')) 
            else:
                if hombre_mujer.value==0:  
                    if ecuacion.value == 'Adult Panel Treatment III':                      
                        field_ca.value = 'Circunferencia abdominal ≥ 94 cm'     
                    elif ecuacion.value == 'Federación Internacional de Diabetes (IDF)':     
                        field_ca.value = 'Circunferencia abdominal ≥ 90 cm'
                    elif ecuacion.value == 'Organización Mundial de la Salud (OMS)':
                        if float(field_perimetro_cintura.value) <= 93:                          
                            field_ca.value = 'Riesgo bajo'
                        elif 93<float(field_perimetro_cintura.value) <= 101:                          
                            field_ca.value = 'Riesgo incrementado'
                        elif float(field_perimetro_cintura.value) > 101:                          
                            field_ca.value = 'Alto riesgo'
                elif hombre_mujer.value==1:  
                    if ecuacion.value == 'Adult Panel Treatment III':                      
                        field_ca.value = 'Circunferencia abdominal ≥ 80 cm'     
                    elif ecuacion.value == 'Federación Internacional de Diabetes (IDF)':     
                        field_ca.value = 'Circunferencia abdominal ≥ 80 cm'
                    elif ecuacion.value == 'Organización Mundial de la Salud (OMS)':
                        if float(field_perimetro_cintura.value) <= 79:                          
                            field_ca.value = 'Riesgo bajo'
                        elif 79<float(field_perimetro_cintura.value) <= 87:                         
                            field_ca.value = 'Riesgo incrementado'
                        elif float(field_perimetro_cintura.value) > 87:                          
                            field_ca.value = 'Alto riesgo'
            container_calculos.update()
        ecuacion =  ft.Dropdown(
            on_change=ca_calc,
            label='Circumferencia abdominal (indicador)',
            options=[
                ft.dropdown.Option("Adult Panel Treatment III"),
                ft.dropdown.Option("Federación Internacional de Diabetes (IDF)"),
                ft.dropdown.Option("Organización Mundial de la Salud (OMS)"),
            ],
            width=360,
        )
        field_ca = ft.TextField(label = 'Criterios de evaluación de riesgos',read_only=True, width=300, color = 'blue')
        clc = ft.ElevatedButton('Calcula ICC', on_click=icc_calc,color ='white',bgcolor='blue')
        field_perimetro_cintura = ft.TextField(suffix_text='centimetros',text_align=ft.TextAlign.CENTER,label='Perimetro cintura',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_perimetro_cadera = ft.TextField(suffix_text='centimetros',text_align=ft.TextAlign.CENTER,label='Perimetro cadera',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_edad = ft.TextField(suffix_text='años',text_align=ft.TextAlign.CENTER,label='Edad',value=edad,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 200)
        hombre_mujer = ft.Slider(min=0, max=1, divisions=1,active_color='blue', inactive_color='red',thumb_color='green', width=20,value = 0,on_change=icc_calc)
        field_icc = ft.TextField(label = 'Índice de cintura y cadera',read_only=True, width=300, color = 'blue')
       
        container_calculos.content= ft.Column([
                                        ft.Row([ft.Text('Índice de cintura y cadera',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                        ft.Divider(height=2, color = 'black'),
                                        ft.Row([field_perimetro_cintura,field_perimetro_cadera,field_edad],ft.MainAxisAlignment.CENTER),
                                        ft.Row([ft.Text('Hombre  '),hombre_mujer,ft.Text('  Mujer')],ft.MainAxisAlignment.CENTER),
                                        ft.Row([clc],ft.MainAxisAlignment.CENTER),
                                        ft.Row([field_icc],ft.MainAxisAlignment.CENTER),
                                        ft.Row([ecuacion],ft.MainAxisAlignment.CENTER),
                                        ft.Row([field_ca],ft.MainAxisAlignment.CENTER)
                                        ])
        container_calculos.update()
    #calculo de  la composicion corporal y procentaje de grasa
    def spc_clicked(e):
        
        def spc_calc(e):
            edad=int(field_edad.value) if field_edad.value != '' else ''
            peso=float(field_peso.value) if field_peso.value != '' else ''
            pl_bi=float(field_pl_bicipital.value) if field_pl_bicipital.value != '' else 0
            pl_tri=float(field_pl_tricipital.value) if field_pl_tricipital.value != '' else 0
            pl_sup=float(field_pl_suprailiaco.value) if field_pl_suprailiaco.value != '' else 0
            pl_sub=float(field_pl_subescapular.value) if field_pl_subescapular.value != '' else 0
            smm=pl_bi+pl_tri+pl_sup+pl_sub
            if field_edad.value == '' or field_peso.value == '' or smm == 0:
               page.open(ft.SnackBar(ft.Text('Tienes que introducir mas datos',color = 'white'), bgcolor='red')) 
            else:
                if hombre_mujer.value== 0:
                    if edad < 20 :
                        if pl_bi != 0 and pl_tri == 0 and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1066,0.0686
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1252,0.0625
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1312,0.0670    
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1092,0.0420
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1423,0.0687
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1457,0.0707
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1247,0.0501
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1561,0.0711
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1370,0.0545
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1374,0.0544
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1643,0.0727
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1466,0.0584
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1469,0.0583
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1555,0.0607
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1620,0.0630 
                    elif 20 <= edad <30 :
                        if pl_bi != 0 and pl_tri == 0 and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1015,0.0616
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1131,0.053
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1360,0.07    
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1117,0.0431
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1307,0.0603
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1469,0.0709
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1259,0.0502
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1525,0.0687
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1362,0.0538
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1429,0.0573
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1593,0.0694
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1451,0.0572
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1508,0.0599
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1575,0.0617
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1631,0.0632
                    elif 30 <= edad <40 :
                        if pl_bi != 0 and pl_tri == 0 and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.0781,0.0396
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.0834,0.0361
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.0978,0.0416    
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1047,0.0432
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.0995,0.0431
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.0753,0.0445
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1174,0.0486
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1165,0.0484
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1273,0.0531
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1260,0.0497
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1213,0.0487
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1332,0.0542
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1315,0.0510
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1393,0.0544
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1422,0.0544
                    elif 40 <= edad <50 :
                        if pl_bi != 0 and pl_tri == 0 and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.0829,0.0508
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1041,0.0609
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1246,0.0686    
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1029,0.0483
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1174,0.0614
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1341,0.0680
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1171,0.0539
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1519,0.0771
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1383,0.0660
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1392,0.0633
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1530,0.0730
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1422,0.0674
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1452,0.0640
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1604,0.0716
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1620,0.0700
                    elif edad >=50 :
                        if pl_bi != 0 and pl_tri == 0 and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.0833,0.0617
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1027,0.0662
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1334,0.076    
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1193,0.0652
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1185,0.0683
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1427,0.0762
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1307,0.0678
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1527,0.0793
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1415,0.0718
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1582,0.0771
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1569,0.0780
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1473,0.0718
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1626,0.0768
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1680,0.0787
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1715,0.0779 
                    '''elif 60 <= edad <72 :
                        if pl_bi != 0 and pl_tri == 0 and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.0997,0.0659
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1143,0.0618
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1396,0.0741    
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1171,0.0530
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1356,0.07
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1498,0.0759
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1331,0.0601
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1625,0.0797
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1463,0.0656
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1522,0.0671
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1689,0.0793
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1556,0.0683
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1605,0.0694
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1704,0.0731
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1765,0.0744'''
                elif hombre_mujer.value == 1:
                    if edad < 20 :
                        if pl_bi != 0 and pl_tri == 0 and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.0889,0.0553
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1159,0.0648
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1081,0.0621   
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.0931,0.0470
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1290,0.0657
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1241,0.0643
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1113,0.0537
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1468,0.0740
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1311,0.0624
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1278,0.0616
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1509,0.0715
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1382,0.0628
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1355,0.0622
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1517,0.0689
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1549,0.0678 
                    elif 20 <= edad <30 :
                        if pl_bi != 0 and pl_tri == 0 and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.0903,0.0601
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1319,0.0776
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1184,0.0716 
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.0923,0.0509
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1394,0.0738
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1314,0.0706
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1112,0.0568
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1582,0.0813
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1377,0.0684
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1280,0.0640
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1605,0.0777
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1441,0.0680
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1366,0.0648
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1566,0.0728
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1599,0.0717
                    elif 30 <= edad <40 :
                        if pl_bi != 0 and pl_tri == 0 and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.0794,0.0511
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1176,0.0686
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.0979,0.0567    
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.0860,0.0497
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1243,0.0646
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1120,0.0581
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1020,0.0528
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1356,0.0680
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1281,0.0644
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1132,0.0564
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1385,0.0654
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1319,0.0624
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1212,0.0570
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1397,0.0646
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1423,0.0632
                    elif 40 <= edad <50 :
                        if pl_bi != 0 and pl_tri == 0 and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.0736,0.0492
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1121,0.0691
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.0860,0.0505    
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.0691,0.0407
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1230,0.0672
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1031,0.0549
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.0921,0.0494
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1230,0.0635
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1198,0.0630
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.0997,0.0509
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1303,0.0635
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1267,0.0626
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1108,0.0536
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1278,0.0609
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1333,0.0612
                    elif edad >=50 :
                        if pl_bi != 0 and pl_tri == 0 and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.0682,0.0510
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1160,0.0762
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.0899,0.0590  
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.0656,0.0419
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1226,0.0710
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1029,0.0592
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.0857,0.0490
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1347,0.0742
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1158,0.0635
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.0963,0.0523
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1372,0.0710
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1227,0.0633
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1063,0.0544
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1298,0.0650
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1339,0.0645 
                    '''elif 60 <= edad <68 :
                        if pl_bi != 0 and pl_tri == 0 and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.0871,0.0593
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1279,0.0775
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1100,0.0669    
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.0884,0.0514
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup == 0 : C_dw,M_dw=1.1362,0.0740
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1245,0.0674
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1090,0.0577
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1507,0.0785
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1367,0.0704
                        elif pl_bi == 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1234,0.0632
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup == 0 : C_dw,M_dw=1.1543,0.0756
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub == 0 and pl_sup != 0 : C_dw,M_dw=1.1432,0.0969
                        elif pl_bi != 0 and pl_tri == 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1530,0.0727
                        elif pl_bi == 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1327,0.0643
                        elif pl_bi != 0 and pl_tri != 0  and pl_sub != 0 and pl_sup != 0 : C_dw,M_dw=1.1567,0.0717'''
                        
                            
                
            suma_pliegues = pl_bi + pl_tri + pl_sup + pl_sub
            field_suma_pliegues.value = suma_pliegues
            densidad_corporal = C_dw-(M_dw*math.log(suma_pliegues,10))
            field_densidad_corporal.value = round(densidad_corporal,5)
            masa_grasa = peso *((4.95/densidad_corporal)-4.5)
            field_masa_grasa.value = round(masa_grasa,2)
            masa_libre_grasa = peso - masa_grasa
            field_masa_libre_grasa.value = round(masa_libre_grasa,2)
            gct = round(((4.95/densidad_corporal)-4.5)*100,1)
            field_grasa_corporal.value = f'{round(gct,2)}%'
            if hombre_mujer.value == 0:
                if 18 <= edad < 25:
                    if gct <= 5 : promedio_normal = 8
                    elif 5 < gct <= 10 : promedio_normal = 9
                    elif 10 < gct <= 15 : promedio_normal = 10
                    elif 15 < gct <= 25 : promedio_normal = 12
                    elif 25 < gct <= 50 : promedio_normal = 16
                    elif 50 < gct <= 75 : promedio_normal = 20
                    elif 75 < gct <= 85 : promedio_normal = 23
                    elif 85 < gct <= 90 : promedio_normal = 25
                    elif 90 < gct <= 95 : promedio_normal = 28
                elif 25 <= edad < 30:
                    if gct <= 5 : promedio_normal = 9
                    elif 5 < gct <= 10 : promedio_normal = 10
                    elif 10 < gct <= 15 : promedio_normal = 11
                    elif 15 < gct <= 25 : promedio_normal = 13
                    elif 25 < gct <= 50 : promedio_normal = 18
                    elif 50 < gct <= 75 : promedio_normal = 23
                    elif 75 < gct <= 85 : promedio_normal = 25
                    elif 85 < gct <= 90 : promedio_normal = 26
                    elif 90 < gct <= 95 : promedio_normal = 29
                elif 23 <= edad < 35:
                    if gct <= 5 : promedio_normal = 16
                    elif 5 < gct <= 10 : promedio_normal = 17
                    elif 10 < gct <= 15 : promedio_normal = 18
                    elif 15 < gct <= 25 : promedio_normal = 20
                    elif 25 < gct <= 50 : promedio_normal = 23
                    elif 50 < gct <= 75 : promedio_normal = 26
                    elif 75 < gct <= 85 : promedio_normal = 27
                    elif 85 < gct <= 90 : promedio_normal = 28
                    elif 90 < gct <= 95 : promedio_normal = 30
                elif 35 <= edad < 40:
                    if gct <= 5 : promedio_normal = 15
                    elif 5 < gct <= 10 : promedio_normal = 17
                    elif 10 < gct <= 15 : promedio_normal = 18
                    elif 15 < gct <= 25 : promedio_normal = 20
                    elif 25 < gct <= 50 : promedio_normal = 23
                    elif 50 < gct <= 75 : promedio_normal = 25
                    elif 75 < gct <= 85 : promedio_normal = 27
                    elif 85 < gct <= 90 : promedio_normal = 27
                    elif 90 < gct <= 95 : promedio_normal = 29
                elif 40 <= edad < 45:
                    if gct <= 5 : promedio_normal = 14
                    elif 5 < gct <= 10 : promedio_normal = 16
                    elif 10 < gct <= 15 : promedio_normal = 18
                    elif 15 < gct <= 25 : promedio_normal = 21
                    elif 25 < gct <= 50 : promedio_normal = 26
                    elif 50 < gct <= 75 : promedio_normal = 30
                    elif 75 < gct <= 85 : promedio_normal = 32
                    elif 85 < gct <= 90 : promedio_normal = 34
                    elif 90 < gct <= 95 : promedio_normal = 36
                elif 45 <= edad < 50:
                    if gct <= 5 : promedio_normal = 15
                    elif 5 < gct <= 10 : promedio_normal = 17
                    elif 10 < gct <= 15 : promedio_normal = 19
                    elif 15 < gct <= 25 : promedio_normal = 21
                    elif 25 < gct <= 50 : promedio_normal = 26
                    elif 50 < gct <= 75 : promedio_normal = 30
                    elif 75 < gct <= 85 : promedio_normal = 32
                    elif 85 < gct <= 90 : promedio_normal = 34
                    elif 90 < gct <= 95 : promedio_normal = 36
                elif 50 <= edad < 55:
                    if gct <= 5 : promedio_normal = 15
                    elif 5 < gct <= 10 : promedio_normal = 17
                    elif 10 < gct <= 15 : promedio_normal = 19
                    elif 15 < gct <= 25 : promedio_normal = 22
                    elif 25 < gct <= 50 : promedio_normal = 27
                    elif 50 < gct <= 75 : promedio_normal = 31
                    elif 75 < gct <= 85 : promedio_normal = 33
                    elif 85 < gct <= 90 : promedio_normal = 35
                    elif 90 < gct <= 95 : promedio_normal = 37
                elif 55 <= edad < 60:
                    if gct <= 5 : promedio_normal = 15
                    elif 5 < gct <= 10 : promedio_normal = 18
                    elif 10 < gct <= 15 : promedio_normal = 20
                    elif 15 < gct <= 25 : promedio_normal = 22
                    elif 25 < gct <= 50 : promedio_normal = 27
                    elif 50 < gct <= 75 : promedio_normal = 31
                    elif 75 < gct <= 85 : promedio_normal = 33
                    elif 85 < gct <= 90 : promedio_normal = 35
                    elif 90 < gct <= 95 : promedio_normal = 37
            elif hombre_mujer.value == 1:
                if 18 <= edad < 25:
                    if gct <= 5 : promedio_normal = 17
                    elif 5 < gct <= 10 : promedio_normal = 19
                    elif 10 < gct <= 15 : promedio_normal = 21
                    elif 15 < gct <= 25 : promedio_normal = 23
                    elif 25 < gct <= 50 : promedio_normal = 27
                    elif 50 < gct <= 75 : promedio_normal = 33
                    elif 75 < gct <= 85 : promedio_normal = 35
                    elif 85 < gct <= 90 : promedio_normal = 37
                    elif 90 < gct <= 95 : promedio_normal = 40
                elif 25 <= edad < 30:
                    if gct <= 5 : promedio_normal = 18
                    elif 5 < gct <= 10 : promedio_normal = 20
                    elif 10 < gct <= 15 : promedio_normal = 21
                    elif 15 < gct <= 25 : promedio_normal = 24
                    elif 25 < gct <= 50 : promedio_normal = 29
                    elif 50 < gct <= 75 : promedio_normal = 34
                    elif 75 < gct <= 85 : promedio_normal = 37
                    elif 85 < gct <= 90 : promedio_normal = 39
                    elif 90 < gct <= 95 : promedio_normal = 41
                elif 23 <= edad < 35:
                    if gct <= 5 : promedio_normal = 21
                    elif 5 < gct <= 10 : promedio_normal = 23
                    elif 10 < gct <= 15 : promedio_normal = 25
                    elif 15 < gct <= 25 : promedio_normal = 27
                    elif 25 < gct <= 50 : promedio_normal = 31
                    elif 50 < gct <= 75 : promedio_normal = 36
                    elif 75 < gct <= 85 : promedio_normal = 38
                    elif 85 < gct <= 90 : promedio_normal = 40
                    elif 90 < gct <= 95 : promedio_normal = 42
                elif 35 <= edad < 40:
                    if gct <= 5 : promedio_normal = 22
                    elif 5 < gct <= 10 : promedio_normal = 24
                    elif 10 < gct <= 15 : promedio_normal = 25
                    elif 15 < gct <= 25 : promedio_normal = 28
                    elif 25 < gct <= 50 : promedio_normal = 32
                    elif 50 < gct <= 75 : promedio_normal = 37
                    elif 75 < gct <= 85 : promedio_normal = 39
                    elif 85 < gct <= 90 : promedio_normal = 40
                    elif 90 < gct <= 95 : promedio_normal = 42
                elif 40 <= edad < 45:
                    if gct <= 5 : promedio_normal = 25
                    elif 5 < gct <= 10 : promedio_normal = 28
                    elif 10 < gct <= 15 : promedio_normal = 29
                    elif 15 < gct <= 25 : promedio_normal = 31
                    elif 25 < gct <= 50 : promedio_normal = 35
                    elif 50 < gct <= 75 : promedio_normal = 39
                    elif 75 < gct <= 85 : promedio_normal = 41
                    elif 85 < gct <= 90 : promedio_normal = 42
                    elif 90 < gct <= 95 : promedio_normal = 43
                elif 45 <= edad < 50:
                    if gct <= 5 : promedio_normal = 26
                    elif 5 < gct <= 10 : promedio_normal = 28
                    elif 10 < gct <= 15 : promedio_normal = 29
                    elif 15 < gct <= 25 : promedio_normal = 32
                    elif 25 < gct <= 50 : promedio_normal = 36
                    elif 50 < gct <= 75 : promedio_normal = 39
                    elif 75 < gct <= 85 : promedio_normal = 41
                    elif 85 < gct <= 90 : promedio_normal = 42
                    elif 90 < gct <= 95 : promedio_normal = 44
                elif 50 <= edad < 55:
                    if gct <= 5 : promedio_normal = 27
                    elif 5 < gct <= 10 : promedio_normal = 30
                    elif 10 < gct <= 15 : promedio_normal = 32
                    elif 15 < gct <= 25 : promedio_normal = 35
                    elif 25 < gct <= 50 : promedio_normal = 39
                    elif 50 < gct <= 75 : promedio_normal = 43
                    elif 75 < gct <= 85 : promedio_normal = 46
                    elif 85 < gct <= 90 : promedio_normal = 47
                    elif 90 < gct <= 95 : promedio_normal = 48
                elif 55 <= edad < 60:
                    if gct <= 5 : promedio_normal = 27
                    elif 5 < gct <= 10 : promedio_normal = 30
                    elif 10 < gct <= 15 : promedio_normal = 32
                    elif 15 < gct <= 25 : promedio_normal = 35
                    elif 25 < gct <= 50 : promedio_normal = 39
                    elif 50 < gct <= 75 : promedio_normal = 44
                    elif 75 < gct <= 85 : promedio_normal = 45
                    elif 85 < gct <= 90 : promedio_normal = 47
                    elif 90 < gct <= 95 : promedio_normal = 49        
            if 0 <= gct <=5 : field_frisancho.value = f'Magro, GCT: {gct}%'
            elif 5 < gct <= 15 : field_frisancho.value = f'Grasa debajo del promedio, GCT: {gct}%'  
            elif 15 < gct <= 75 : field_frisancho.value = f'Grasa promedio, GCT: {gct}%'     
            elif 75 < gct <= 85 : field_frisancho.value = f'Grasa arriba del promedio, GCT: {gct}%' 
            elif 85 < gct <= 100 : field_frisancho.value = f'Exceso de grasa, GCT: {gct}%'
            
            container_calculos.update()
        clc = ft.ElevatedButton('Calcula la densidad corporal', on_click=spc_calc,color ='white',bgcolor='blue')
        field_edad = ft.TextField(suffix_text='años',text_align=ft.TextAlign.CENTER,label='Edad',value = edad,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_peso = ft.TextField(suffix_text='kilogramos',text_align=ft.TextAlign.CENTER,label='Peso',value = peso,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_pl_bicipital = ft.TextField(suffix_text='milimetros',text_align=ft.TextAlign.CENTER,label='Pliegue bicipital',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_pl_tricipital = ft.TextField(suffix_text='milimetros',text_align=ft.TextAlign.CENTER,label='Pliegue tricipital',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_pl_suprailiaco = ft.TextField(suffix_text='milimetros',text_align=ft.TextAlign.CENTER,label='Pliegue suprailiaco',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_pl_subescapular = ft.TextField(suffix_text='milimetros',text_align=ft.TextAlign.CENTER,label='Pliegue subescapular',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_densidad_corporal=ft.TextField(text_align=ft.TextAlign.CENTER,label = 'Densidad corporal',read_only=True,width =300, color = 'blue')
        field_grasa_corporal = ft.TextField(text_align=ft.TextAlign.CENTER,label = 'Grasa corporal',read_only=True, width =300, color = 'blue')
        field_masa_grasa = ft.TextField(suffix_text='kilogramos',text_align=ft.TextAlign.CENTER,label = 'Masa grasa',read_only=True, width =300, color = 'blue')
        field_masa_libre_grasa = ft.TextField(suffix_text='kilogramos',text_align=ft.TextAlign.CENTER,label = 'Masa libre grasa',read_only=True, width =300, color = 'blue')
        field_suma_pliegues = ft.TextField(suffix_text='milimetros',text_align=ft.TextAlign.CENTER,label = 'Suma pliegues',read_only=True, width =300, color = 'blue')
        field_frisancho = ft.TextField(text_align=ft.TextAlign.CENTER,label = 'Tabla Frisancho',read_only=True, width =300, color = 'blue')
        hombre_mujer = ft.Slider(min=0, max=1, divisions=1,active_color='blue', inactive_color='red',thumb_color='green', width=20,value = 0,on_change=spc_calc)
        
       
        
        container_calculos.content= ft.Column([
                                            ft.Row([ft.Text('Cálculo de la composición corporal y porcentaje de grasa',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Divider(height=2, color = 'black'),
                                            ft.Row([field_edad,field_peso],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_pl_bicipital,field_pl_tricipital,field_pl_suprailiaco,field_pl_subescapular],ft.MainAxisAlignment.CENTER),
                                            ft.Row([ft.Text('Hombre  '),hombre_mujer,ft.Text('  Mujer')],ft.MainAxisAlignment.CENTER),
                                            ft.Row([clc],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_suma_pliegues, field_grasa_corporal,field_densidad_corporal,],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_frisancho,field_masa_grasa, field_masa_libre_grasa],ft.MainAxisAlignment.CENTER)
                                            ])
        container_calculos.update()    
    #Calculo de ingesta diaria
    def id_clicked(e):
        
        def id_calc(e):
            if field_car.value == '' and field_pro.value == '' and field_lip.value == '' and field_peso.value == '':
               page.open(ft.SnackBar(ft.Text('Tienes que introducir mas datos',color = 'white'), bgcolor='red'))                
            else:
                cal_car = float(field_car.value)*4 if field_car.value != '' else 0
                field_cal_car.value = round(cal_car,2)
                cal_pro = float(field_pro.value)*4 if field_pro.value != '' else 0
                field_cal_pro.value = round(cal_pro,2)
                cal_lip = float(field_lip.value)*9 if field_cal_lip.value != '' else 0
                field_cal_lip.value = round(cal_lip,2)
                peso = float(field_peso.value) if field_peso.value != '' else 1
                field_gr_kg_car.value = round(float(round(cal_car,2))/peso,2) if field_car.value != '' else 0
                field_gr_kg_pro.value = round(float(round(cal_pro,2))/peso,2) if field_pro.value != '' else 0
                field_gr_kg_lip.value = round(float(round(cal_lip,2))/peso,2) if field_lip.value != '' else 0  
                sum_cal= cal_car + cal_pro+ cal_lip
                field_ingesta_calorica.value = sum_cal
                globals()['ingesta_calorica']=sum_cal
                field_pdm_car.value = round(cal_car*100/sum_cal,1)
                field_pdm_pro.value = round(cal_pro*100/sum_cal,1)
                field_pdm_lip.value = round(cal_lip*100/sum_cal,1)
                
            
            if field_des.value == '':field_des.value=0
            if field_mm.value == '':field_mm.value=0
            if field_alm.value == '':field_alm.value=0
            if field_mer.value == '':field_mer.value=0
            if field_cen.value == '':field_cen.value=0
            if float(field_des.value)+float(field_mm.value)+float(field_alm.value)+float(field_mer.value)+float(field_cen.value) != 100:
               page.open(ft.SnackBar(ft.Text('La distribución de ingesta diaria no suma el 100%',color = 'white'), bgcolor='red'))                
            else:
                
                d1 = f'Carbohídratos: {round(round(cal_car,2)*float(field_des.value)/100,1)}Kcal, {round(field_gr_kg_car.value*float(field_des.value)/100,1)}gr/kg peso, {round(field_pdm_car.value*float(field_des.value)/100,1)}%, {round(field_gr_kg_car.value*float(field_des.value)/4,1)}gr\n'
                d2 = f'Proteínas: {round(round(cal_pro,2)*float(field_des.value)/100,1)}Kcal, {round(field_gr_kg_pro.value*float(field_des.value)/100,1)}gr/kg peso, {round(field_pdm_pro.value*float(field_des.value)/100,1)}%, {round(field_gr_kg_pro.value*float(field_des.value)/4,1)}gr\n'
                d3 = f'Lípidos : {round(round(cal_lip,2)*float(field_des.value)/100,1)}Kcal, {round(field_gr_kg_lip.value*float(field_des.value)/100,2)}gr/kg peso, {round(field_pdm_lip.value*float(field_des.value)/100,1)}%, {round(field_gr_kg_lip.value*float(field_des.value)/9,1)}gr\n'
                d4 = f'Total: {round(round(round(cal_car,2)*float(field_des.value)/100,1) + round(round(cal_pro,2)*float(field_des.value)/100,1) + round(round(cal_lip,2)*float(field_des.value)/100,1),2)} Kcal'
                field_cant_des.value = d1+d2+d3+d4
                
                mm1 = f'Carbohídratos: {round(round(cal_car,2)*float(field_mm.value)/100,1)}Kcal, {round(field_gr_kg_car.value*float(field_mm.value)/100,1)}gr/kg peso, {round(field_pdm_car.value*float(field_mm.value)/100,1)}%, {round(field_gr_kg_car.value*float(field_mm.value)/4,1)}gr\n'
                mm2 = f'Proteínas: {round(round(cal_pro,2)*float(field_mm.value)/100,1)}Kcal,  {round(field_gr_kg_pro.value*float(field_mm.value)/100,1)}gr/kg peso, {round(field_pdm_pro.value*float(field_mm.value)/100,1)}%, {round(field_gr_kg_pro.value*float(field_mm.value)/4,1)}gr\n'
                mm3 = f'Lípidos: {round(round(cal_lip,2)*float(field_mm.value)/100,1)}Kcal,{round(field_gr_kg_lip.value*float(field_mm.value)/100,2)}gr/kg peso, {round(field_pdm_lip.value*float(field_mm.value)/100,1)}%,  {round(field_gr_kg_lip.value*float(field_mm.value)/9,1)}gr\n'
                m4 = f'Total: {round(round(round(cal_car,2)*float(field_mm.value)/100,1) + round(round(cal_pro,2)*float(field_mm.value)/100,1) + round(round(cal_lip,2)*float(field_mm.value)/100,1),2)} Kcal'
                field_cant_mm.value = mm1+mm2+mm3+m4
                
                a1 = f'Carbohídratos: {round(round(cal_car,2)*float(field_alm.value)/100,1)}Kcal, {round(field_gr_kg_car.value*float(field_alm.value)/100,1)}gr/kg peso, {round(field_pdm_car.value*float(field_alm.value)/100,1)}%, {round(field_gr_kg_car.value*float(field_alm.value)/4,1)}gr\n'
                a2 = f'Proteínas: {round(round(cal_pro,2)*float(field_alm.value)/100,1)}Kcal, {round(field_gr_kg_pro.value*float(field_alm.value)/100,1)}gr/kg peso, {round(field_pdm_pro.value*float(field_alm.value)/100,1)}%, {round(field_gr_kg_pro.value*float(field_alm.value)/4,1)}gr\n'
                a3 = f'Lípidos: {round(round(cal_lip,2)*float(field_alm.value)/100,1)}Kcal,  {round(field_gr_kg_lip.value*float(field_alm.value)/100,2)}gr/kg peso, {round(field_pdm_lip.value*float(field_alm.value)/100,1)}%, {round(field_gr_kg_lip.value*float(field_alm.value)/9,1)}gr\n'
                a4 = f'Total: {round(round(round(cal_car,2)*float(field_alm.value)/100,1) + round(round(cal_pro,2)*float(field_alm.value)/100,1) + round(round(cal_lip,2)*float(field_alm.value)/100,1),2)} Kcal'
                field_cant_alm.value = a1+a2+a3+a4
       
                mer1 = f'Carbohídratos: {round(round(cal_car,2)*float(field_mer.value)/100,1)}Kcal, {round(field_gr_kg_car.value*float(field_mer.value)/100,1)}gr/kg peso, {round(field_pdm_car.value*float(field_mer.value)/100,1)}%, {round(field_gr_kg_car.value*float(field_mer.value)/4,1)}gr\n'
                mer2 = f'Proteínas: {round(round(cal_pro,2)*float(field_mer.value)/100,1)}Kcal, {round(field_gr_kg_pro.value*float(field_mer.value)/100,1)}gr/kg peso, {round(field_pdm_pro.value*float(field_mer.value)/100,1)}%, {round(field_gr_kg_pro.value*float(field_mer.value)/4,1)}gr\n'
                mer3 = f'Lípidos: {round(round(cal_lip,2)*float(field_mer.value)/100,1)}Kcal, {round(field_gr_kg_lip.value*float(field_mer.value)/100,2)}gr/kg peso, {round(field_pdm_lip.value*float(field_mer.value)/100,1)}%, {round(field_gr_kg_lip.value*float(field_mer.value)/9,1)}gr\n'
                mer4 = f'Total: {round(round(round(cal_car,2)*float(field_mer.value)/100,1) + round(round(cal_pro,2)*float(field_mer.value)/100,1) + round(round(cal_lip,2)*float(field_mer.value)/100,1),2)} Kcal'
                field_cant_mer.value = mer1+mer2+mer3+mer4
                
                cen1 = f'Carbohídratos: {round(round(cal_car,2)*float(field_cen.value)/100,1)}Kcal, {round(field_gr_kg_car.value*float(field_cen.value)/100,1)}gr/kg peso, {round(field_pdm_car.value*float(field_cen.value)/100,1)}%, {round(field_gr_kg_car.value*float(field_cen.value)/4,1)}gr\n'
                cen2 = f'Proteínas:   {round(round(cal_pro,2)*float(field_cen.value)/100,1)}Kcal, {round(field_gr_kg_pro.value*float(field_cen.value)/100,1)}gr/kg peso,{round(field_pdm_pro.value*float(field_cen.value)/100,1)}%, {round(field_gr_kg_pro.value*float(field_cen.value)/4,1)}gr\n'
                cen3 = f'Lípidos: {round(round(cal_lip,2)*float(field_cen.value)/100,1)}Kcal, {round(field_gr_kg_lip.value*float(field_cen.value)/100,2)}gr/kg peso, {round(field_pdm_lip.value*float(field_cen.value)/100,1)}%, {round(field_gr_kg_lip.value*float(field_cen.value)/9,1)}gr\n'
                cen4 = f'Total: {round(round(round(cal_car,2)*float(field_cen.value)/100,1) + round(round(cal_pro,2)*float(field_cen.value)/100,1) + round(round(cal_lip,2)*float(field_cen.value)/100,1),2)} Kcal'
                field_cant_cen.value = cen1+cen2+cen3+cen4
            
            container_calculos.update()
        clc = ft.ElevatedButton('Cálcula ingesta diaria', on_click=id_calc,color ='white',bgcolor='blue')
        
        field_peso = ft.TextField(suffix_text='kilogramos',text_align=ft.TextAlign.CENTER,label='Peso',width = 300)
        
        field_car = ft.TextField(suffix_text='gramos',text_align=ft.TextAlign.CENTER,label = 'Carbohídratos',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width =300)
        field_pro = ft.TextField(suffix_text='gramos',text_align=ft.TextAlign.CENTER,label = 'Proteínas',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width =300)
        field_lip = ft.TextField(suffix_text='gramos',text_align=ft.TextAlign.CENTER,label = 'Lípidos',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width =300)
        
        field_cal_car = ft.TextField(suffix_text='Kilocalorias',text_align=ft.TextAlign.CENTER,label = 'Carbohídratos',read_only=True,width =300, color = 'blue')
        field_cal_pro = ft.TextField(suffix_text='Kilocalorias',text_align=ft.TextAlign.CENTER,label = 'Proteínas',read_only=True,width =300, color = 'blue')
        field_cal_lip = ft.TextField(suffix_text='Kilocalorias',text_align=ft.TextAlign.CENTER,label = 'Lípidos',read_only=True,width =300, color = 'blue')
        field_gr_kg_car = ft.TextField(suffix_text='gr/kg peso',text_align=ft.TextAlign.CENTER,label = 'Carbohídratos',read_only=True,width =300, color = 'blue')
        field_gr_kg_pro = ft.TextField(suffix_text='gr/kg peso',text_align=ft.TextAlign.CENTER,label = 'Proteínas',read_only=True,width =300, color = 'blue')
        field_gr_kg_lip = ft.TextField(suffix_text='gr/kg peso',text_align=ft.TextAlign.CENTER,label = 'Lípidos',read_only=True,width =300, color = 'blue')
        field_pdm_car = ft.TextField(suffix_text='% distribución',text_align=ft.TextAlign.CENTER,label = 'Carbohídratos consumidos',read_only=True,width =300, color = 'blue')
        field_pdm_pro = ft.TextField(suffix_text='% distribución',text_align=ft.TextAlign.CENTER,label = 'Proteínas consumidas',read_only=True,width =300, color = 'blue')
        field_pdm_lip = ft.TextField(suffix_text='% distribución',text_align=ft.TextAlign.CENTER,label = 'Lípidos consumidos',read_only=True,width =300, color = 'blue')
        
        field_ingesta_calorica = ft.TextField(suffix_text='Kilocalorias',text_align=ft.TextAlign.CENTER,label = 'Ingesta calórica IC',value=ingesta_calorica,read_only=True,width =300,)
        
        field_des = ft.TextField(suffix_text='% distribución',text_align=ft.TextAlign.CENTER,label = 'Ingesta diaria desayuno',width =300,)
        field_mm = ft.TextField(suffix_text='% distribución',text_align=ft.TextAlign.CENTER,label = 'Ingesta diaria media mañana',width =300,)
        field_alm = ft.TextField(suffix_text='% distribución',text_align=ft.TextAlign.CENTER,label = 'Ingesta diaria almuerzo',width =300,)
        field_mer = ft.TextField(suffix_text='% distribución',text_align=ft.TextAlign.CENTER,label = 'Ingesta diaria merienda',width =300,)
        field_cen = ft.TextField(suffix_text='% distribución',text_align=ft.TextAlign.CENTER,label = 'Ingesta diaria cena',width =300,)
        field_cant_des = ft.TextField(label = 'Desayuno',read_only=True,width =500, color = 'blue',multiline=True,min_lines=4)
        field_cant_mm = ft.TextField(label = 'Media mañana',read_only=True,width =500, color = 'blue',multiline=True,min_lines=4)
        field_cant_alm = ft.TextField(label = 'Almuerzo',read_only=True,width =500, color = 'blue',multiline=True,min_lines=4)
        field_cant_mer = ft.TextField(label = 'Merienda',read_only=True,width =500, color = 'blue',multiline=True,min_lines=4)
        field_cant_cen = ft.TextField(label = 'Cena',read_only=True,width =500, color = 'blue',multiline=True,min_lines=4)
        
        
        
        container_calculos.content= ft.Column([
                                            ft.Row([ft.Text('Cálculo de ingesta diaria de macronutrientes en la dieta',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Divider(height=2, color = 'black'),
                                            ft.Row([field_car,field_pro,field_lip,field_peso],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_des,field_mm,field_alm,field_mer,field_cen],ft.MainAxisAlignment.CENTER),
                                            ft.Row([clc],ft.MainAxisAlignment.CENTER),
                                            ft.Row([ft.Text('Calorías correspondiente al consumo de macronutrientes',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),                                              
                                            ft.Row([field_cal_car,field_cal_pro,field_cal_lip,field_ingesta_calorica],ft.MainAxisAlignment.CENTER),
                                            ft.Row([ft.Text('Cantidad de gramos de macronutrientes por kilogramo de peso',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_gr_kg_car,field_gr_kg_pro,field_gr_kg_lip],ft.MainAxisAlignment.CENTER),
                                            ft.Row([ft.Text('Porcentaje (%) de distribución de los macronutrientes consumidos',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_pdm_car,field_pdm_pro,field_pdm_lip],ft.MainAxisAlignment.CENTER),
                                            ft.Row([ft.Text('Distribución de los macronutrientes por comidas',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Column([
                                                ft.Row([field_cant_des,field_cant_alm,field_cant_cen],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_cant_mm,field_cant_mer],ft.MainAxisAlignment.CENTER),
                                            ])
                                               
                                               ])
        container_calculos.update()
    #calculo peso ideal, peso corregido, TMB     
    def pi_clicked(e):
        
        def pi_calc(e):
            if field_edad.value == '' or field_altura.value == '' or field_peso.value == 0:
               page.open(ft.SnackBar(ft.Text('Tienes que introducir mas datos',color = 'white'), bgcolor='red'))               
            else:
                edad = float(field_edad.value) if field_edad.value != '' else 0
                altura = float(field_altura.value) if field_altura.value != '' else 0
                peso = float(field_peso.value) if field_peso.value != '' else 0
                mod = ecuacion.value
                peso_ideal = 0
                if mod == 'Lorentz':
                    if hombre_mujer.value== 0:    
                        peso_ideal = round(altura - 100 - ((altura -150)/4) + ((edad-20)/4),1)
                    if hombre_mujer.value== 1:    
                        peso_ideal = round(altura - 100 - ((altura -150)/4) + ((edad-20)/2.5),1)   
                elif mod == 'El índice de Brocca' :
                        peso_ideal = round(altura - 100,1)
                elif mod == 'Metropolitan Life Insurance Company':     
                    peso_ideal = round(50 + 0.75*(altura - 150),1)
                field_pi.value = peso_ideal
                peso_corregido = round(peso_ideal + 0.25*(peso-peso_ideal),1)
                field_pc.value =  peso_corregido  
                if hombre_mujer.value== 1:
                    if 18 <= edad <= 30 : tmb = 14.7*peso_corregido+496
                    elif 30 < edad <= 60 : tmb =8.7*peso_corregido+829
                    elif edad >60 : tmb = 10.5*peso_corregido+596
                elif hombre_mujer.value== 0:
                    if 18 <= edad <= 30 : tmb = 15.3*peso_corregido+679
                    elif 30 < edad <= 60 : tmb =11.6*peso_corregido+879
                    elif edad >60 : tmb = 13.5*peso_corregido+478
                field_tmb.value = round(tmb,1)
                dormido = float(field_t_dormido.value) if field_t_dormido.value != '' else 0
                cp = float(field_t_cp.value) if field_t_cp.value != '' else 0
                comiendo = float(field_t_comiendo.value) if field_t_comiendo.value != '' else 0
                cocinando = float(field_t_cocinando.value) if field_t_cocinando.value !='' else 0
                sentado= float(field_t_sentado.value) if field_t_sentado.value != '' else 0
                trabajo = float(field_t_trabajo.value) if field_t_trabajo.value != '' else 0
                conducir =float(field_t_conducir.value) if field_t_conducir.value !='' else 0
                caminar = float(field_t_caminar.value) if field_t_caminar.value != '' else 0
                actividades = float(field_t_actividades.value) if field_t_actividades.value !='' else 0
                if dormido+cp+comiendo+cocinando+sentado+trabajo+conducir+caminar+actividades != 24:
                   page.open(ft.SnackBar(ft.Text('Las actividades no ocupan los 24h del dia',color = 'white'), bgcolor='red'))                    
                pal = round((dormido*1 + cp*2.3 + comiendo*1.5 + cocinando*2.1 + sentado*1.5 + trabajo*2.8 + conducir*2 + caminar*3.2 + actividades*1.4) / 24 ,2)
                par = round(dormido*1 + cp*2.3 + comiendo*1.5 + cocinando*2.1 + sentado*1.5 + trabajo*2.8 + conducir*2 + caminar*3.2 + actividades*1.4,1)
                field_par.value = par if par !=  0.0 else ''
                pal_v=''
                if 1.4 <= pal < 1.7: pal_v = 'Estilo de vida sedentario o de actividad ligera'
                elif 1.7 <= pal < 2: pal_v = 'Estilo de vida activo o moderadamente activo'
                elif 2 <= pal < 2.4: pal_v = 'Estilo de vida vigoroso o vigorosamente activo'
                field_pal.value = f'{pal_v}, vlaor PAL: {pal}' if pal !=  0.0 else ''
                if ec.value =='Método factorial FAO / OMS / ONU':
                    get = tmb*pal    
                else:
                    if hombre_mujer.value ==0:
                        get= (10*peso)+(6.25*altura)-(5*edad)+5
                    elif hombre_mujer.value == 1:
                        get = (10*peso)+(6.25+altura)-(5*edad) -161
                field_get.value = round(get,1) if get !=  0.0 else ''
                eta = round(0.1*get,1)
                field_get_eta.value=round(get + eta,1) if round(get + eta,1) !=  0.0 else ''
                field_be.value = round(float(field_ic.value)-get,1) if field_ic.value != '' else 'No datos de ingesta calórica'
                field_eta.value = eta
                container_calculos.update()
        clc = ft.ElevatedButton('Calcula peso ideal y peso corregido', on_click=pi_calc,color ='white',bgcolor='blue')
        field_edad = ft.TextField(suffix_text='años',text_align=ft.TextAlign.CENTER,label='Edad',value= edad,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_peso = ft.TextField(suffix_text='kilogramos',text_align=ft.TextAlign.CENTER,label='Peso',value = peso,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_altura= ft.TextField(suffix_text='centimetros',text_align=ft.TextAlign.CENTER,label='Altura',value = altura,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_pi = ft.TextField(suffix_text='kilogramos',text_align=ft.TextAlign.CENTER,label = 'Peso ideal',read_only=True,width =300, color = 'blue')
        field_pc = ft.TextField(suffix_text='kilogramos',text_align=ft.TextAlign.CENTER,label = 'Peso corregido',read_only=True,width =300, color = 'blue')
        field_tmb = ft.TextField(text_align=ft.TextAlign.CENTER,label = 'Tasa metabólica basal TMB',read_only=True,width =300, color = 'blue')
        ecuacion =  ft.Dropdown(
            on_change=pi_calc,
            label='Cálculo de peso ideal segun',
            options=[
                ft.dropdown.Option("Lorentz"),
                ft.dropdown.Option("El índice de Brocca"),
                ft.dropdown.Option("Metropolitan Life Insurance Company"),
            ],
            width=320,
        )
        ec =  ft.Dropdown(
            on_change=pi_calc,
            label='Metodo calculo gasto energetico total',
            options=[
                ft.dropdown.Option("Método factorial FAO / OMS / ONU"),
                ft.dropdown.Option("Método ecuación Mark Mifflin y Sachiko St Jeor"),
            
            ],
            width=450,
        )
        hombre_mujer = ft.Slider(min=0, max=1, divisions=1,active_color='blue', inactive_color='red',thumb_color='green', width=20,value = 0,on_change=pi_calc)
        
        field_t_dormido = ft.TextField(suffix_text='horas',text_align=ft.TextAlign.CENTER,label='Dormido',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_t_cp = ft.TextField(suffix_text='horas',text_align=ft.TextAlign.CENTER,label = 'Cuidado personal (vestirse, ducharse)',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width =300)
        field_t_comiendo = ft.TextField(suffix_text='horas',text_align=ft.TextAlign.CENTER,label = 'Comiendo',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width =300)
        field_t_cocinando = ft.TextField(suffix_text='horas',text_align=ft.TextAlign.CENTER,label = 'Cocinando',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width =300)
        field_t_sentado = ft.TextField(suffix_text='horas',text_align=ft.TextAlign.CENTER,label = 'Sentado (trabajo sentado...)',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width =300)
        field_t_trabajo = ft.TextField(suffix_text='horas',text_align=ft.TextAlign.CENTER,label = 'Trabajo domestico general',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width =300)
        field_t_conducir  = ft.TextField(suffix_text='horas',text_align=ft.TextAlign.CENTER,label = 'Conducir coche haciá /desde el trabajo',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width =300)
        field_t_caminar  = ft.TextField(suffix_text='horas',text_align=ft.TextAlign.CENTER,label = 'Caminar a diferentes ritmos sin carga',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width =300)
        field_t_actividades = ft.TextField(suffix_text='horas',text_align=ft.TextAlign.CENTER,label = 'Actividades livianas de ocio(TV, charlar...)',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width =300)
        
        field_par = ft.TextField(suffix_text='kilocalorias',text_align=ft.TextAlign.CENTER,label='Coste energetico (PAR)',read_only=True,width=300, color = 'blue')
        field_pal = ft.TextField(text_align=ft.TextAlign.CENTER,label='PAL',read_only=True,width=550, color = 'blue')
        field_get = ft.TextField(suffix_text='kilocalorias',text_align=ft.TextAlign.CENTER,label='Gasto energético total',read_only=True,width=280, color = 'blue')
        field_get_eta  = ft.TextField(suffix_text='kilocalorias',text_align=ft.TextAlign.CENTER,label='Gasto energético total con ETA',read_only=True,width=320, color = 'blue')
        field_ic= ft.TextField(suffix_text='Kilocalorias',text_align=ft.TextAlign.CENTER,label='Ingesta calórica IC',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 320)
        field_be = ft.TextField(suffix_text='kilocalorias',text_align=ft.TextAlign.CENTER,label='Balance energético',read_only=True,width=250, color = 'blue')
        field_eta = ft.TextField(suffix_text='kilocalorias',text_align=ft.TextAlign.CENTER,label='ETA*',read_only=True,width=200, color = 'blue')
        container_calculos.content= ft.Column([
                                                ft.Row([ft.Text('Cálculo de peso ideal y peso corregido, tasa metabólica basal TMB, gasto energetico total',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                                ft.Divider(height=2, color = 'black'),
                                                ft.Row([field_edad,field_altura,field_peso],ft.MainAxisAlignment.CENTER),
                                                ft.Row([ecuacion,field_ic],ft.MainAxisAlignment.CENTER),
                                                ft.Row([field_t_dormido,field_t_cp,field_t_comiendo],ft.MainAxisAlignment.CENTER),
                                                ft.Row([field_t_cocinando,field_t_sentado,field_t_trabajo],ft.MainAxisAlignment.CENTER),
                                                ft.Row([field_t_conducir,field_t_caminar,field_t_actividades],ft.MainAxisAlignment.CENTER),
                                                ft.Row([ec],ft.MainAxisAlignment.CENTER),
                                                ft.Row([ft.Text('Hombre  '),hombre_mujer,ft.Text('  Mujer')],ft.MainAxisAlignment.CENTER),
                                                ft.Row([clc],ft.MainAxisAlignment.CENTER),
                                                ft.Row([field_pi,field_pc,field_tmb],ft.MainAxisAlignment.CENTER),
                                               
                                                ft.Row([ft.Text('PAL es la media que determinamos a partir del factor de actividad física, nos ayuda para estimar de una forma más simplificada el Gasto Energético Total del paciente',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                                ft.Row([ft.Text('Para calcular PAL debe sumar el resultado del “Tiempo x coste energético',weight='bold', color = 'blue'),ft.Text('(factor de activiad)(PAR)”', color = 'red'),ft.Text('por cada actividad y dividirlo entre 24',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                                
                                                ft.Row([field_par,field_pal],ft.MainAxisAlignment.CENTER),
                                                ft.Row([ft.Text('Recuerda que la ecuacion de balance energético es BE= ingesta calórica - gasto energético total (GET)',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                                ft.Row([field_get,field_eta,field_get_eta,field_be],ft.MainAxisAlignment.CENTER),
                                                ft.Row([ft.Text('*ETA - Efefcto termico de los alimentos',size = 12, color = 'red')],ft.MainAxisAlignment.CENTER),
                                                ])
        container_calculos.update()
    #Cálculo de requerimientos diarios de carbohidratos/proteinas/lipidos en la dieta
    def rq_carbohidratos_clicked(e):
        def rq_calc(e):
            
            if field_get.value == '' or field_peso.value == '' or field_pdm_car.value == '' or (field_pdm_lip.value == '' and field_pdm_pro.value == '' and field_gr_kg_pro.value == ''):
               page.open(ft.SnackBar(ft.Text('Tienes que introducir mas datos',color = 'white'), bgcolor='red'))
            else:
                peso = float(field_peso.value) 
                '''rq_car = float(field_get.value)*/4  if field_get.value != '' else 0
                field_rq_car.value = round(rq_car,2) '''
                rq_pro = float(field_gr_kg_pro.value)*peso if field_gr_kg_pro.value !='' else 0
                field_pro.value = round(rq_pro,2)
                '''rq_lip = float(field_get.value)*9 if field_get.value != '' else 0
                field_rq_lip.value = round(rq_lip,2)'''
                
                
                field_car.value = round((float(field_get.value)*float(field_pdm_car.value)/100)/4,2) if field_pdm_car.value != '' else 0
                field_gr_kg_car.value = round(field_car.value/peso,1)
                field_rq_car.value =  round(field_car.value * 4)
                if field_pdm_pro.value =='' and field_pro.value != 0 :
                    field_rq_pro.value = field_pro.value * 4
                    field_pdm_pro.value = round(float(field_rq_pro.value)*100/float(field_get.value),1) 
                elif field_pdm_pro.value == '' and field_gr_kg_pro.value == '' and field_pdm_lip.value != '' and field_pdm_car.value != '':
                    field_pdm_pro.value = int(100 - float(field_pdm_car.value) - float(field_pdm_lip.value))
                    field_rq_pro.value = round((float(field_get.value)*float(field_pdm_pro.value))/100,1)
                    field_pro.value  = round(float(field_rq_pro.value)/4,1)
                    field_gr_kg_pro.value = round(float(field_pro.value)/peso,2)
                else:
                    field_pro.value = round((float(field_get.value)*float(field_pdm_pro.value)/100)/4,2)
                    field_gr_kg_pro.value = round(field_pro.value/peso,2)
                    field_rq_pro.value = field_pro.value * 4
                if field_pdm_lip.value == '':
                    field_pdm_lip.value = int(100 - float(field_pdm_pro.value) - float(field_pdm_car.value)) if field_pdm_pro.value != '' and field_pdm_car.value != '' else 0
                    field_rq_lip.value = round((float(field_get.value)*float(field_pdm_lip.value))/100,1)
                    field_lip.value  = round(float(field_rq_lip.value)/9,1)
                    field_gr_kg_lip.value = round(float(field_lip.value)/peso,2)
                else:
                    field_lip.value = round((float(field_get.value)*float(field_pdm_lip.value)/100)/9,1) 
                    field_gr_kg_lip.value = round(field_lip.value/peso,2)
                    field_rq_lip.value = round(field_lip.value * 9)
                '''if field_pdm_car.value == '': field_pdm_car.value = 0
                if field_pdm_pro.value == '': field_pdm_pro.value = 0
                if field_pdm_lip.value == '': field_pdm_lip.value = 0
                if field_pdm_car.value + field_pdm_pro.value + field_pdm_lip.value != 100:
                       page.open(ft.SnackBar(ft.Text('La distribucion de macronutrientes no alcanza el 100%',color = 'white'), bgcolor='red'))'''
                #field_gr_kg_pro.value = round(float(field_pro.value)/peso,2) if field_pro.value != '' else 0
                #field_gr_kg_lip.value = round(float(field_lip.value)/peso,2) if field_lip.value != '' else 0  
                '''sum_rq= rq_car + rq_pro+ rq_lip
                field_pdm_car.value = round(rq_car*100/sum_rq,1)
                field_pdm_pro.value = round(rq_pro*100/sum_rq,1)
                field_pdm_lip.value = round(rq_lip*100/sum_rq,1)'''
                
                container_calculos.update()
        clc = ft.ElevatedButton('Cálcula requerimientos diarios', on_click=rq_calc,color ='white',bgcolor='blue' )
        n_clc = ft.ElevatedButton('Nuevo calculo', on_click=rq_carbohidratos_clicked,color ='white',bgcolor='blue' )
        field_peso = ft.TextField(suffix_text='Kilogramos',text_align=ft.TextAlign.CENTER,label='Peso',value = peso,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        
        field_car = ft.TextField(suffix_text='gramos',text_align=ft.TextAlign.CENTER,label = 'Carbohídratos',read_only=True,width =300, color = 'blue')
        field_pro = ft.TextField(suffix_text='gramos',text_align=ft.TextAlign.CENTER,label = 'Proteínas',read_only=True,width =300, color = 'blue')
        field_lip = ft.TextField(suffix_text='gramos',text_align=ft.TextAlign.CENTER,label = 'Lípidos',read_only=True,width =300, color = 'blue')
        field_get = ft.TextField(label = 'Gasto energetico total GET (Kcal)',width =300,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_rq_car = ft.TextField(suffix_text='Kilocalorias',text_align=ft.TextAlign.CENTER,label = 'Carbohídratos',read_only=True,width =300, color = 'blue')
        field_rq_pro = ft.TextField(suffix_text='Kilocalorias',text_align=ft.TextAlign.CENTER,label = 'Proteínas',read_only=True,width =300, color = 'blue')
        field_rq_lip = ft.TextField(suffix_text='Kilocalorias',text_align=ft.TextAlign.CENTER,label = 'Lípidos',read_only=True,width =300, color = 'blue')
        field_gr_kg_car = ft.TextField(suffix_text='gr/kg peso',text_align=ft.TextAlign.CENTER,label = 'Carbohídratos',read_only=True,width =300, color = 'blue')
        field_gr_kg_pro = ft.TextField(suffix_text='gr/kg peso',text_align=ft.TextAlign.CENTER,label = 'Proteínas',width =300,)
        field_gr_kg_lip = ft.TextField(suffix_text='gr/kg peso',text_align=ft.TextAlign.CENTER,label = 'Lípidos',read_only=True,width =300, color = 'blue')
        field_pdm_car = ft.TextField(suffix_text='%',text_align=ft.TextAlign.CENTER,label = 'Carbohídtratos',width =300,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_pdm_pro = ft.TextField(suffix_text='%',text_align=ft.TextAlign.CENTER,label = 'Proteínas',width =300,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_pdm_lip = ft.TextField(suffix_text='%',text_align=ft.TextAlign.CENTER,label = 'Lípidos',width =300,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        
        container_calculos.content= ft.Column([
                                            ft.Row([ft.Text('Cálculo de requerimientos diarios de carbohidratos/proteinas/lipidos en la dieta',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Divider(height=2, color = 'black'),
                                            ft.Row([ft.Text('Primero, debes elegir el porcentaje de carbohidratos/proteinas/lipidos que tu paciente debe consumir diariamente. Para ello, puedes utilizar algunas referencias de las grandes entes de salud y nutrición',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Row([
                                            ft.Column([ft.Row([ft.Text('Carbohidratos : ',weight='bold', color = 'blue'),ft.Text('50 - 75 % VCT - OMS 2003\n50 - 60 % VCT - NIH/ATPIII 2002\n40 - 50 % - NAS 2002\n45 - 65 % VCT - FAO')],ft.MainAxisAlignment.CENTER)]),
                                            ft.Column([ft.Text(' ')]),
                                            ft.Column([ft.Row([ft.Text('Proteinas : ',weight='bold', color = 'blue'),ft.Text('10 - 15 % VCT - OMS 2003\n15 % VCT - NIH/ATPIII 2002\n10 - 35 % - NAS 2002\n1 - 1,2 gr/kg VCT - FAO')],ft.MainAxisAlignment.CENTER)]),
                                            ft.Column([ft.Text(' ')]),
                                            ft.Column([ft.Row([ft.Text('Lipidos : ',weight='bold', color = 'blue'),ft.Text('15 - 30 % VCT - OMS 2003\n20 - 35 % VCT - NIH/ATPIII 2002\n20 - 35 % - NAS 2002\n15 - 35 % VCT - FAO')],ft.MainAxisAlignment.CENTER)]),
                                            ],ft.MainAxisAlignment.CENTER),
                                            ft.Row([ft.Text('Sabiendo la distribucion de Carbohidratos y Proteinas la distribucion de Lipidos se calcula automaticamente',weight='bold', color = 'red')],ft.MainAxisAlignment.CENTER),
                                            ft.Divider(height=2, color = 'black'),
                                            ft.Row([field_peso,field_get],ft.MainAxisAlignment.CENTER),
                                            ft.Row([ft.Text('Porcentaje (%) de distribución de los macronutrientes consumidos',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_pdm_car,field_pdm_pro,field_pdm_lip],ft.MainAxisAlignment.CENTER),
                                            ft.Row([clc],ft.MainAxisAlignment.CENTER),
                                            ft.Row([ft.Text('Kilocalorías correspondiente al consumo de macronutrientes',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),                                              
                                            ft.Row([field_rq_car,field_rq_pro,field_rq_lip],ft.MainAxisAlignment.CENTER),                                            
                                            ft.Row([ft.Text('Cantidad de gramos de macronutrientes necesarios',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_car,field_pro,field_lip],ft.MainAxisAlignment.CENTER),
                                            ft.Row([ft.Text('Cantidad de gramos de macronutrientes por kilogramo de peso',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_gr_kg_car,field_gr_kg_pro,field_gr_kg_lip],ft.MainAxisAlignment.CENTER),
                                            #ft.Row([n_clc],ft.MainAxisAlignment.END),                                                  
                                               ])
        container_calculos.update()
    ############
    def diet(e):
        def calculos(e):
            if field_des.value =='' : field_des.value = 0
            if field_mm.value =='' : field_mm.value = 0
            if field_alm.value =='' : field_alm.value = 0
            if field_mer.value =='' : field_mer.value = 0
            if field_cen.value =='' : field_cen.value = 0
            
            if field_kcal_total.value == '':
               page.open(ft.SnackBar(ft.Text('Tienes que introducir el total en Kcalorias a repartir',color = 'white'), bgcolor='red'))
            elif float(field_des.value)+float(field_mm.value)+float(field_alm.value)+float(field_mer.value)+float(field_cen.value) != 100:
               page.open(ft.SnackBar(ft.Text('El procentaje de distribucion de la ingesta diaria no alcanza el 100%',color = 'white'), bgcolor='red'))
            else:
                kcal_des = round(float(field_des.value)/100*float(field_kcal_total.value),1)
                kcal_des_carb = round((float(field_des_car.value)/100)*kcal_des,1) if field_des_car.value != '' else 0
                kcal_des_pro = round((float(field_des_pro.value)/100)*kcal_des,1) if field_des_pro.value != '' else 0
                kcal_des_lip = round((float(field_des_lip.value)/100)*kcal_des,1) if field_des_lip.value != '' else 0
                gr_des_carb = round(kcal_des_carb/4,1)
                gr_des_pro = round(kcal_des_pro/4,1)
                gr_des_lip = round(kcal_des_lip/9,1)
                
                kcal_mm = round(float(field_mm.value)/100*float(field_kcal_total.value),1)
                kcal_mm_carb = round(float(field_mm_car.value)/100*kcal_mm,1) if field_mm_car.value != '' else 0
                kcal_mm_pro = round(float(field_mm_pro.value)/100*kcal_mm,1) if field_mm_pro.value != '' else 0
                kcal_mm_lip = round(float(field_mm_lip.value)/100*kcal_mm,1) if field_mm_lip.value != '' else 0
                gr_mm_carb = round(kcal_mm_carb/4,1)
                gr_mm_pro = round(kcal_mm_pro/4,1)
                gr_mm_lip = round(kcal_mm_lip/9,1)
                
                kcal_alm = round(float(field_alm.value)/100*float(field_kcal_total.value),1)
                kcal_alm_carb = round(float(field_alm_car.value)/100*kcal_alm,1) if field_alm_car.value != '' else 0
                kcal_alm_pro = round(float(field_alm_pro.value)/100*kcal_alm,1) if field_alm_pro.value != '' else 0
                kcal_alm_lip = round(float(field_alm_lip.value)/100*kcal_alm,1) if field_alm_lip.value != '' else 0
                gr_alm_carb = round(kcal_alm_carb/4,1)
                gr_alm_pro = round(kcal_alm_pro/4,1)
                gr_alm_lip = round(kcal_alm_lip/9,1)
                
                kcal_mer = round(float(field_mer.value)/100*float(field_kcal_total.value),1)
                kcal_mer_carb = round(float(field_mer_car.value)/100*kcal_mer,1) if field_mer_car.value != '' else 0
                kcal_mer_pro = round(float(field_mer_pro.value)/100*kcal_mer,1) if field_mer_pro.value != '' else 0
                kcal_mer_lip = round(float(field_mer_lip.value)/100*kcal_mer,1) if field_mer_lip.value != '' else 0
                gr_mer_carb = round(kcal_mer_carb/4,1)
                gr_mer_pro = round(kcal_mer_pro/4,1)
                gr_mer_lip = round(kcal_mer_lip/9,1)
                
                kcal_cen = round(float(field_cen.value)/100*float(field_kcal_total.value),1)
                kcal_cen_carb = round(float(field_cen_car.value)/100*kcal_cen,1) if field_cen_car.value != '' else 0
                kcal_cen_pro = round(float(field_cen_pro.value)/100*kcal_cen,1) if field_cen_pro.value != '' else 0
                kcal_cen_lip = round(float(field_cen_lip.value)/100*kcal_cen,1) if field_cen_lip.value != '' else 0
                gr_cen_carb = round(kcal_cen_carb/4,1)
                gr_cen_pro = round(kcal_cen_pro/4,1)
                gr_cen_lip = round(kcal_cen_lip/9,1)
                
                field_cant_des.value= f'Carbohidratos: {gr_des_carb} gr → {kcal_des_carb} kcal\nProteinas: {gr_des_pro} gr → {kcal_des_pro} kcal\nLipidos: {gr_des_lip} gr → {kcal_des_lip} kcal'
                field_cant_mm.value = f'Carbohidratos: {gr_mm_carb } gr → {kcal_mm_carb} kcal\nProteinas: {gr_mm_pro} gr → {kcal_mm_pro} kcal\nLipidos: {gr_mm_lip } gr → {kcal_mm_lip} kcal'
                field_cant_alm.value= f'Carbohidratos: {gr_alm_carb} gr → {kcal_alm_carb} kcal\nProteinas: {gr_alm_pro} gr → {kcal_alm_pro} kcal\nLipidos: {gr_alm_lip }gr → {kcal_alm_lip} kcal'
                field_cant_mer.value= f'Carbohidratos: {gr_mer_carb} gr → {kcal_mer_carb} kcal\nProteinas: {gr_mer_pro} gr → {kcal_mer_pro} kcal\nLipidos: {gr_mer_lip} gr → {kcal_mer_lip} kcal'
                field_cant_cen.value= f'Carbohidratos: {gr_cen_carb} gr → {kcal_cen_carb} kcal\nProteinas: {gr_cen_pro} gr → {kcal_cen_pro} kcal\nLipidos: {gr_cen_lip }gr → {kcal_cen_lip} kcal'
                
                container_calculos.update()
        field_kcal_total = ft.TextField(label = 'Gasto energetico total GET (Kcal)',width =300,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
       
        field_des = ft.TextField(label = 'Desayuno',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_des_car=ft.TextField(label = 'Desayuno',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_des_pro=ft.TextField(label = 'Desayuno',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_des_lip=ft.TextField(label = 'Desayuno',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        
        field_mm = ft.TextField(label = 'Media mañana',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_mm_car=ft.TextField(label = 'Media mañana',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_mm_pro=ft.TextField(label = 'Media mañana',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_mm_lip=ft.TextField(label = 'Media mañana',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        
        field_alm = ft.TextField(label = 'Almuerzo',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_alm_car=ft.TextField(label = 'Almuerzo',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_alm_pro=ft.TextField(label = 'Almuerzo',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_alm_lip=ft.TextField(label = 'Almuerzo',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        
        field_mer = ft.TextField(label = 'Merienda',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_mer_car=ft.TextField(label = 'Merienda',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_mer_pro=ft.TextField(label = 'Merienda',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_mer_lip=ft.TextField(label = 'Merienda',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        
        field_cen = ft.TextField(label = 'Cena',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_cen_car=ft.TextField(label = 'Cena',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_cen_pro=ft.TextField(label = 'Cena',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        field_cen_lip=ft.TextField(label = 'Cena',width =200,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),)
        
        
        field_cant_des = ft.TextField(label = 'Desayuno',read_only=True,width =350,text_style=ft.TextStyle(weight='bold',color = 'blue'),multiline=True,min_lines=3)
        field_cant_mm = ft.TextField(label = 'Media mañana',read_only=True,width =350,text_style=ft.TextStyle(weight='bold',color = 'blue'),multiline=True,min_lines=3)
        field_cant_alm = ft.TextField(label = 'Almuerzo',read_only=True,width =350,text_style=ft.TextStyle(weight='bold',color = 'blue'),multiline=True,min_lines=3)
        field_cant_mer = ft.TextField(label = 'Merienda',read_only=True,width =350,text_style=ft.TextStyle(weight='bold',color = 'blue'),multiline=True,min_lines=3)
        field_cant_cen = ft.TextField(label = 'Cena',read_only=True,width =350,text_style=ft.TextStyle(weight='bold',color = 'blue'),multiline=True,min_lines=3)
        clc = ft.ElevatedButton('Cálcula', on_click=calculos,color ='white',bgcolor='blue' )
        
        container_calculos.content= ft.Column([
                                            ft.Row([ft.Text('Cálculo de ....',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Divider(height=2, color = 'black'),
                                            ft.Row([field_kcal_total],ft.MainAxisAlignment.CENTER),
                                            ft.Row([ft.Text('Distribución de ingesta diaria a lo largo del dia %',weight='bold',color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_des,field_mm,field_alm,field_mer,field_cen],ft.MainAxisAlignment.CENTER),
                                            ft.Divider(height=2, color = 'black'),
                                            ft.Row([ft.Text('Primero, debes elegir el porcentaje de carbohidratos que tu paciente debe consumir diariamente. Para ello, puedes utilizar algunas referencias de las grandes entes de salud y nutrición',weight='bold', color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Row([
                                            ft.Column([ft.Row([ft.Text('Carbohidratos : ',weight='bold', color = 'blue'),ft.Text('50 - 75 % VCT - OMS 2003\n50 - 60 % VCT - NIH/ATPIII 2002\n40 - 50 % - NAS 2002\n45 - 65 % VCT - FAO')],ft.MainAxisAlignment.CENTER)]),
                                            ft.Column([ft.Text(' ')]),
                                            ft.Column([ft.Row([ft.Text('Proteinas : ',weight='bold', color = 'blue'),ft.Text('10 - 15 % VCT - OMS 2003\n15 % VCT - NIH/ATPIII 2002\n10 - 35 % - NAS 2002\n1 - 1,2 gr/kg VCT - FAO')],ft.MainAxisAlignment.CENTER)]),
                                            ft.Column([ft.Text(' ')]),
                                            ft.Column([ft.Row([ft.Text('Lipidos : ',weight='bold', color = 'blue'),ft.Text('15 - 30 % VCT - OMS 2003\n20 - 35 % VCT - NIH/ATPIII 2002\n20 - 35 % - NAS 2002\n15 - 35 % VCT - FAO')],ft.MainAxisAlignment.CENTER)]),
                                            ],ft.MainAxisAlignment.CENTER),
                                            ft.Divider(height=2, color = 'black'),
                                            ft.Row([ft.Text('Distribución de Carbohidratos a lo lagro del dia %',weight='bold',color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_des_car,field_mm_car,field_alm_car,field_mer_car,field_cen_car],ft.MainAxisAlignment.CENTER),
                                            ft.Row([ft.Text('Distribución de Proteinas a lo lagro del dia %',weight='bold',color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_des_pro,field_mm_pro,field_alm_pro,field_mer_pro,field_cen_pro],ft.MainAxisAlignment.CENTER),
                                            ft.Row([ft.Text('Distribución de Lipidos a lo lagro del dia %',weight='bold',color = 'blue')],ft.MainAxisAlignment.CENTER),
                                            ft.Row([field_des_lip,field_mm_lip,field_alm_lip,field_mer_lip,field_cen_lip],ft.MainAxisAlignment.CENTER),
                                            ft.Row([clc],ft.MainAxisAlignment.CENTER),
                                            ft.Divider(height=2, color = 'black'),
                                            ft.Row([
                                                ft.Column([field_cant_des]),
                                                ft.Column([field_cant_mm]),
                                                ft.Column([field_cant_alm]),
                                                ft.Column([field_cant_mer]),
                                                ft.Column([field_cant_cen]),
                                            ],ft.MainAxisAlignment.CENTER)
                                               ])
        container_calculos.update()
    def datos(e):
        def calc(e):
            globals()['peso'] = int(field_peso.value)
            globals()['altura'] = int(field_altura.value)
            globals()['edad'] = int(field_edad.value)
        field_peso = ft.TextField(label='Introduce el peso (kg)',value = peso,input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]"),width = 300)
        field_altura = ft.TextField(label='Introduce altura (cm)',value = altura,input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 300)
        field_edad = ft.TextField(label='Introduce edad',input_filter=ft.InputFilter(allow=False, regex_string=r"[a-zñç|A-ZÑÇ|,|*|\\|º|/|+|<|>|:|;|_|!|@|`|´|¡|'|¿|?|=|)|(|/|&|%$|·|\"|!|ª|#|~|€|¬|{|}|[|]||^]", replacement_string=""),width = 200)
        field_imc = ft.TextField(label = 'Índice de masa corporal',value=indice_masa_corporal,read_only=True,width = 300, color = 'blue')
        clc = ft.ElevatedButton('Set', on_click=calc,color ='white',bgcolor='blue')
        container_calculos.content= ft.Column([
              ft.Row([field_peso,field_altura,field_edad],ft.MainAxisAlignment.CENTER),
              ft.Row([clc],ft.MainAxisAlignment.CENTER),
              ft.Row([field_imc],ft.MainAxisAlignment.CENTER),
                ])
        container_calculos.update()
    #######################3
    # Tablas M/C
    def tablas_mc(e):
        cl = ft.Column(spacing=10,  width = 800,  scroll=ft.ScrollMode.ALWAYS,  on_scroll_interval=0,)
        for n in range(1,7):
            cl.controls.append(ft.Image(src=f'info/dc{n}.png',width = 800,))
        #[ft.Image(src=f'info/dc{n}.png',width =1200, height=790) for n in range(1,7)]#width =1190, height=1290
       
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('La densidad corporal es la relación entre la masa y el volumen del cuerpo. Existen diferentes fórmulas para calcular la densidad corporal, en este caso utilizaremos la ecuación de Durnin y Womersley',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text('Densidad Corporal (DC) = C - [M X Log (Suma Pliegues)]',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text('C y M representan unas constantes que puedes encontrar en la siguientes tablas, ten en cuenta que, el valor de estas constantes depende del sexo del paciente y el número de pliegues que le fueron tomados',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([cl],alignment=ft.MainAxisAlignment.CENTER),
                                    ])
        container_calculos.update()
    # Tablas Frisnacho
    def tablas_frisnacho(e):
        cl = ft.Column(spacing=10,  width = 800,  scroll=ft.ScrollMode.ALWAYS,  on_scroll_interval=0,)
        for n in range(1,3):
            cl.controls.append(ft.Image(src=f'info/fr{n}.png',width = 800,))
        #[ft.Image(src=f'info/dc{n}.png',width =1200, height=790) for n in range(1,7)]#width =1190, height=1290
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Tablas Frisnacho',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text('Para interpretar el resultado del cálculo puedes utilizar las tablas de Frisancho, que indica los percentiles de porcentaje de grasa corporal, con respecto a la edad y sexo del paciente',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text('Estos percentiles te ayudan a ubicar qué tan cerca del “promedio normal”se encuentra tu paciente en cuanto a su porcentaje de grasa',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([cl],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text('Luego de ubicar el percentil de tu paciente debes dirigirte a la siguiente tabla de Frisancho que te ayuda a interpretar los resultados',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/fr3.png',width = 800)],alignment=ft.MainAxisAlignment.CENTER)
                                    ])
        container_calculos.update()
    # Cálculo de peso ideal y de peso corregido
    def formulas_pi(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Cálculo de peso ideal y de peso corregido',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    #ft.Row([ft.Text('El peso ideal se calcula, principalmente, en función de la altura del paciente, sin embargo,\nen algunas formulas también se utiliza la edad y sexo, como podemos observar en la ecuación de Lorentz, la cual recomendamos utilizar por su mayor especificidad',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/formulas_pi_pc.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Signos clinicos comunes
    def signos_clinicos(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Signos clinicos comunes',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    #ft.Row([ft.Text('A continuación, te presentaré algunos signos clínicos que te pueden orientar hacia alguna posible alteración nutricional.\nEsta tabla que verás a continuación es suministrada por la FAO',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/signos_clinicos12.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER),
                                    #ft.Row([ft.Text('Tipo de carencias nutricionales asociados',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    #ft.Row([ft.Text('Ahora, que ya conoces los signos clínicos más comunes, podrás identificar a qué tipo de carencias nutricionales están asociados.\nA continuación, te invito a revisar la siguiente tabla proporcionada por la FAO',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    #ft.Row([ft.Image(src=f'info/carencia_nutricional.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Aplicación de evaluación dietética
    def aed(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Aplicación de evaluación dietética',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/aed.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Cálculo de ingesta diaria de macronutrientes en la dieta
    def cid(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Cálculo de ingesta diaria de macronutrientes en la dieta',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/cid.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Índices antropométricos
    def imc(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Índices antropométricos',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text('Los índices antropométricos son valores de dimensión y composición corporal que nos indican el contenido graso y muscular presente en el cuerpo.\n Son muy útiles porque funcionan como predictores del estado nutricional, y de los factores de riesgo como enfermedades cardiovasculares, diabetes, dislipidemias, entre otros. ',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/imc.png')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text('clasificación del IMC',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/clasificacion_imc.png')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text('Circunferencia abdominal (CA)',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text('Es un indicador indirecto de la presencia de grasa intraabdominal o visceral.\nSu principal función es predecir el riesgo de enfermedades crónicas asociadas al sobrepeso u obesidad, como lo son las cardiovasculares y la diabetes.',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/circumferencia_abdominal.png',)],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text('Índice cintura/cadera (C/C)',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text('El Índice de cintura/cadera evalúa de forma indirecta la grasa abdominal del paciente.\nEste es un método predictivo del riesgo cardiometabólico. Para determinar este índice dividimos el perímetro de la cintura entre el perímetro de la cadera.',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/icc.png')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Text('Luego, se utiliza la tabla de “criterios de evaluación de riesgos” para analizar el riesgo cardiovascular.',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/cer.jpeg',)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    
                                    ])
        container_calculos.update()
    # Composición corporal del cuerpo humano
    def comp(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Composición corporal del cuerpo humano',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/comp.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Toma de medidas antropométricas en el paciente
    def med_ant(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Toma de medidas antropométricas en el paciente',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/med_ant.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Balance energético
    def bal_en(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Balance energético',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/bal_en.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Gasto energético
    def gasto_en(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Gasto energético',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/gasto_en.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Calculo gasto energético
    def calc_gasto_en(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Gasto energético',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/calc_gasto_en.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Espectro de los carbohidratos    
    def espectro_carb(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Espectro de los carbohidratos',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/esp_carb.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Cálculo de requerimientos diarios de carbohidratos en la dieta
    def calc_carb(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Cálculo de requerimientos diarios de carbohidratos en la dieta',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/calc_carb.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Proteínas vegetales y animales
    def proteinas(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Proteínas vegetales y animales',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/proteinas.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Cálculo de requerimientos diarios de proteínas en la dieta
    def calc_pro(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Cálculo de requerimientos diarios de proteínas en la dieta',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/calc_pro.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Grasas dietéticas y sus efectos en la salud humana
    def lipidos(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Grasas dietéticas y sus efectos en la salud humana',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/lipidos.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Cálculo de requerimientos diarios de lípidos en la dieta
    def calc_lip(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Cálculo de requerimientos diarios de lípidos en la dieta',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/calc_lip.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Vitaminas liposolubles (Rhoades y Tarner; Fisiología Médica, Masson 1997)
    def vitaminas_liposolubles(e):
        
        container_calculos.content=ft.Column([
                                    ft.Row([ft.Text('Vitaminas liposolubles (Rhoades y Tarner; Fisiología Médica, Masson 1997)',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/vitaminas_liposolubles.png',width =1200, height=800)],alignment=ft.MainAxisAlignment.CENTER)
                                        ])
        container_calculos.update()
    # Ingestas recomendadas de las vitaminas hidrosolubles
    def vitaminas_hidrosolubles(e):
        
        
        container_calculos.content=ft.Column([
                                    ft.Row([ft.Text('Ingestas recomendadas de las vitaminas hidrosolubles',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),                                    
                                    ft.Row([ft.Image(src=f'info/vitaminas_hidrosolubles.png',width =1200, height=800)],alignment=ft.MainAxisAlignment.CENTER)
                                    ])
        container_calculos.update()
    # Minerales esenciales, beneficios, fuentes y recomendaciones diarias
    def minerales_esenciales(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Minerales esenciales, beneficios, fuentes y recomendaciones diarias. Fundación Nemours / KidsHealth, Revisado por: Mary L. Gavin, MD 2014',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/minerales_esenciales.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Intervención nutricional
    def interv_nutr(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Intervención nutricional',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/interv_nutr.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Horarios de comida
    def horario_comida(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Horarios de comida',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/horario_comida.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Distribución de macronutrientes por tiempos de comida
    def dist_macro(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Distribución de macronutrientes por tiempos de comida',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/dist_macro.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # Creación de un menú saludable
    def menu_sal(e):
        
        container_calculos.content= ft.Column([
                                    ft.Row([ft.Text('Creación de un menú saludable',weight='bold', color = 'blue')],alignment=ft.MainAxisAlignment.CENTER),
                                    ft.Row([ft.Image(src=f'info/menu_sal.png',width =1200)],alignment=ft.MainAxisAlignment.CENTER)#width =1190, height=1290
                                    ])
        container_calculos.update()
    # exit
    def salir(e):
        page.window.destroy()
    # about
    def about(e):
        def close_dlg(*args):
                    dlg_modal.open = False
                    page.update()
        dlg_modal = ft.AlertDialog(
            modal=False,
            title=ft.Text('Acerca de', text_align='center',size=24),
            content=ft.Text(spans= [ft.TextSpan('Hecho con ❤️ por Alexandru G. Muntenas para mi esposa\n'), ft.TextSpan('alexandru.muntenas@gmail.com',on_click=lambda _:page.launch_url('mailto:alexandru.muntenas@gmail.com'),style=ft.TextStyle(color='red',weight=ft.FontWeight.W_400))], size=14,italic = True, text_align='center'),
            actions=[ft.TextButton('Ok', on_click=close_dlg),], actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=close_dlg
                    )
                
            
       
        page.overlay.append(dlg_modal)
        dlg_modal.open = True
        page.update()
        
    '''page.appbar = ft.AppBar(
        leading=ft.PopupMenuButton(
                icon = ft.icons.MENU,
                tooltip='Calculos',
                items=[
                    ft.PopupMenuItem(text="Cálculo de índice de masa corporal",on_click=imc_clicked),
                    ft.PopupMenuItem(text="Cálculo riesgo diabete en funcion de circumferencia abdominal",on_click=cabd_clicked),
                    ft.PopupMenuItem(text="Índice de cintura y cadera",on_click=icc_clicked),
                    ft.PopupMenuItem(text="Cálculo de la composición corporal y porcentaje de grasa",on_click=spc_clicked),
                    ft.PopupMenuItem(text="Cálculo de peso ideal y peso corregido, tasa metabólica basal TMB, gasto energetico total",on_click=pi_clicked),
                    ft.PopupMenuItem(text="Cálculo de ingesta diaria de macronutrientes en la dieta",on_click=id_clicked),                    
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(text="Cálculo de requerimientos diarios de carbohidratos/proteinas/lipidos en la dieta",on_click=rq_carbohidratos_clicked),       
                    ft.PopupMenuItem(text="Cálculo dieta",on_click=diet),                
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(text="Salir",on_click=salir),
                ]
            ),
        leading_width=40,
        title=ft.Text("Calculos nutricion"),
        center_title=False,
        bgcolor=ft.colors.BLUE,
        actions=[
            #ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            #ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                icon = ft.icons.INFO_OUTLINE,
                tooltip='Valoracción nutricional',
                items=[
                    
                    ft.PopupMenuItem(text="Tablas constante M y C",on_click=tablas_mc),
                    ft.PopupMenuItem(text="Tablas de Frisnacho",on_click=tablas_frisnacho),
                    ft.PopupMenuItem(text="Formulas de calculo peso ideal",on_click=formulas_pi),
                    ft.PopupMenuItem(text="Formula de calculo peso corregido",on_click=formulas_pc),
                    ft.PopupMenuItem(text="Signos clinicos",on_click=signos_clinicos),          
                    ft.PopupMenuItem(text="Índices antropométricos",on_click=imc),    
                    ft.PopupMenuItem(text="Composición corporal del cuerpo humano",on_click=comp),   
                    ft.PopupMenuItem(text="Toma de medidas antropométricas en el paciente",on_click=med_ant), 
                    ft.PopupMenuItem(text="Balance energético",on_click=bal_en), 
                    ft.PopupMenuItem(text="Gasto energético",on_click=gasto_en),
                    ft.PopupMenuItem(text="Cálculo gasto energético",on_click=calc_gasto_en),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(text="Salir",on_click=salir),
                ]
            ),
             ft.PopupMenuButton(
                icon = ft.icons.INFO,
                tooltip='Estudio de los nutrientes',
                items=[
                   
                   
                    ft.PopupMenuItem(text="Espectro de los carbohidratos",on_click=espectro_carb),
                    ft.PopupMenuItem(text="Cálculo de requerimientos diarios de carbohidratos en la dieta",on_click=calc_carb), 
                    ft.PopupMenuItem(text="Proteínas vegetales y animales",on_click=proteinas),
                    ft.PopupMenuItem(text="Cálculo de requerimientos diarios de proteínas en la dieta",on_click=calc_pro), 
                    ft.PopupMenuItem(text="Grasas dietéticas y sus efectos en la salud humana",on_click=lipidos),
                    ft.PopupMenuItem(text="Cálculo de requerimientos diarios de lípidos en la dieta",on_click=calc_lip),
                    ft.PopupMenuItem(text="Vitaminas liposolubles",on_click=vitaminas_liposolubles),
                    ft.PopupMenuItem(text="Vitaminas hidrosolubles",on_click=vitaminas_hidrosolubles),   
                    ft.PopupMenuItem(text="Minerales esenciales",on_click=minerales_esenciales), 
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(text="Intervención nutricional",on_click=interv_nutr),
                    ft.PopupMenuItem(text="Horarios de comida",on_click=horario_comida),
                    ft.PopupMenuItem(text="Distribución de macronutrientes por tiempos de comida",on_click=dist_macro),
                    ft.PopupMenuItem(text="Creación de un menú saludable",on_click=menu_sal),
                    
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(text="Salir",on_click=salir),
                ]
            ),
           
            
        ],
    )'''
    
    def bde(e):
        url='https://www.bedca.net/bdpub/index.php'
        page.launch_url(url)
        
    ##############################
    menubar = ft.MenuBar(
        expand=True,        
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.colors.PURPLE_100,
            mouse_cursor={ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                          ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
        ),
        
        controls=[
            ft.SubmenuButton(
                content=ft.IconButton(icon=ft.icons.HOME,on_click=display),
            ),            
            ft.SubmenuButton(
                content=ft.Text("Calculos"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text('Cálculo de índice de masa corporal'),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}),
                        on_click=imc_clicked
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Cálculo riesgo diabete en funcion de circumferencia abdominal"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}),
                        on_click=cabd_clicked
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Índice de cintura y cadera"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}),
                        on_click=icc_clicked
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Cálculo de la composición corporal y porcentaje de grasa"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}),
                        on_click=spc_clicked
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Cálculo de peso ideal y peso corregido, tasa metabólica basal TMB, gasto energetico total"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}),
                        on_click=pi_clicked
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Cálculo de ingesta diaria de macronutrientes en la dieta"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}),
                        on_click=id_clicked
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Cálculo de requerimientos diarios de carbohidratos/proteinas/lipidos en la dieta"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}),
                        on_click=rq_carbohidratos_clicked
                    ),
                    #ft.MenuItemButton(
                    #    content=ft.Text("Cálculo dieta"),
                    #    style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}),
                    #    on_click=diet
                   # ),
                   
                ]
            ),
            
            ft.SubmenuButton(
                content=ft.Text("Info"),
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("Valoracción nutricional"),
                        leading=ft.Icon(ft.icons.INFO),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Tablas constante M y C"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=tablas_mc
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Tablas de Frisnacho"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=tablas_frisnacho
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Cálculo de peso ideal y  de peso corregido"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=formulas_pi
                            ),
                            #ft.MenuItemButton(
                            #    content=ft.Text("Formula de calculo peso corregidoFormula de calculo peso corregido"),
                             #   close_on_click=True,
                              #  style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                              #  on_click=formulas_pc
                           # ),
                            ft.MenuItemButton(
                                content=ft.Text("Signos clinicos"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=signos_clinicos
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Aplicación de evaluación dietética"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=aed
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Cálculo de ingesta diaria de macronutrientes en la dieta"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=cid
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Índices antropométricos"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=imc
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Composición corporal del cuerpo humano"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=comp
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Toma de medidas antropométricas en el paciente"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=med_ant
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Balance energético"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=bal_en
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Gasto energético"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=gasto_en
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Cálculo gasto energético"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=calc_gasto_en
                            ),
                            
                        ]
                    ),
                                 
                    ft.SubmenuButton(
                        content=ft.Text("Estudio de los nutrientes"),
                        leading=ft.Icon(ft.icons.INFO),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Espectro de los carbohidratos"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=espectro_carb
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Cálculo de requerimientos diarios de carbohidratos en la dieta"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=calc_carb
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Proteínas vegetales y animales"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=proteinas
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Cálculo de requerimientos diarios de proteínas en la dieta"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=calc_pro
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Grasas dietéticas y sus efectos en la salud humana"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=lipidos
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Cálculo de requerimientos diarios de lípidos en la dieta"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=calc_lip
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Vitaminas liposolubles"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=vitaminas_liposolubles
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Vitaminas hidrosolubles"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=vitaminas_hidrosolubles
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Minerales esenciales"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=minerales_esenciales
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Intervención nutricional"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=interv_nutr
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Horarios de comida"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=horario_comida
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Distribución de macronutrientes por tiempos de comida"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=dist_macro
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Creación de un menú saludable"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=menu_sal
                            ),
                        ]
                        
                    ),
                    ft.Divider(),
                    ft.MenuItemButton(
                        content=ft.Text("Base de Datos Española de Composición de Alimentos"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}),
                        on_click=bde
                    ),
                    ft.Divider(),
                    ft.MenuItemButton(
                                content=ft.Text("Acerca de"),
                                close_on_click=True,
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200}),
                                on_click=about
                    ),
                   
                ]
            ),
            ft.SubmenuButton(content=ft.Text("",expand=True),),
            #ft.SubmenuButton(content=ft.IconButton(on_click=salir,icon=ft.icons.EXIT_TO_APP),),
            #ft.SubmenuButton(content=ft.IconButton(on_click=datos,icon=ft.icons.DATA_ARRAY),)
        ]
    )
                 

    #container_calculos.alignment=ft.alignment.top_center
    page.add(ft.Row([menubar,],alignment=ft.MainAxisAlignment.CENTER),  
                        
        ft.Column([container_calculos],height=830,scroll=ft.ScrollMode.AUTO, on_scroll_interval=0)
        )
    display('')
ft.app(target=main,assets_dir='assets',view=ft.AppView.WEB_BROWSER)

''' ft.Divider(),
                    ft.MenuItemButton(
                        content=ft.Text("Salir"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}),
                        on_click=salir
                    ),'''
