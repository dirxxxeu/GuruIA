
import openai
#change for your API KEY | cambia por tu api key
openai.api_key = "API_KEY"


def ask_openai(prompt):

    completions = openai.Completion.create(

        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message


def image_openai(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response["data"][0]["url"]
    return image_url



print("Bienvenido al asistente de preguntas de GuruIA.")
answer = ''
while answer != '0':



    answer = input('''Elige una de las tres opciones \n
        1) Pregunta 
        2) Imagen 
        0) Salir     
    ''')
    if answer =='1':
        answer = input("¿Tienes una pregunta?\n ")
        response = ask_openai(answer)
        print("Respuesta:", response)
    elif answer =='2':
        answer = input("¿Qué imagen deseas?\n")
        response = image_openai(answer)
        print("Enlace: \n", response)
    else:
        answer =='0'
        break


print("\nGracias por usar el asistente de preguntas de GuruIA. ¡Hasta luego!")
