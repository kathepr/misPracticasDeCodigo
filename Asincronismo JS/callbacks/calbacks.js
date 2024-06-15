
//Funcion que se encarga de sumar valores
function sum(num1, num2){
    return num1 + num2
}

function calc(num1, num2, callback){
    return callback(num1, num2);
}

//Los callbacks permiten que una función ejecute otra función una vez que ha completado su tarea

let result = calc(5, 10, sum);
console.log(result);


//Set Time Out es otro tipo de callback

setTimeout(() => {
    console.log("Hola JavaScript")
}, 2000) //2 segundos


function saludo(nombre) {
    console.log(`Hola ${nombre}`)
}

//Aqui setTimeout funciona como un callback
setTimeout(saludo, 2000, "Kathe")