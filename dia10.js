//////////////////////////////////////////////
//////////// MATRIZES - Dia 10///////////////
////////////////////////////////////////////

let matriz1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
];

//acessar elemento da matriz

let matriz2 = [
    [1,2,3],
    [3,6,9],
    [10,15,20]
];
console.log(matriz2[1][2]);

//percorrendo a matriz e exibindo todos os elementos
for (let i=0; i < matriz2.length; i++) {
    for(let j=0; i < matriz2[i].length; j++) {
        console.log('Elemento na linha ${i}, coluna ${j}: ${matriz2[i][j]}');
    }
}

//função para verificar se uma matriz é um quadrado mágico