class QuizBrain:

    def __init__(self,lista_preguntas):
        self.pregunta_nro = 0
        self.lista = lista_preguntas
        self.puntaje = 0
    
    def siguiente_pregunta(self):
        pregunta_actual = self.lista[self.pregunta_nro]
        self.pregunta_nro += 1
        respuesta_usuario = input(f"P1. {self.pregunta_nro}: {pregunta_actual.text} (True/False): ")
        self.check_respuesta(respuesta_usuario,pregunta_actual.answer)

    def hay_preguntas(self):
        return self.pregunta_nro < len(self.lista)
    
    def check_respuesta(self,respuesta_usuario,respuesta_correcta):
        if respuesta_usuario.lower() == respuesta_correcta.lower():
            self.puntaje += 1
            print("Tu respuesta es correcta!")
        else:
            print("La respuesta es incorrecta!")
        print(f"La respuesta correcta era {respuesta_correcta}")
        print(f"Tu actual puntaje es de {self.puntaje}/{self.pregunta_nro} preguntas!")
        print("\n")

