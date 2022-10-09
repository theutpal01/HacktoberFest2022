//this little rock papers scissors it's on spanish!
//developed by Codebreaker - https://www.github.com/CodeBreaker518
let player
let cpu

const game = function (player, cpu) {
  if (player === cpu) {
    console.log('Empate!')
  } else if ((player === 'piedra' && cpu === 'tijeras') || (player === 'papel' && cpu === 'piedra') || (player === 'tijeras' && cpu === 'papel')) {
    console.log('Ganaste!')
  } else if ((player === 'piedra' && cpu === 'papel') || (player === 'papel' && cpu === 'tijeras') || (player === 'tijeras' && cpu === 'piedra')) {
    console.log('Perdiste!')
  } else {
    console.log('Ingresa un valor valido')
  }
}

game('piedra', 'piedra')