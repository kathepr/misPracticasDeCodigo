/*
La palabra async antes de la función, hace que la función devuelva una promesa.

La palabra await se utiliza dentro de las funciones async, lo que hace que el programa espere hasta que la variable(promesa) se resuelva para continuar. 

*/

const funcionAsync = () => {
    return new Promise((resolve, reject) => {
        (true)
        ? setTimeout (() => resolve('Async'), 2000)
        : reject(new Error('Error'));
    });
}

const otraFuncion = async () => {
    console.log('Ya la llamamos, ahora llamaremos funcionAsync y esperaremos a que se resuelva')
    const algo = await funcionAsync();
    console.log(algo);
    console.log('Listo, ya se resolvió el proceso asincrono');
    
}

console.log("Antes de llamar otraFuncion")
otraFuncion();
console.log("Holaaa, me llamaron y no tengo que esperar a que termine el proceso asincrono")