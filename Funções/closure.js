// Closure é o escopo criado quando uma função é declarada
// Este escopo permite a funcao acessar e manipular variaveis externas a funcao

// Contexto léxico em ação!

const x = 'Global'

function fora() {
    const x = 'Local'
    function dentro() {
        return x
    }

    return dentro
}

const minhaFuncao = fora()
console.log(minhaFuncao())