//1
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,  
    output:process.stdout
});

function calcularMedia (){
    rl.question("Digite a primeira nota (de 0 a 10:", (nota1) => {
        rl.question("Digite a segunda nota (de 0 a 10):", (nota2) => {
            rl.question("Digite a terceira nota (de 0 a 10):", (nota3) => {
                rl.question("Digite a quarta nota (de 0 a 10):", (nota4) => {
                    nota1 = parseFloat(nota1);
                    nota2 = parseFloat(nota2);
                    nota3 = paseFloat(nota3);
                    nota4 = parseFloat(nota4);
                    //
                    let media = (nota1 + nota2+ nota3+ nota4)/4;
                    console.log ('Sua media é: ${media.toFixed(2)}');
                    if (media >= 7) {
                        console.log('Aprovado');
                    }else{
                        console.log('Reprovado');
                    }
                    rl.close;
                });
            });
        });
    });
}
calcularMedia ();

//2

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function somarPares() {
    rl.question("Digite um numero para o inicio do intervalo:", (inicio) =>{
        rl.question("Digite um numero final para o intervalo:", (final) =>{
            inicio = parseInt(inicio);
            final = parseInt(final);
            let soma = 0;
            let i = inicio;
            
            while (i <= fim) {
                if (i %2 === 0){
                    soma +=1;
                }
                i++;
            }
            console.log ('A soma dos numeros pares no intervalo de ${inicio} a ${fim} é: ${soma}');
            rl.close();
        });
    });
});
somarParesWhile();

//3

function verificarPalindromo() {
    const readline = require("readline");

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });



    rl.question("Digite uma palavra ou frase: ", (entrada) => {
        let texto = entrada.toLowerCase().replace(/[\s]/g, "");
        let tamanho = texto.length;
        let ehPalindromo = true;

        for (let i = 0; i < Math.floor(tamanho / 2); i++) {
            if (texto[i] !== texto[tamanho - 1 - i]) {
                ehPalindromo = false;
                break; 
            }
        }

        if (ehPalindromo) {
            console.log(" É palíndromo!");
        } else {
            console.log("Não é palíndromo.");
        }

        rl.close();
    });
}

verificarPalindromo();

//4

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function calcularJurosSimples() {
    rl.question("Digite o valor principal (P): ", function (p) {
        rl.question("Digite a taxa de juros anual (r) em decimal (ex: 0.05 para 5%): ", function (r) {
            rl.question("Digite o tempo em anos (t): ", function (t) {
                let principal = parseFloat(p);
                let taxaJuros = parseFloat(r);
                let tempo = parseFloat(t);

                if (isNaN(principal) || isNaN(taxaJuros) || isNaN(tempo) || principal < 0 || taxaJuros < 0 || tempo < 0) {
                    console.log("Entrada inválida. Insira valores numéricos positivos.");
                } else {
                    let montante = principal * (1 + taxaJuros * tempo);
                    console.log(`O montante final após ${tempo} anos será: ${montante.toFixed(2)}`);
                }

                rl.close();
            });
        });
    });
}

calcularJurosSimples();

//5

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function contarDigitos() {
    rl.question("Digite um número inteiro positivo: ", function (numero) {
        let num = parseInt(numero);
        
        if (isNaN(num) || num <= 0) {
            console.log("Entrada inválida. Insira um número inteiro positivo.");
            rl.close();
            return;
        }

        let count = 0;
        do {
            count++;
            num = Math.floor(num / 10); // Remove o último dígito
        } while (num > 0);

        console.log(`O número possui ${count} dígitos.`);
        rl.close();
    });
}

contarDigitos();

