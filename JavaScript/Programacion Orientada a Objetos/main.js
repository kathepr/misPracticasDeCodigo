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






