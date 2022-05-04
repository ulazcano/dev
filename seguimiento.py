import datetime as datetime

semanas_1 = [
            {
                "semana":"S4",
                "id": 1,
                "num_semana": 4,
                "dias_para_seguimiento": 28*1,
                "dias_para_prox_seguimiento": 28*2,
                "start_date": "",
                "end_date": "",
                "last_date": ""
            },
            {
                "semana":"S8",
                "id": 2,
                "num_semana": 8,
                "dias_para_seguimiento": 28*2,
                "dias_para_prox_seguimiento": 28*3,
                "start_date": "",
                "end_date": "",
                "last_date": ""
            },
            {
                "semana":"S12",
                "id": 3,
                "num_semana": 12,
                "dias_para_seguimiento": 28*3,
                "dias_para_prox_seguimiento": 7*13,
                "start_date": "",
                "end_date": "",
                "last_date": ""
            },
            {
                "semana":"S13",
                "id": 4,
                "num_semana": 13,
                "dias_para_seguimiento": 7*13,
                "dias_para_prox_seguimiento": 7*26,
                "start_date": "",
                "end_date": "",
                "last_date": ""
            },
            {
                "semana":"S26",
                "id": 5,
                "num_semana": 26,
                "dias_para_seguimiento": 7*26,
                "dias_para_prox_seguimiento": 7*39,
                "start_date": "",
                "end_date": "",
                "last_date": ""
            },
            {
                "semana":"S39",
                "id": 6,
                "num_semana": 39,
                "dias_para_seguimiento": 7*39,
                "dias_para_prox_seguimiento": 0,
                "start_date": "",
                "end_date": "",
                "last_date": ""
            }
            ]

class planificacion:
   
    def __init__(self, fechapcr,semanas):
        self.fechapcr = fechapcr
        self.semanas = semanas


# fecha_pcr_str = "2021-04-10"
# # fechas limites 
# # S4 2022-03-31



# date_entry = input('Fecha PCR  (AAAA-MM-DD): ')
# year, month, day = map(int, date_entry.split('-'))
# fecha_pcr = datetime.date(year, month, day)

        #fecha_pcr_str = input("'Fecha PCR  (AAAA-MM-DD): ")
    def listado_fechas(self,seg,date):  
        
 
        fecha_pcr_str = self.fechapcr
        fecha_pcr=datetime.datetime.strptime(fecha_pcr_str, "%Y-%m-%d").date()
        dias_desde_pcr = (datetime.datetime.today().date()- fecha_pcr).days
        semanas_desde_pcr=(dias_desde_pcr/7)
        print('')
        print( 'Días desde PCR: ', dias_desde_pcr)
        print( 'Semanas desde PCR: ', semanas_desde_pcr)
        print('')

        if semanas_desde_pcr < 8:
            semana_inicio_seguimiento = 4

        if semanas_desde_pcr >= 8 and semanas_desde_pcr < 12:
            semana_inicio_seguimiento = 8
        
        if semanas_desde_pcr >= 12: 
            semana_inicio_seguimiento = 12



        #Recorrer diccionario para completar fechas de inicio y cierre de seguimiento
        for semana in self.semanas:
            # Seguimiento con inicio anterior a semana 12 
            if semana_inicio_seguimiento <12:

                # Calculo la fecha de inicio y término para primer seguimiento 
                    
                    if semana_inicio_seguimiento == semana["num_semana"]:
                        
                        if semanas_desde_pcr < 4:
                            semana['start_date'] = fecha_pcr + datetime.timedelta(days=semana['dias_para_seguimiento'])
                        
                        
                        dias_para_prox_seguimiento = abs(dias_desde_pcr - semana["dias_para_prox_seguimiento"])
                        
                        if semanas_desde_pcr >= 4:
                            semana['start_date']=datetime.datetime.today().date()
                                        
                        if dias_para_prox_seguimiento <7 :
                            semana['end_date']= semana['start_date']+ datetime.timedelta(days=semana["dias_para_prox_seguimiento"] - dias_desde_pcr-1)
                        
                        if dias_para_prox_seguimiento >=7 :
                            semana['end_date']= semana['start_date']+ datetime.timedelta(days=6)


                # Calculo la fecha de inicio para el resto de los seguimiento                

                    if semana_inicio_seguimiento < semana["num_semana"]: 
                        semana['start_date'] = fecha_pcr + datetime.timedelta(semana['dias_para_seguimiento'])
                        semana['end_date'] = semana['start_date']+ datetime.timedelta(days=6)
                        
            # Seguimiento con inicio en semana 12            
            else:            

                if  semana["num_semana"] < 12:
                    continue

                elif  semana["num_semana"] == 12:          
                    semana['start_date']=datetime.datetime.today().date()
                    start_date_semana_12=semana['start_date']

                    dias_para_seguimiento_13 = abs(semana["dias_para_prox_seguimiento"] - dias_desde_pcr)
                    
                    if dias_para_seguimiento_13 >= 7 :
                        semana['end_date']= semana['start_date']+ datetime.timedelta(days=6)
                    
                    if dias_para_seguimiento_13 < 7 :
                        semana['end_date']= semana['start_date']+ datetime.timedelta(days=dias_para_seguimiento_13)
                
                else:
                        semana['start_date'] = start_date_semana_12 + datetime.timedelta(days=semana["dias_para_seguimiento"]-84)
                        semana['end_date'] = semana['start_date'] + datetime.timedelta(days=6) 
                    
        #print (semana['semana'],'||',semana['start_date'],'||',semana['end_date'],'||', datetime.timedelta(days=1) + semana['end_date']- semana['start_date'])
        #print('')
        #print(self.semanas)
        return self.semanas

plan=planificacion("2022-04-01",semanas_1)
plan.listado_fechas(1,"start")


#for seguimiento in plan.semanas:
 #   print(seguimiento["start_date"])



#print(semanas_1)
