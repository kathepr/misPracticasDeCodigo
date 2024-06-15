/*
Las promesas pueden suceder: 

    Ahora
    En el futuro
    Nunca 

Para crear una promesa:

Utilizamos la palabra reservada 'new' seguida de la palabra 'Promise' que es el constructor de la promesa. 

Este constructor recibe un único parámetro que es una función, la cuál a su vez, recibe otros dos parámetros: resolve y reject
*/ 

const promesa = new Promise(function(resolve, reject){
    resolve("Todo correcto")
    // reject("No funciona")
})



//EJEMPLO con promesas

const vacas = 15;
const contadorVacas = new Promise((resolve, reject) => {
    if (vacas >10){
        resolve("Si tenemos las vacas necesarias")
    }
    else{
        reject("Nos faltan vacas")
    }
})

contadorVacas.then((result) => {
    console.log(result);
}).catch((error) => {
    console.log(error);
}).finally(() => {
    console.log("Terminó la ejecución de la promesa")
})

