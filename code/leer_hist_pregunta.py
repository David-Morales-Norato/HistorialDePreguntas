from read_files import leer_datos,pd

class leer_datos_historial_pregunta(leer_datos):
    def __init__(self):
        self.NOMBRES_HOJAS = ["CURSOS","CURSOS_ACTIVIDADES","PREGUNTAS"]
        super().__init__()

    def lectura_especifica(self,file_path, tipo):
        try:
            
            archivo_excel = pd.read_excel(file_path, sheet_name=None)
            if(tipo ==1):
                datos = self.lectura_historal_preguntas(archivo_excel)
            else: 
                datos = self.lectura_historial_pregunta_cursos_actividad_específica(archivo_excel)
            return datos
        except Exception as e:
            self.log += str(e)
            return None

    def lectura_historal_preguntas(self, archivo_excel):
        # Leemos las hojas
        cursos_hoja = archivo_excel[self.NOMBRES_HOJAS[0]]

        # Leemos cursos y actividades
        cursos= self.leer_columna(cursos_hoja,"CURSOS_ID")

        
        return [cursos]
    
    def lectura_historial_pregunta_cursos_actividad_específica(self, archivo_excel):
        # Leemos las hojas
        cursos_hoja = archivo_excel[self.NOMBRES_HOJAS[1]]
        preguntas_hoja = archivo_excel[self.NOMBRES_HOJAS[2]]

        # Leemos cursos y actividades
        cursos= self.leer_columna(cursos_hoja,"CURSOS_ID")

        # Leemos cursos y actividades
        actividades= self.leer_columna(cursos_hoja,"ACTIVIDADES")

        

        # Leemos las preguntas
        actividades= self.leer_columna(preguntas_hoja,"PREGUNTAS_ID")

        return [cursos, actividades, actividades]

    def get_log(self):
        return self.log