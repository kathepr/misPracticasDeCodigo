// https://rapidapi.com/

const API = 'https://imdb-top-100-movies.p.rapidapi.com/top1';

const options = {
  method: 'GET',
  headers: {
    'x-rapidapi-key': '47dd54ca27mshcc4f5a7b3f8e65bp13a9e9jsn9c7ad419d058',
	'x-rapidapi-host': 'imdb-top-100-movies.p.rapidapi.com'
  }
};

async function fetchData(urlAPI) {
  const response = await fetch(urlAPI, options);
  const data = await response.json();
  return data;
}

(async () => {
  try {
    const movie = await fetchData(API);
    console.log(movie); // Añade esta línea para imprimir la respuesta y verificar la estructura

    let view = `
      <div class="group relative p-4 border rounded-md bg-gray-100">
        <img src="${movie.big_image}" alt="${movie.title}">
        <h3 class="text-lg font-bold text-gray-800">${movie.title}</h3>
        <p class="text-sm text-gray-600"><strong>Rating:</strong> ${movie.rating}</p>
        <p class="text-sm text-gray-600"><strong>Year:</strong> ${movie.year}</p>
        <p class="text-sm text-gray-600"><strong>Description:</strong> ${movie.description}</p>
        <p class="text-sm text-gray-600"><strong>Genre:</strong> ${movie.genre.join(', ')}</p>
        <p class="text-sm text-gray-600"><strong>Director:</strong> ${movie.director.join(', ')}</p>
      </div>
    `;
    document.getElementById('content').innerHTML = view; // Se selecciona un elemento en el DOM con el ID content y se inserta el contenido de la variable view dentro de este elemento. Esto actualiza el contenido del elemento en la página web con el nuevo HTML generado.

  } catch (error) {
    console.error('Error fetching data:', error);
  }
})();