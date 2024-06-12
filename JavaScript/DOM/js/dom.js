console.log("**********Elementos del documento**********");
/*Gracias a la anotación del punto o ciertas propiedades, podemos acceder a los elementos*/

console.log(document.head);
console.log(document.body)
console.log(document.documentElement) // Obtener el HTML
console.log(document.doctype)


//Nodos, elementos y selectores

//Nodo: Un nodo es cualquier objeto en la estructura jerárquica del documento HTML

//Elementos: Representan las etiquetas HTML.

//Selectores: Los selectores son cadenas que utilizas para seleccionar uno o más elementos del DOM.

console.log(document.getElementsByTagName("li"));
console.log(document.getElementsByClassName("card"));
console.log(document.getElementsByName("nombre"));
console.log(document.getElementById("menu"));
console.log(document.querySelector("#menu")); //Recibe como parametro un ID, una clase, una etiqueta, cualquier tipo de elemento

//Se usa más estos que los anteriores
console.log(document.querySelector("a")); //Para conocer el primer enlace que tiene la pagina
console.log(document.querySelectorAll("a")); //Para conocer TODOS los enlaces que tiene la pagina
document.querySelectorAll("a").forEach((element) => console.log(element));//Para que muestre todos los elementos

console.log(document.querySelectorAll(".card")); //Para conocer TODAS las cartas que tiene la pagina
console.log(document.querySelectorAll(".card")[2]); //Para acceder a la tercer tarjeta. 





//INTERACTUAR CON ATRIBUTOS DE HTML

console.log("**********INTERACTUAR CON ATRIBUTOS************")

console.log(document.documentElement.lang)
console.log(document.querySelector(".link-dom").href) //Trae URL de la pagina

//Para cambiar atributo desde javascript
document.documentElement.lang = "es";
console.log(document.documentElement.lang)
document.documentElement.setAttribute("lang","es-MX")
console.log(document.documentElement.lang)


//guardar en variables

const linkDOM = document.querySelector(".link-dom");