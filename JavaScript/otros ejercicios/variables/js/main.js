// En JavaScript, puedes declarar una variable utilizando let y luego cambiar su valor tantas veces como quieras. Sin embargo, solo puedes declararla una vez dentro del mismo ámbito

let message;

message = 'Hola!';

message = 'Mundo!'; // valor alterado

alert(message);


// También podemos declarar dos variables y copiar datos de una a la otra.

let hello = "Hola Mundo";
let message2;

message2 = hello;
// Ahora, ambas variables contienen los mismos datos
alert(hello)// Hola mundo!
alert(message2)// Hola mundo!


//OJO: SIN EMBARGO: Utilizar diferentes variables para distintos valores incluso puede ayudar a optimizar su código







//Nombrar variables:

// let 1a;  no puede iniciar con un dígito

// let my-name; los guiones '-' no son permitidos en nombres



//Variables constantes (nunca cambian)


const myBirthday = "18.04.1990"
//Estas variable NO permiten cambios en su valor, a diferencia de let. 


//También se usa mucho las letras mayusculas, pero solo para valores que ya son conocidos por todos y ya están pre-definidos por defecto, como "pi", colores hexadecimales. 
const COLOR_RED = "#F00";
const COLOR_GREEN = "#0F0";
const COLOR_BLUE = "#00F";
const COLOR_ORANGE = "#FF7F00";

// COLOR_ORANGE es mucho más fácil de recordar y escribir que "#FF7F00".
let color = COLOR_ORANGE;
alert(color); // #FF7F00