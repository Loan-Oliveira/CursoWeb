function criarProduto(nome, preco){
    return {
        nome, //nao e obrigado a passar o valor, pois o mesmo nome e o parametro
        preco,
        desconto: 0.1
    }
}

console.log(criarProduto('Notebook', 21199.49))
console.log(criarProduto('iPad', 1199.49))