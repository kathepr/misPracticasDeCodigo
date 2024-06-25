//Paso por valor:

let a = 10;

function cambiarValor(valor) {
  valor = 20;
  console.log("Dentro de la función: " + valor); // 20
}

cambiarValor(a);
console.log("Fuera de la función: " + a); // 10




//Paso por referencia
let obj = { propiedad: 10 };

function cambiarPropiedad(o) {
  o.propiedad = 20;
  console.log("Dentro de la función: " + o.propiedad); // 20
}

cambiarPropiedad(obj);
console.log("Fuera de la función: " + obj.propiedad); // 20