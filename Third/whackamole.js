const holes = document.querySelectorAll('.hole');
const scoreBoard = document.querySelector('.score');
const moles = document.querySelectorAll('.mole');
let lastHole;
let timeUp = false;
let score = 0;

function randTime(min, max) {
    return Math.round(Math.random()*(max-min)+min)
}

function randHole(holes) {
 const randIndex = Math.floor(Math.random()*holes.length)
 const hole = holes[randIndex]
 if(hole==lastHole){
     return randHole(holes)
 }
 lastHole = hole;
 return hole;
}

function peep() {
 const time = randTime(1000,2000)  //1초와 2초 사이로 지정.
 const hole = randHole(holes)
 hole.classList.add('up') //옹라가는 효과?

 setTimeout(() => {
    hole.classList.remove('up')
    if(!timeUp){
        //만약 게임이 끝나지않았다면,
        peep()
    }
 },time) //time시간동안..설정?
}

function startGame() {
 //점수를 0으로 초기화.
 scoreBoard.textContent = 0
 score = 0
 timeUp = false
 peep()

 setTimeout(() => timeUp = true, 10000)  //두더지 게임 진행시간.
 //10000:10초 의미.
}

function bonk(e) {
    //클릭했을경우, 점수와 관련된 함수.
//클릭을 신뢰할 수 있는지 없는지에 관한 함수.
  if(!e.isTrusted) return
  this.classList.remove('up')
  score++
  scoreBoard.textContent = score
}

moles.forEach(mole => mole.addEventListener('click', bonk));