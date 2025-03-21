// Função em JS é First-Class Object (Citizens)
// Higher-order function

// Cria de forma literal
function fun1(){ }

// Armazena em uma variavel
const fun2 = function(){ }

// Armazena em um array
const array = [function(a, b){return a + b}, fun1, fun2]

console.log(array[0](2,3))

// Armazena em um atributo de objeto
const obj = {}
obj.falar = function () {return 'Opa'}
console.log(obj.falar())

// Passa função como parametro
function run(fun){
    fun()
}
run(function(){console.log('Executando...')})

// uma função pode retornar/conter uma função
function soma(a, b){
    return function(c){
        console.log(a+b+c)
    }
}
soma(2,3)(4)
const cincoMais = soma(2,3)
cincoMais(4)