const apiKey = '6ecf068d782a9600388a3e3f815b6440';
const apiUrl = 'https://api.flickr.com/services/rest/';

async function obtenerFotos(ciudad) {
    const params = {
        method: 'flickr.photos.search',
        api_key: apiKey,
        text: ciudad,
        format: 'json',
        nojsoncallback: 1,
        per_page: 1,
    };

    try {
        const response = await fetch(`${apiUrl}?${new URLSearchParams(params)}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        if (data.photos && data.photos.photo.length > 0) {
            mostrarFotos(data.photos.photo);
        } else {
            console.log('No se encontraron fotos para la ciudad especificada.');
        }
    } catch (error) {
        console.error('Error al obtener fotos:', error);
    }
}

function mostrarFotos(photos) {
    const container = document.getElementById('fotos-container');
    container.innerHTML = '';

    photos.forEach((photo) => {
        const imgUrl = `https://farm${photo.farm}.staticflickr.com/${photo.server}/${photo.id}_${photo.secret}.jpg`;
        const imgElement = document.createElement('img');       
        imgElement.src = imgUrl;
        container.appendChild(imgElement);
    });
}



//obtenerFotos("23512grupo27esquel") 

//prueba de la llamada
var select = document.getElementById("miSelectMultiple");
 
select.addEventListener("change", function(){
  var selectedOptions = this.selectedOptions;
  console.log("Options selected: ");
  for (var i = 0; i < selectedOptions.length; i++) {
    var valor_elegido =(selectedOptions[i].value)
        console.log( valor_elegido)
        obtenerFotos(valor_elegido); 

       }
   
});
        