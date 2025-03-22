// factory function é uma função que retorna um obj
// Fatcory simples
function criarPessoa() {
    return {
        nome: 'Ana',
        sobrenome: 'Silva'
    }
}

console.log(criarPessoa())

// Exercício proposto
function criarProduto(nome, preco){
    return {
        nome: nome,
        preco: preco
    }
}

console.log(criarProduto('prod1', 5.99))
console.log(criarProduto('prod2', 10.05))