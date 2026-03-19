import feedparser
# Configuramos el feed.
url_periodico = "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada"
datos = feedparser.parse(url_periodico)

print(f"Leyendo las noticias de: {datos.feed.title}")

# Se crea y abre el archivo en modo escritura.
with open("noticias.txt", "w", encoding="utf-8") as archivo:

    # Escribimos un encabezado en el archivo
    archivo.write(f"NOTICIAS DE: {datos.feed.title}\n")
    archivo.write("=" * 30 + "\n\n")

    # Bucle para recorrer las noticias
    for noticia in datos.entries[:15]:
        # Imprimimos por consola para ver que se está haciendo bien y lo que se está guardando.
        print(f"Guardando: {noticia.title}")
        
        # Guarda y escribe en el archivo las noticias.
        archivo.write(f"Titulo: {noticia.title}\n")
        archivo.write(f"Link: {noticia.link}\n")
        archivo.write("-" * 30 + "\n")

print("\n¡Listo! Todas las noticias se han guardado en 'noticias.txt'")