// Função que recebe um objeto e desestrutura para obter os atributos
function rand({ min = 0, max = 1000}) {
    const valor = Math.random() * (max - min) + min
    return Math.floor(valor)
}

const obj = {max: 50, min: 40} // Cria o objeto
console.log(rand(obj)) // retorna o valor
console.log(rand({min: 955})) // posso já passar somente o atrb
console.log(rand({})) // ou nao passar, pois tem o valor padrao na function
// console.log(rand())