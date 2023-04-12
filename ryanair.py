import http.client

class datos_api:

    def vuelos():

        conn = http.client.HTTPSConnection("ryanair.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "INTRODUCIR CLAVE API",
            'X-RapidAPI-Host': "ryanair.p.rapidapi.com"
        }

        conn.request("GET", "/flights?origin_code=LGW&destination_code=DUB&origin_departure_date=2023-09-28&destination_departure_date=2023-10-28", headers=headers)

        res = conn.getresponse()
        data = res.read()

        return data.decode("utf-8")