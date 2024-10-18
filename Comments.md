## Detalles de decisiones tomadas

- En primer lugar, decidi utilizar la base de datos proporcionada por **django** para simplificar lo relacionado a la misma ya que no era necesario profundizar tanto en su uso al tener datos simples.
- Por otro lado decidi hacer uso del **admin** proporcionado nuevamente por **django** para manejar todo lo relacionado a los modelos, tanto la creacion, modificacion y eliminacion de los mismos. No me parecia necesario tener que contruir los endpoints y la logica detras de la manipulacion de los modelos porque no es el enfoque del desafio. Por lo tanto preferi utilizar el admin, por eso es necesario crear un superuser durante el setup, para poder agregar usuarios y pagos.
- No arme un modelo **_Country_** ya que no senti necesario el uso del mismo en profundidad, la unica relacion que se me ocurrio fue que el pago deberia ser en la moneda del cual el usuario es perteneciente. Pero de nuevo, es una logica externa al problema y que no necesariamente es correcta, por lo tanto opte por utilizar un enum. Esto mismo tambien es aplicable a los campos _local_currency_ y _status_ de **_Payment_**, preferi utilizar enums ya que me parecio que era lo mas simple para el problema pedido. Y a la hora de elegir las posibles opciones dentro de los enums me decante en poner pocas, ya que por ejemplo agregar un nuevo estado _in_progress_ no modifica nada en el problema.
- Cuando comence a armar los tests, me vi obligado a modificar la funcion _calculate_total_amount_ dentro de _business_logic.py_ para que no se llame al servicio externo y que tome valores de cambios de moneda distintos cada vez que corre. Por lo tanto agregue un Mock que le envia una funcion prearmada para modificar los valores de amount pero siempre por el mismo valor. Esto fue para poder chequear el correcto funcionamiento de la funcion en si misma.
- Me tome la libertad de crear las 2 funciones que traen la informacion pedida, tanto la cantidad de pagos rechazados en el último día, _get_rejected_payments_, y monto acumulado total (en usd) de pagos por usuario en la última semana, _calculate_total_amount_, para que en lugar de tener fijo los dias, se le envie una valor que puede ser modificado desde _settings.py_ con los valores **DAYS_FOR_REJECTED_PAYMENTS** y **DAYS_FOR_TOTAL_AMOUNT**.
- El servicio externo al cual llamo para conserguir la conversion de las monedas es **Currency Conversion and Exchange Rates**, particularmente solo el endpoint de conversion.
  La llamada tiene la siguiente pinta:

  curl --location 'https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert?from=ARS&to=USD&amount=1000' \
  --header 'x-rapidapi-host: currency-conversion-and-exchange-rates.p.rapidapi.com' \
  --header 'x-rapidapi-key: 821945cee4mshfb3769699c79de2p17d012jsnfde78438b77e'

  Donde _from=ARS_, _to=USD_ y _amount=1000_ son los parametros puestos como ejemplo.

  Los casos de respuesta son los siguientes:

  .Caso positivo:
  ```json
  {
    "success": true,
    "query": {
      "from": "ARS",
      "to": "USD",
      "amount": 1000
    },
    "info": {
      "timestamp": 1729291997,
      "rate": 0.00102
    },
    "date": "2024-10-18",
    "result": 1.02
  }
  ```
  .Caso negativo:
  ```json
  {
    "success": false,
    "error": {
      "code": 402,
      "type": "invalid_from_currency",
      "info": "You have entered an invalid \"from\" property. [Example: from=EUR]"
    }
  }
  ```
