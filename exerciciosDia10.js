//1 Soma de Matrizes: Crie duas matrizes 3x3 e escreva uma função para somá-las. A função deve retornar uma nova matriz com o resultado.

function somaMatrizes (){
    let resultado
    for(let i=0; i<3; i++) {
        for(let j[i]=0; j<3; j++);{
            resultado[i][j]= MatrizA[i][j] + MatrizB[i][j];
        }
    }
    return resultado;
}

let matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

let matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
];

// Somando as matrizes
let matrizSoma = somarMatrizes(matriz1, matriz2);

// Exibindo os resultados
console.log("Matriz 1:");
console.table(matriz1);

console.log("Matriz 2:");
console.table(matriz2);

console.log("Matriz Soma:");
console.table(matrizSoma);

//2 Transposição de Matriz: Escreva uma função que receba uma matriz 3x3 e retorne sua transposta (troque linhas por colunas).

function transporMatriz(matriz) {
    let transposta = [];

    for (let i = 0; i < 3; i++) {
        transposta[i] = [];
        for (let j = 0; j < 3; j++) {
            transposta[i][j] = matriz[j][i]; // Troca linhas por colunas
        }
    }

    return transposta;
}

let matrizOriginal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

let matrizTransposta = transporMatriz(matrizOriginal);

console.log("Matriz Original:");
console.table(matrizOriginal);

console.log("Matriz Transposta:");
console.table(matrizTransposta);


