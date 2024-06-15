//setTimeout recibe una funcion y un tiempo

console.log("Inicio")
let temporizador = setTimeout (() => {
    console.log("Ejecutando un setTimeout. Este se ejecuta una sola vez")
}, 3000)

setInterval (() => {
    console.log("Ejecutando un setTimeout. Este se ejecuta indefinidamente cada cierto intervalo de tiempo")
}, 3000)


setInterval (() => {
    console.log(new Date().toLocaleTimeString());
}, 3000) //Cada 3 segundos me va a dar la hora