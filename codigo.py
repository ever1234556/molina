import gradio as gr

def generar_codigo(prompt):
    prompt = prompt.lower()

    if "html" in prompt:
        return """<!DOCTYPE html>
<html>
<head>
<title>Mi Página</title>
</head>
<body>
<h1>Hola Mundo</h1>
<p>Tu IA funciona correctamente</p>
</body>
</html>"""

    elif "python" in prompt:
        return 'print("Hola Mundo")'

    elif "javascript" in prompt:
        return 'console.log("Hola Mundo");'

    else:
        return "Pide código HTML, Python o JavaScript"

demo = gr.Interface(
    fn=generar_codigo,
    inputs=gr.Textbox(label="Pide cualquier código"),
    outputs=gr.Code(label="Código generado"),
    title="🚀 Mi IA Programadora REAL"
)

demo.launch()