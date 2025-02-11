#-El chatbot responde basándose en palabras clave que detecta en la entrada del usuario.
#-El cahtbot sigue funcionando hasta que el usuario dice "adiós" o "chao".
def chatbot():
    print("Hola, soy un chatbot simple. ¿En qué puedo ayudarte?")
    
    while True:
        #El chatbot toma la entrada del usuario a través de "input()".
        user_input = input("Tú: ").lower()
        
        if "hola" in user_input:
            print("Chatbot: ¡Hola! ¿Cómo estás?")
        elif "cómo estás" in user_input:
            print("Chatbot: Estoy bien, gracias por preguntar. ¿Y tú?")
        elif "adiós" in user_input or "chao" in user_input:
            print("Chatbot: ¡Adiós! Que tengas un buen día.")
            break
        elif "nombre" in user_input:
            print("Chatbot: Soy un chatbot simple, no tengo nombre.")
        elif "ayuda" in user_input:
            print("Chatbot: Puedo ayudarte con preguntas simples. Intenta preguntarme algo.")
        else:
            print("Chatbot: Lo siento, no entiendo eso. ¿Puedes intentar preguntar de otra manera?")

if __name__ == "__main__":
    chatbot()