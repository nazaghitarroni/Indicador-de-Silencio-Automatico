import pyautogui
import cv2
import numpy as np
import time
import requests

template_muted = cv2.imread("imagenes/mic-muted.png", 0)
template_unmuted = cv2.imread("imagenes/mic-unmuted.png", 0)

w, h = template_muted.shape[::-1]
last_state = None

while True:
    screenshot = pyautogui.screenshot()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    res_muted = cv2.matchTemplate(screenshot_cv, template_muted, cv2.TM_CCOEFF_NORMED)
    _, max_val_muted, _, _ = cv2.minMaxLoc(res_muted)

    res_unmuted = cv2.matchTemplate(screenshot_cv, template_unmuted, cv2.TM_CCOEFF_NORMED)
    _, max_val_unmuted, _, _ = cv2.minMaxLoc(res_unmuted)

    threshold = 0.7

    if max_val_muted >= threshold or max_val_unmuted >= threshold:
        if max_val_muted > max_val_unmuted:
            current_state = "MUTEADO"
            confidence = max_val_muted
        else:
            current_state = "DESMUTEADO"
            confidence = max_val_unmuted

        if current_state != last_state:
            last_state = current_state
            print(f"Micrófono {current_state} (confianza: {confidence:.2f})")

            try:
                if current_state == "MUTEADO":
                    requests.get("http://192.168.0.120:8080/linterna-on")
                else:
                    requests.get("http://192.168.0.120:8080/linterna-off")
            except Exception as e:
                print("Error al contactar al celular:", e)

    else:
        print("No se detectó claramente ningún estado")

    time.sleep(2)
