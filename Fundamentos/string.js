const escola = "Cod3r"

console.log(escola.charAt(4)) // Retorna o caractere index 4
console.log(escola.charAt(5)) // Nao retorna erro ao nao encontrar o index
console.log(escola.charCodeAt(3)) // Retorna o codigo ASC do index
console.log(escola.indexOf('3')) // Retorna o index do caractare 3

console.log(escola.substring(1)) // Retorna a substring do index 1 em diante
console.log(escola.substring(0, 3)) // Retorna a substring do index 1 a 3

console.log('Escola '.concat(escola).concat("!")) // Exemplo de concatenação
console.log(escola.replace(3, "e")) // substitui o 3 por e

console.log('Ana,Maria,Pedro'.split(',')) // Parte a string em array sepadando pela ,