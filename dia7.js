
//1

let numero1 = parseInt(prompt("Digite um numero para a contagem REGRESSIVA"));
for (let i=numero1; 1 >=0; i--) {
    console.log(i);
}
//2

let numero2 = parseInt(Prompt("Digite um numero"));
let soma = 0;
let ind = 1;
while (ind <= numero2) {
    soma += ind;
    ind++;
}
console.log("Soma", soma);

//3


let numero3 = parseInt(prompt("Digite um numero para ser multiplicado de 1 a 10"));
for (let i=1; i <=10; i++ ) {
    let resultado = numero *i
    console.log('${numero3} *${i} = ${resultado}')
}

//4

let numero4 = parseInt(prompt("Digite um número para ver os pares até ele:"));
for (let i = 2; i <= numero4; i += 2) {
    console.log(i);
}

//5

let numero5 = parseInt(prompt("Digite um número para calcular o fatorial:"));
let fatorial = 1;
let i = 1;
while (i <= numero5) {
    fatorial *= i;
    i++;
}
console.log(`Fatorial de ${numero}: ${fatorial}`);

//6

let numero6;
do {
    numero6 = parseInt(prompt("Digite um número maior que 10:"));
} while (numero6 <= 10);
console.log("Número válido:", numero6);

//7

let tamanho = parseInt(prompt("Digite o tamanho do quadrado:"));
for (let i = 0; i < tamanho; i++) {
    let linha = "";
    for (let j = 0; j < tamanho; j++) {
        linha += "* ";
    }
    console.log(linha);
}
