//
let nome = "João";
let idade = 25;
console.log(nome, idade);

//

let a = 10;
let b = 5;
console.log(a, b);
console.log("Soma", a + b);
console.log("Subtração", a - b);
console.log("Multiplicação", a * b);
console.log("Divisão", a / b);

//

let PrimeiroNome = "Maria";
let Sobrenome = "Joana Peixoto";
let NomeCompleto = PrimeiroNome + "" + Sobrenome;
console.log (NomeCompleto);

//

let x = 15;
let y = 20;
console.log("x é maior que y?", x > y);
console.log("x é igual a y?", x = y);

//

let frase = "JavaScript é divertido";
console.log(frase.toUpperCase());
let novaFrase = frase.replace("divertido", "poderoso");
console.log(novaFrase);

//

let TemCarteira=true;
let idade=18;
let TemCarro=false;
let PodeDirigir =idade >= 18;
console.log("PodeDirigir");
console.log("PodeDirigir" e "TemCarro?", PodeDirigir && TemCarro);

//

let contador = 0
contador += 5; 
contador -= 2;
contador *= 3;
console.log("valor final do contador", contador);

//

let nota = 75
if (nota >= 60) {
    console.log('Aprovado');
} else if (nota >= 40); {
    console.log("Recuperação");
    else {
        console.log("Reprovado";);
 }