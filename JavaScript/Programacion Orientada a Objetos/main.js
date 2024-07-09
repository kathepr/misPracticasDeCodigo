// Objetos en Javascript: Casi todo en JavaScript es un Objeto.

//Se crean objetos usando llaves {}
console.log({})


function showFullName(){
    return "Mi nombre es Kathe PR"
}

//Object Properties
const user = {
    name: "Cata",
    lastname: "PR",
    age: "22", 
    showFullName: showFullName, //Methods: Son funciones,  describe lo que hace el objeto. O hacemos que ese objeto haga algo.
    nombreCompleto: function(){
        return this.name + " " + this.lastname;
    } // Methonds, también podemos poner la funcion adentro del objeto.
}

console.log(user.showFullName()); // Llamo al método showFullName del objeto user
console.log(user.nombreCompleto()); // Llama al método nombreCompleto del objeto user



//Object Properties
const account = {
    number: "1236547896541230",
    amount: 100,
    deposit(quantity){
        return this.amount = this.amount + quantity
        
    }, //Method
    withdraw(){
        return this.amount = this.amount - 100
        
    } 
}

console.log(account.deposit(300))
console.log(account.withdraw())


//Object Properties
const car = {
    model: "Shellby Cobra",
    color: "blue",
    creationYear: 1953,
    speed: 160,
    price: 1500000,
}





// *******************************************************



//Constructor: Es como un generador de objetos, nos evita estar repitiendo miles de datos (no tenemos que crear objetos literales) y lo que hace es crear un tipo de "plantilla". Son funciones.


const usuario1 = {
    name: "Katheryn",
    lastname: "PR",
    age: "30", 
    fullName(){
        return `${this.name} ${this.lastname}`;
    } // Methonds, también podemos poner la funcion adentro del objeto.
}


//Este es el CONSTRUCTOR de objetos
function Persona(){
    //Se coloco P mayuscula, para hacer referencia a un constructor
    this.name = "",
    this.lastname = "",
    this.age = 0
    this.fullName = function(){
        return `${this.name} ${this.lastname}`;
    }
} 

//palabra clave para constructures: new
const usuario2 = new Persona()
usuario2.name = "Matilda"
usuario2.lastname = "Wormwood"
usuario2.age = 6
console.log(usuario2.fullName())


//palabra clave para constructures: new
const usuario3 = new Persona()
usuario3.name = "Hermione"
usuario3.lastname = "Granger"
usuario3.age = 44
console.log(usuario3.fullName())



// *******************************************************

function Person(){
    this.name = "",
    this.lastname = ""
}

//Es muy importante colocar new, para que JavaScript entienda que hablamos de OBJETOS.

const person = new Person()
console.log(person)



// *******************************************************


//Constructores de JAVASCRIPT

const number = new Object(6)
console.log(number)







// *******************************************************


//Prototipos

function Pet(name, age){
    this.name = name,
    this.age = age,
    this. displayInfo = function(){
        return `${this.name} ${this.age}` 
    }
}

const tabby = new Pet("Tabby", 7)
tabby.name = "Gatalina" //También es posible cambiar la propiedad
const tommy = new Pet("Tommy", 5)


//PROTOTIPO
Pet.prototype.greet = function(){
    return `Hello I am ${this.name}`
} //Le añadí un nuevo metodo al constructor Pet


//Ahora todos tienen el saludo greet
console.log(tommy.greet())
console.log(tabby.greet())




//ejemplo 2 prototipo
const s = new String("hello people")

String.prototype.concaTest = function() {
    return this + "test"
}
console.log(s.concaTest())










// *******************************************************


//Class: Las clases son una plantilla que define un tipo de objeto. Puede contener metodos (funciones) y propiedades (valores)

//Esto es lo mismo, son dos formas distintas de escribirlo.

function Pasatiempo(){
    this.name = ""
    this.years = 0
}



class Hobbie {
    constructor(name, years){
        this.name = name,
        this.years = years
    } 
    greet(){
        return `He practicado ${this.name} por ${this.years} años`
    }
}
//El constructor devuelve un objeto nuevo y tiene las mismas propiedades del constructor que ya habiamos visto, es solo que este se escribe de forma distinta. 

const acuarela = new Hobbie("acuarela", 2 )
const crochet = new Hobbie("crochet", 3 )

console.log(acuarela)
console.log(acuarela.greet())
console.log(crochet)
console.log(crochet.greet())