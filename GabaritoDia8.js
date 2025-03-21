//1

function calcularMedia () {
    let soma = 0
    for (let i = 0; i < 4; i++) {
        let nota = parseFloat(prompt('Digite a ${i + 1}ª nota:'));
        soma += nota;
    }
    let media = soma/4;
    console.log("Média:", media);
    if (media >= 7) {
        console.log("Aprovado");
    } else {
        console.log("Reprovado");
    }
}
calcularMedia ();

//2

function somaParesNoIntervalo () {
    let inicio = parseFloat(prompt("Digite o inicio do intervalo:"));
    let fim = parseFloat(prompt("Digite o fim do intervalo:"));
    let soma = 0;
    for (let i = inicio; i <= fim; i++) {
        if (i % 2 === 0) {
            soma += i;
        }
    }
    console.log("Soma dos números pares:", soma);
}
somaParesNoIntervalo ();

//3

function verificarPalindromo (){
    let texto = parseFloat(prompt("Digite uma palavra ou frases:").toLowerCase().replace(/ /g, "");
    let textoInvertido = texto.split("").reverse().join("");
    if (texto === textoInvertido) {
        console.log("É Palíndromo");
    } else{
        console.log("Não é Palíndromo");
    }
}
verificarPalindromo ();

//4

function calcularJurosSimples() {
    let P = parseFloat(prompt("DIgite o valor de (P):"));
    let r = parseFloat(prompt("Digite o valor de (r):")); /100;
    let t = parseFloat(prompt("Digite o valor de (t):"))
    let M=P*(1+r*t);
    console.log("Montante final é R$ ${M.toFixed(2)}");
}
calcularJurosSimples();

//5

function contarDigitos () {
    let numero = prompt("Digite um número inteiro positivo:");
    if (/^\d+$/.test(numero)) {
        console.log("Número de dígitos:", numero.length);
    } else{
        console.log("Insira um número inteiro positivo válido.");
    }
}
contarDigitos();