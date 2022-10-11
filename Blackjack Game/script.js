

//Creating array for storing multiple cards
let cardNew = []
let sumber = 0
 let hasBlackjack = false
 let isAlive = false
 let message = ""
 let  p1El = document.getElementById("p1_el")
 let  p3El = document.getElementById("p3_el")
 let  renderEl = document.getElementById("render")
 let p2El = document.getElementById("p2_el")
 


 playerEl.textContent = playerDetails.name + playerDetails.chips

 console.log(cardNew)

 function startGame() {

    isAlive = true
    let max = randomCard()
    let min = randomCard()  
    cardNew = [max, min]
 
    sumber = max + min  


renderGame()

}


function renderGame () {

   p2El.textContent = "Cards : "

 for(let i = 0; i< cardNew.length; i++){

    p2El.textContent += cardNew[i] + " "


}
    p3El.textContent = "Sum : "  + sumber  

    if(sumber <= 20 ){
        message = "Do you want to draw a new card?"
    }

    else if (sumber === 21){

        message = "Wohoo! You've got Blackjack!"
        hasBlackjack = true
    }

    else{

        message = "You are out of game"
        isAlive = false
    }

    p1El.textContent = message
    
     
}

function newCard() {

    alert("Drawing a new card from the deck")

  if(isAlive === true && hasBlackjack === false){

  let cardVar = randomCard()

  sumber += cardVar
    // pushing the new card into the cards to display new cards
  cardNew.push(cardVar)

  renderGame()
  }

}





function randomCard() {

let randomCard = Math.floor(Math.random() * 13) + 1

if(randomCard > 10){
    return 10
} else if (randomCard === 1){
    return 11

} else {
        return randomCard
}


}
