const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

//

class personagem {
    constructor(vida, tipo, atk, def, nome, mana, skills) {
        this.nome = nome;
        this.atipo = tipo;
        this.vida = vida;
        this.atk = atk;
        this.def = def;
        this.mana = mana;
        this.skills = skills;
    }
    atk(alvo) {
        let dano= this.atk - alvo.def;
        if (dano>0) alvo.vida -=dano;
        console.log('${this.nome} atacou${alvo.nome} causando ${dano} de dano.');
    }
}
class Mago extends personagem {
    constructor(nome,) {
        super(nome, "Mago", );
    }
}
class Viking extends personagem {
    constructor(nome){
        super(nome, "Viking", );
    }
}
class Druida extends personagem{
    constructor (nome) {
        super(nome, "Druída", );
    }
}
class Bardo extends personagem{
    constructor (nome){
        super(nome, "Bardo", );
    }
}
class Paladin extends personagem{
    constructor (nome){
        super(nome, "Paladin", );
    }
}
class Draconian extends personagem{
    constructor(nome){
        super(nome, "Draconian", );
    }
}

