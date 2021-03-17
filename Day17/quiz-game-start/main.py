from question_model import Pregunta
from data import question_datav1
from quiz_brain import QuizBrain

banco_preguntas = []
for pregunta in question_datav1:
    banco_preguntas.append(Pregunta(pregunta["question"],pregunta["correct_answer"]))

cerebro = QuizBrain(banco_preguntas)

while cerebro.hay_preguntas():
    cerebro.siguiente_pregunta()

print("Terminaste el questionario.")
print(f"Tu puntaje final es de: {cerebro.puntaje}/{cerebro.pregunta_nro}")