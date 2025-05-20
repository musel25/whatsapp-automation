"""
Send a WhatsApp message from Python with pywhatkit
Prereqs:
  1.  pip install pywhatkit
  2.  Chrome/Edge/Firefox already logged-in to WhatsApp Web
  3.  Keep your PC awake while the script runs
"""

import pywhatkit as kit
import time

PHONE   = "+39 331 318 7687"          # <-- full number with country code, no spaces
MESSAGE = '''Hi, my name is Musel Tabares, a student at UPT with experience building websites. I noticed your business doesn’t seem to have a website on Google Maps, and I believe having one could really boost your visibility and credibility.

Since I’m a student, I can create a clean, professional website for a very low cost—just enough to support my studies. I’d be happy to share examples and tailor it to your style and needs.

If you're interested or have any questions, feel free to reply or call me directly. I'd love to help!

'''  
WAIT    = 10                     # seconds to wait while WhatsApp Web loads

try:
    # open WhatsApp Web, wait, paste, send, close tab
    kit.sendwhatmsg_instantly(
        phone_no   = PHONE,
        message    = MESSAGE,

        wait_time  = WAIT,   # default is 15 s – use a bit more on slow links
        tab_close  = True,   # close the browser tab after sending
        close_time = 3       # seconds to wait *after* the message is sent
    )
    print("✅  Message queued – watch the browser tab do its thing.")
except Exception as err:
    print(f"⚠️  Couldn’t send: {err}")
    # give yourself a moment to read the error if it happens inside the browser
    time.sleep(10)
