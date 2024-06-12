// const promesaEjemplo = new Promise((resolve, reject) => {
//     //Si la operacion es exitosa, se llama resolve
//     //Si la operacion falla, reject.
//     resolve('I have succeded')
//     // reject('Salió error')
// });

// console.log("inicio de promesa")

// //PRIMERA FORMA DE ejecutar promesa:
// promesaEjemplo.then((data) => {
//     //data va a tener todos los datos y se ejecuta cuando la operacion ha sido exitosa
//     console.log("mensaje", data)
// }).catch((error)=>{
//     //Se ejecuta cuando el proceso falla
//     console.error("error", error)
// })

// console.log("fin de promesa")





// const promesaEjemplo2 = new Promise((resolve, reject) => {
//     //Si la operacion es exitosa, se llama resolve
//     //Si la operacion falla, reject.
//     resolve('I have succeded')
//     // reject('Salió error')
// });

// //SEGUNDA FORMA de ejecutar promesa
// console.log("inicio de segunda promesa")


// //Siempre que el await está dentro de una funcion, se acompaña del async
// const funcionPromesa = async() =>{
//     return await promesaEjemplo
// }

// const dato = await funcionPromesa();
// console.log(dato)
// console.log("fin de segunda promesa")





//FETCH
// const url = `https://jsonplaceholder.typicode.com/posts/`;
// const options = {
// 	method: 'GET',
// };

// const response = await fetch(url, options);
// const data = await response.json();
// console.table(response['body'])



//POST

// const url = `https://jsonplaceholder.typicode.com/posts/`;

// const datosEnviar = {
//     title: 'foo',
//     body: 'bar',
//     userId: 2024,
// }

// const options = {
// 	method: 'POST',
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify(datosEnviar)
// };


// const response = await fetch(url, options);
// const data = await response.json();
// console.table(data)





//PUT

// const url = `https://jsonplaceholder.typicode.com/posts/9`;

// const datosEnviar = {
//     title: 'Otro nombre',
//     body: 'bar',
//     userId: 2024,
// }

// const options = {
// 	method: 'PUT',
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify(datosEnviar)
// };


// const response = await fetch(url, options);
// const data = await response.json();
// console.table(data)





//DELETE

// const url = `https://jsonplaceholder.typicode.com/posts/10`;


// const options = {
// 	method: 'DELETE',
//     headers: { "Content-Type": "application/json" },
// };


// const response = await fetch(url, options);
// console.table(response)