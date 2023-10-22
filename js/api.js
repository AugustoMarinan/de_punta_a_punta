
const ciudad = 'Esquel'; // Reemplaza con el nombre de la ciudad que te interesa


// URL de la API de OpenWeatherMap para obtener información sobre la ciudad
const apiUrl =`https://goweather.herokuapp.com/weather/${ciudad}`;

// Función para obtener datos de la ciudad
async function obtenerDatosCiudad() {
  try {
    // Realizar la petición a la API utilizando fetch
    const respuesta = await fetch(apiUrl);

    // Verificar si la petición fue exitosa (código de estado 200)
    if (!respuesta.ok) {
      throw new Error(`Error en la petición: ${respuesta.status}`);
    }

    // Convertir la respuesta a formato JSON
    const datosCiudad = await respuesta.json();

    // Extraer información sobre la ciudad (puedes ajustar esto según la estructura de datos)
    //const poblacion = datosCiudad.population;

    // Imprimir datos de la ciudad
    console.log(datosCiudad);


  } catch (error) {
    console.error('Error al obtener datos de la ciudad:', error);
  }
}

// Función para obtener fotos de la ciudad (reemplázala con la lógica adecuada)
//function obtenerFotosCiudad() {
  // Implementa aquí la lógica para obtener fotos de la ciudad
  // Puedes usar fetch nuevamente para obtener las fotos
//}

// Llamar a la función para obtener datos de la ciudad al cargar la página
obtenerDatosCiudad();