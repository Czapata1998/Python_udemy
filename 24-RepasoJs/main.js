var nombre = "Cristhian Zapata";
var altura = 189;

/* var concatenacion = nombre + " " + altura;


 document.write(concatenacion); 

var datos = document.getElementById("datos");

datos.innerHTML = `
 <h1>Soy la caja de datos</h1>
 <h2>Mi nombre es ${nombre}</h2>
 <h3>Mido: ${altura}</h3>


`;

if (altura >= 190){
    datos.innerHTML += '<h1>Eres una persona alta</h1>';
}else{
    datos.innerHTML += '<h1>Eres una persona baja</h1>';
}

for(var i = 1998; i <= 2020; i++){
    datos.innerHTML += "<h2> Estamos en el year: "+i;

}
 */
function Muestraminombre(nombre, altura){
    
    var  misDatos = `
     <h1>Soy la caja de datos</h1>
     <h2>Mi nombre es ${nombre}</h2>
     <h3>Mido: ${altura}</h3>
     `;

     return misDatos;
}

function imprimir(){
    var datos = document.getElementById("datos");
    datos.innerHTML = Muestraminombre();
}

Muestraminombre("Victor Robles WEB 111", 190)

imprimir();

var nombres = [ 'Cristhian' , 'Daniel' , 'Anuel' , 'Bad bunny'];

document.write('<h1>Listado de nombres </h1>');
/* for(i = 0; i < nombres.length; i++){
    document.write(nombres[i] + '<br>');
} */

nombres.forEach((nombre) => {
    document.write(nombre + '<br/>');

});