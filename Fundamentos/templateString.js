const nome = 'Rebeca' // String convencional
const concatenacao = 'Olá ' + nome + '!' 
const template = `
    Olá
    ${nome}!` // TemplateString, ${valor}
console.log(concatenacao, template)

// expressões...
console.log(`1 + 1 = ${1 + 1}`)

const up = texto => texto.toUpperCase() // Funcao que formata como maiusculo
console.log(`Ei... ${up('cuidado')}!`) // Template com a funcao