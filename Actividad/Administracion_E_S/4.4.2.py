import asyncio
import aiofiles

##IMPORTANTE DESCARGAR LA BIBLIOTECA AIOFILES USANDO PIP

#Implementa un programa en Python, C o java que realice operaciones de entrada/salida asíncronas usando archivos.

async def escribir_archivo(nombre_archivo, contenido):
    async with aiofiles.open(nombre_archivo, mode='w') as archivo:
        await archivo.write(contenido)
        print(f"Escrito en el archivo {nombre_archivo}: {contenido}")

async def leer_archivo(nombre_archivo):
    async with aiofiles.open(nombre_archivo, mode='r') as archivo:
        contenido = await archivo.read()
        print(f"Leído desde el archivo {nombre_archivo}: {contenido}")

async def main():
    archivo = "archivo_asincrono.txt"
    
    await escribir_archivo(archivo, "Este es un ejemplo de escritura asíncrona.")
    await leer_archivo(archivo)

if __name__ == "__main__":
    asyncio.run(main())