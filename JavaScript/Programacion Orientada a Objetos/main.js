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








//**************************************************
// POO: Busca crear código modular y reutilizable. A¿Utiliza la abstracción.

//PRINCIPIOS: 

//ASOCIACIÓN: Capacidad de los objetos de referir a otros objetos.
class Person2 {
    constructor(name, lastname){
        this.name = name,
        this.lastname = lastname
    } 
}

//La asociación sugiere que estos dos objetos pueden relacionarse. Sin embargo, si no hay asociación, pueden seguir funcionando de manera independiente
const john = new Person2("John", "Ray")
const maria = new Person2("Maria", "Perez")

maria.parent = john; //Aqui le añado una relación a través de una propiedad.
console.log(maria)
console.log(john)






//AGREGACIÓN: Capacidad de referir uno o más objetos independientes. Algunos objetos pueden tener un rol "mayor" que otros, a este se le llama "Aggregate" (es el objeto que puede contener a otros) y los objetos que estan dentro se conocen como "Componentes"

const company = {
    name: "Kath Tech",
    employees: []
}

const sara = new Person2("Sara", "Ray")
const luisa = new Person2("Luisa", "Perez")

company.employees.push(sara) // Se usa PUSH para añadir
company.employees.push(luisa)

console.log(company)












//COMPOSICIÓN: Capacidad de referir uno o más objetos dependientes.
const user2 = {
    name: "Ryan",
    lastname: "Ray",
    address: {
        street: "dreamer street",
        city: "Quebec",
        country: "Canada"
    }
}

//Address, no es un objeto independiente. Si yo lo sacara de user2, no tendría sentido ya que está fuertemente relacionado con el objeto que lo contiene. 







//ENCAPSULACIÓN: Capacidad de concentrar datos en una sola entidad ocultando detalles internos. Simplifica el uso del objeto.


//Creación de constructor
function Company(name){
    let employees = [] //esto es una variable dentro del objeto, que se asocia, gracias a los metodos que se muestran a continuación.
    this.name = name

    this.getEmployees = function(){
        return employees
    }//esto es un metodo

    this.addEmployee = function(employee){
        employees.push(employee)
    }//esto es un metodo
}
company2.addEmployee({name: "Pepa"})
const company2 = new Company("Kathe's Tech")
console.log(company2)
console.log(company2.getEmployees())

//Gracias  a esto he podido acceder a un objeto que está dentro del constructor y alterarlo.











//HERENCIA: Mecanismo en el que un objeto puede adquirir las caracteristicas de uno o mas objetos.
function Person3(){
    this.name = "",
    this.lastname = ""
}

function Programmer(){
    // this.name = "",
    // this.lastname = "",    parano repetir TODAS las propiedades, podemos hacer que las HEREDE.
    this.language = ""
}

//PARA HACER UNA HERENCIA se usa prototype.
Programmer.prototype = new Person3() //programmer, hereda propiedades de Person2


// Ahora se puede crear instancias de Programmer que heredan las propiedades de Person3.
let programmer = new Programmer();
programmer.name = "John";
programmer.lastname = "Doe";
programmer.language = "JavaScript";

console.log(programmer.name);      // John
console.log(programmer.lastname);  // Doe
console.log(programmer.language);  // JavaScript




//--------------------EJEMPLO 2---------------------------
// Definición de la clase Person5
class Person5 {
    constructor(name, lastname) {
        this.name = name;
        this.lastname = lastname;
    }
}

// Definición de la clase Programmer1 que hereda de Person5
class Programmer1 extends Person5 {
    constructor(name, lastname, language) {
        super(name, lastname); // Llama al constructor de Person5
        this.language = language; // Define la propiedad específica de Programmer1
    }
}

// Creación de una instancia de Person5
const personita = new Person5("Sofia", "Rivera");
console.log(personita); // Output: Person5 { name: 'Sofia', lastname: 'Rivera' }

// Creación de una instancia de Programmer1
const programmer1 = new Programmer1("Katheryn", "Pimentel", "Python");
console.log(programmer1); // Output: Programmer1 { name: 'Katheryn', lastname: 'Pimentel', language: 'Python' }

















//POLIMORFISMO: Capacidad de procesar objetos con distintos tipos de datos y estructuras. Capacidad de las funciones para manejar diferentes tipos de datos sin necesidad de modificar su definición.

function countItems (x){
    return x.toString().length //Gracias a la conversión a cadena con toString(), la función puede procesar tanto cadenas de texto como números. Esto demuestra polimorfismo porque la misma función puede manejar y procesar diferentes tipos de datos (cadenas y números) de manera adecuada.
}

console.log(countItems("Hola"))
console.log(countItems(500))


function suma(x=0, y=0, z=0){
    return x+y+z
}
//Cualquier argumento no proporcionado se establece por defecto a 0 gracias a los valores predeterminados. Esto permite que la función sea flexible y pueda manejar diferentes cantidades de argumentos sin problemas:
console.log(suma(10,20))






//POLIMORFISMO PARAMETRICO: permite que las funciones o los datos sean genéricos, es decir, pueden operar con cualquier tipo de dato sin depender de un tipo específico

// Función genérica que simplemente retorna el valor que se le pasa
function identity(value) {
    return value;
}

console.log(identity(42)); // Salida: 42
console.log(identity("Hola")); // Salida: Hola
console.log(identity([1, 2, 3])); // Salida: [1, 2, 3]
console.log(identity({ a: 1, b: 2 })); // Salida: { a: 1, b: 2 }

//En este ejemplo, la función identity toma un argumento value de cualquier tipo y lo retorna sin modificarlo. Esta función es "paramétricamente polimórfica" porque puede aceptar cualquier tipo de dato sin estar atada a un tipo específico.



//-----------------EJEMPLO 2------------------

function Stack(){
    this.items = []
    this.push = function(item){
        this.items.push(item)
    }
}

const stack = new Stack()
stack.push("lalala")
const stack2 = new Stack()
stack2.push(1000)

console.log(stack)
console.log(stack2)





//POLIMORFISMO POR SUBTIPO: permite que una función o un método opere sobre objetos de diferentes tipos, siempre que estos tipos deriven de un tipo base común



// Clase base
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name} hace un sonido.`);
    }
}

// Clase derivada
class Dog extends Animal {
    speak() {
        console.log(`${this.name} ladra.`);
    }
}

// Otra clase derivada
class Cat extends Animal {
    speak() {
        console.log(`${this.name} maúlla.`);
    }
}

// Función que demuestra el polimorfismo por subtipo
function makeAnimalSpeak(animal) {
    animal.speak();
}

// Crear instancias de las clases derivadas
const dog = new Dog('Rex');
const cat = new Cat('Whiskers');

// Llamar a la función con diferentes subtipos
makeAnimalSpeak(dog); // Salida: Rex ladra.
makeAnimalSpeak(cat); // Salida: Whiskers maúlla.
