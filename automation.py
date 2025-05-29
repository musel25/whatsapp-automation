import pandas as pd
import pywhatkit as kit
import time

# Settings
WAIT = 6  # seconds to wait before sending each message
DELAY_BETWEEN_MESSAGES = 7  # seconds to pause between each message

# Load CSV
df = pd.read_csv("places.csv")

# Loop through each contact
for idx, row in df.iterrows():
    name = row['name']
    address = row['address']
    phone = str(row.get('phone', '')).strip()

    print(phone)
    # Skip if phone number is missing
    if not phone.startswith('+'):
        print(f"❌ Skipping {name} — invalid or missing phone number.")
        continue

    # Custom message
#     message = f'''Hi, my name is Musel Tabares, a student at UPT with experience building websites. I noticed your business "{name}" at "{address}" doesn’t seem to have a website on Google Maps, and I believe having one could really boost your visibility and credibility.

# Since I’m a student, I can create a clean, professional website for a very low cost—just enough to support my studies. I’d be happy to share examples and tailor it to your style and needs.

# If you're interested or have any questions, feel free to reply or call me directly. I'd love to help!
# '''
    message = f'''Hola, mi nombre es Musel Tabares, soy estudiante de programación y tengo experiencia creando sitios web. Noté que su negocio "{name}", ubicado en "{address}", no parece tener un sitio web en Google Maps, y creo que tener uno podría aumentar significativamente su visibilidad.

    Como soy estudiante, puedo crearle un sitio web limpio y profesional a un costo muy bajo, solo lo suficiente para apoyar mis estudios. Con gusto puedo mostrarle ejemplos y adaptarlo a su estilo y necesidades.

    Si está interesado o tiene alguna pregunta, no dude en responder o llamarme directamente. ¡Me encantaría ayudarle!
    '''



    try:
        print(f"📨 Sending message to {name} at {phone}...")
        kit.sendwhatmsg_instantly(
            phone_no=phone,
            message=message,
            wait_time=WAIT,
            tab_close=True,
            close_time=5
        )
        print("✅ Message sent.")
    except Exception as err:
        print(f"⚠️ Couldn’t send to {name} ({phone}): {err}")

    # Wait before next message
    time.sleep(DELAY_BETWEEN_MESSAGES)
