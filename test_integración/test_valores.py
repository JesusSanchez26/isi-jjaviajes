#Test de integración: Al introducir valores de entrada y realizar la búsqueda, 
#la información se muestra correctamente
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_busqueda_vuelos():
    # Iniciar el driver y abrir la página web de la aplicación
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000/buscar")

    # Seleccionar los campos de entrada
    origen = driver.find_element_by_id("origen")
    destino = driver.find_element_by_id("destino")
    fecha = driver.find_element_by_id("fecha")

    # Introducir valores de entrada
    origen.send_keys("Malaga")
    destino.send_keys("Barcelona")

    # Realizar la búsqueda
    buscar_button = driver.find_element_by_id("buscar")
    buscar_button.click()

    # Comprobar que la página resultante muestra la información esperada
    assert "JJA VIAJES" in driver.title
    assert "BCN" in driver.page_source
    assert "AGP" in driver.page_source

    # Cerrar el driver
    driver.close()


#Para ejecutarlo: python -m unittest test_valores.py