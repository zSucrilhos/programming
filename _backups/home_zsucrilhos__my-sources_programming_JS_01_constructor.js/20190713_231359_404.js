/* A constructor is a template to create objects.
 * It starts like a function, then you can call that
 * same constructor with it's arguments' values to create
 * a new object from the template.
 * And you can also use functions as properties.
 *
 * Functions with no name are anonymous functions. Why give the
 * function a name when you already have the property name?
*/ 

function Car(numberOfWheels, numberOfDoors, name, brand, horsePower){
    this.name = name;
    this.brand = brand;
    this.horsePower = horsePower;
    this.numberOfDoors = numberOfDoors;
    this.numberOfWheels = numberOfWheels;

    this.type = function(){
        console.log("An SUV...");
    }
}
document.getElementById

var logan = new Car(4, 5, "Logan", "Renault", 160);
console.log(logan);
logan.type();
erick erick
eri

function Jar(material, size, color) {
    this.material = material;
    this.size = size;
    this.color = color;
    this.type = "This is a jar to serve juice or water";

    this.observation = function(){
        console.log("This jar is beautiful!");
    }
}

var juiceJar = new Jar("glass", "big", "transparent");
console.log(juiceJar);
juiceJar.observation();
