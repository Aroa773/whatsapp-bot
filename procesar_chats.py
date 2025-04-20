from leer_chats import leer_chat

def procesar_chats_en_carpeta(carpeta):
    import os
    import pandas as pd
    df_total = pd.DataFrame()

    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            ruta = os.path.join(carpeta, archivo)
            df = leer_chat(ruta)
            df['chat'] = archivo.replace(".txt", "")
            df_total = pd.concat([df_total, df], ignore_index=True)

    return df_total

if __name__ == "__main__":
    df_final = procesar_chats_en_carpeta("chats_whatsapp")
    df_final.to_csv("datos_whatsapp.csv", index=False)
    print("✅ Chat procesado y guardado en datos_whatsapp.csv")

