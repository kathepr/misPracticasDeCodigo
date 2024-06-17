// Lista de APIS: https://github.com/public-apis/public-apis


/*

*********************************
    SECCION DE URL'S: 
*********************************
*/

const API_URL_RANDOM= "https://api.thecatapi.com/v1/images/search?limit=2"

const API_URL_FAVOURITE= "https://api.thecatapi.com/v1/favourites"

const API_URL_DELETE = (id) => `https://api.thecatapi.com/v1/favourites/${id}`

const API_URL_UPLOAD = "https://api.thecatapi.com/v1/images/upload"





const spanError = document.getElementById("error")




/*

*********************************
    SECCION DE BUSQUEDA RANDOM: 
*********************************
*/
async function loadRandomCats(){
    const res = await fetch(API_URL_RANDOM);
    const data = await res.json();


    const botonFavourite1 = document.getElementById("botonFavourite1")
    const botonFavourite2 = document.getElementById("botonFavourite2")

    botonFavourite1.onclick = () => saveFavouriteCats(data[0].id)
    botonFavourite2.onclick = () => saveFavouriteCats(data[1].id)





    const img = document.querySelectorAll("img");

    if (res.status !== 200){
        spanError.innerHTML = "Se ha presentado un ERROR" + res.status

    }else{

    //Añadir el src de las imagenes
    img.forEach((img, index) => {
        if (data[index]) {
            img.src = data[index].url;
        }
    });
    }
}

window.onload = loadRandomCats()




/*

*****************************
SECCIÓN SUBIR FOTO DE GATITO
*****************************

*/

async function uploadMichiPhoto() {
    const form = document.getElementById("uploadingForm");
    const formData = new FormData(form);
    const file = formData.get("file"); // Obtener el archivo del form data

    console.log(file); // Debug: Aqui puedo revisar si el archivo está siendo recibido correctamente

    if (!file) {
        console.error('El archivo no ha sido seleccionado');
    }

    try {
        const res = await fetch(API_URL_UPLOAD, {
            method: "POST",
            headers: {
                'x-api-key': 'live_8YKVJsVer7wdPfMfgk8nUX9MAn3KDydecePacVT6QJTXe1P10AkXbiddPqf9qbsN'
            },
            body: formData,
        });

        const data = await res.json(); //Se convierte la data a JSON

        if (res.status != 201) {
            spanError.innerHTML = "Hubo un error: " + res.status;
     
        } else {
            console.log("Foto del gatito subida satisfactoriamente");
            console.log({ data });
            console.log(data.url);
            saveFavouriteCats(data.id); //La guardo en mis favoritos
            loadFavouriteCats();
        }
    } catch (error) {
        console.error('Error:', error);
    }
}



/*

*********************************
    SECCION DE GATOS FAVORITOS: 
*********************************
*/


//Get datos de gatos favoritos
async function loadFavouriteCats(){
    const res = await fetch(API_URL_FAVOURITE, {
        method: "GET",
        headers:{

            "Content-Type": "application/json", 

            'x-api-key': 'live_8YKVJsVer7wdPfMfgk8nUX9MAn3KDydecePacVT6QJTXe1P10AkXbiddPqf9qbsN' 
        }
    });
    const data = await res.json();

    if (res.status !== 200){
        spanError.innerHTML = "Se ha presentado un ERROR" + res.status

    }else{
        //Limpiar sección y volver a crear documentos
        const section = document.getElementById("favouriteMichis")
        section.innerHTML = "";
        const h2 = document.createElement('h2')
        const h2Text = document.createTextNode("Gatitos Favoritos")
        
        section.appendChild(h2)
        h2.appendChild(h2Text)

        //recorremos el array para mostrarlo
        data.forEach(gato => {
            const article = document.createElement("article");
            const img = document.createElement("img");
            const button = document.createElement("button");
            const buttonText = document.createTextNode("Sacar al michi de favoritos")


            img.src = gato.image.url
            article.appendChild(img)
            article.appendChild(button)
            button.onclick = () => {deleteFavouriteCats(gato.id)}
            button.appendChild(buttonText)
            section.appendChild(article)


        })
    }

}

loadFavouriteCats()


//Post datos de gato en favoritos
async function saveFavouriteCats(id){
    const res = await fetch(API_URL_FAVOURITE, {
        method: "POST",
        headers:{
            "Content-Type": "application/json", 

            'x-api-key': 'live_8YKVJsVer7wdPfMfgk8nUX9MAn3KDydecePacVT6QJTXe1P10AkXbiddPqf9qbsN' 
        },
        body: JSON.stringify(
            {
                image_id:id
            })
    })

    const data = await res.json();

    if (res.status !== 200){
        spanError.innerHTML = "Se ha presentado un ERROR" + res.status
    }else{
        console.log("Gatito guardado en Favoritos")
        loadFavouriteCats();
    }

}


//Eliminar datos de gatos favoritos
async function deleteFavouriteCats(id){
    const res = await fetch(API_URL_DELETE(id), {
        method: "DELETE",
        headers:{
            "Content-Type": "application/json", 
            'x-api-key': 'live_8YKVJsVer7wdPfMfgk8nUX9MAn3KDydecePacVT6QJTXe1P10AkXbiddPqf9qbsN' 
        }
    })

    const data = await res.json();

    if (res.status !== 200){
        spanError.innerHTML = "Se ha presentado un ERROR" + res.status
    } else{
        console.log("Gatito eliminado de Favoritos")
        loadFavouriteCats()
    }
}