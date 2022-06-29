# ProyectoFinal-TodosLosGrupos

A tener en cuenta:

index.csv tiene todo el código del proyecto
A tener en cuenta de que se tiene que hacer un downgrade de uno de los paquetes en el terminal de IDE. Se debe ingresar "npm install node-fetch@2.6.1"

El código tiene las siguientes funciones:

- getUFValue que devuelve un archivo "parametros.txt" el cual tiene la fecha y el valor de la UF actual. 
- getPrincipios que devuelve un array con los principios ingresados en el archivo "principios_activos"
- sinTildes que entrega una cadena de texto sin tildes 
- arraySinTildes que entrega un array sin tildes 
- getArraysofLinks que crea los links que usaremos más adelante para conseguir toda la información

- Promedio total: promedio por principio
- Promedioporfarmacia
- Menorprecio: entrega el menor precio en farmacia por principio
- info: muestra por consola la información de todas las instancias creadas

- getAhumadaInfo: en esta función aplicamos el paradigma procedural ya que hacemos webscrapping en las páginas de los links de la farmacia ahumada
- getDrsimiInfo: en esta función aplicamos el paradigma procedural ya que hacemos webscrapping en las páginas de los links de la farmacia Dr. Simi

La clase principal que ocupa el código para guardar y mostrar la información es "Medicamento". Esta clase tiene sus propiedades privadas, setters y getters para modificar y acceder a la información de cada una de las instancias creadas.
