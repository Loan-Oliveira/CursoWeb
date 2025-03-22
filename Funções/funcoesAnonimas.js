const soma = function (x, y) {
    return x + y
}// funcao anonima em uma constante que soma 2 parametros

const imprimirResultado = function (a, b, operacao = soma) {
    console.log(operacao(a, b))
}// funcao anonima em uma const que calcula 2 param com base no param operacao
// se nao informado a operacao, usa a primeira funcao do exemplo
// pode se informar uma outra funcao como parametro

imprimirResultado(3, 4) // sem operacao, funcao soma
imprimirResultado(3, 4, soma) // implicitamente, usa a funcao soma
imprimirResultado(3, 4, function(x, y){
    return x - y
})// passa outra funcao no lugar da soma, neste caso uma funcao anonima
imprimirResultado(3, 4, (x, y) => x * y)// passa arrow f. no lugar da soma

const pessoa = {
    falar: function () {
        console.log('Opa')
    }
}// funcao anonima como atributo de um obj

pessoa.falar()