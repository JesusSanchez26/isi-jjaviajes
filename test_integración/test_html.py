#Test de integración: El html se carga correctamente
from selenium import webdriver

def test_html_loads():
    # Configurar el controlador del navegador
    driver = webdriver.Chrome('C:\Users\Usuario\OneDrive - Universidad de Castilla-La Mancha\Escritorio\Lab ISI')
    driver.implicitly_wait(10)

    # Cargar la página de inicio
    driver.get('http://localhost:5000/')
    #Tambien funcionaría con: driver.get('http://127.0.0.1:5000/')

    # Verificar que el HTML se ha cargado correctamente
    assert '<html>' in driver.page_source

    # Cerrar el navegador
    driver.quit()

    #Para ejecutarlo y probar que funcione poner en la terminal situado en la 
    #carpeta donde este el archivo: python test_html.py
