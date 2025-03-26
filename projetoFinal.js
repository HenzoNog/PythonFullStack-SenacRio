//Dia 12- Ultima aula UC1
//Aula do dia 26/03/25

class Disciplina {
    constructor(nome, codigo) {
        this.nome = nome;
        this.codigo = codigo;
        this.alunosMatriculados = [];
    }

    matricularAluno(aluno) {
        this.alunosMatriculados.push(aluno);
        console.log(`${aluno.nome} foi matriculado na disciplina ${this.nome}.`);
    }

    gerarBoletim() {
        console.log(`\n📄 Boletim da Disciplina: ${this.nome} (${this.codigo})`);
        if (this.alunosMatriculados.length === 0) {
            console.log("Nenhum aluno matriculado nesta disciplina.");
            return;
        }
        this.alunosMatriculados.forEach((aluno) => {
            let media = aluno.calcularMedia();
            console.log(`Aluno: ${aluno.nome} | Matrícula: ${aluno.matricula} | Média: ${media.toFixed(2)}`);
        });
    }
}

class Aluno {
    constructor(nome, matricula) {
        this.nome = nome;
        this.matricula = matricula;
        this.notas = [];
    }

    adicionarNota(nota) {
        this.notas.push(nota);
    }

    calcularMedia() {
        if (this.notas.length === 0) return 0;
        let soma = this.notas.reduce((acc, nota) => acc + nota, 0);
        return soma / this.notas.length;
    }
}

// ---- Testando o código ----

let disciplina = new Disciplina("Matemática", "MAT101");

let aluno1 = new Aluno("João", "A001");
aluno1.adicionarNota(8);
aluno1.adicionarNota(7);
aluno1.adicionarNota(9);

let aluno2 = new Aluno("Maria", "A002");
aluno2.adicionarNota(6);
aluno2.adicionarNota(8);
aluno2.adicionarNota(7);

disciplina.matricularAluno(aluno1);
disciplina.matricularAluno(aluno2);

disciplina.gerarBoletim();
