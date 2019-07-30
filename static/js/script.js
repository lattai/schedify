console.log("clicked!")

const compareClass = document.querySelector('.compare');//compare div
compareClass.style.visibility  = "hidden" //"visable"


const fullSched = document.querySelector("#your-month")

const compare1 = document.querySelector("#compare1")
const compare2 = document.querySelector("#compare1")
const compare3 = document.querySelector("#compare1")
const resetview = document.querySelector("#resetScheduleView")

compare1.addEventListener("click",e =>{
  console.log("clicked!")
  fullSched.style.height = 0
  fullSched.style.width = 0
  compareClass.style.visibility = "visible"
})
compare2.addEventListener("click",e =>{
  console.log("clicked!")
  fullSched.style.height = 0
  fullSched.style.width = 0
  compareClass.style.visibility = "visible"
})
compare3.addEventListener("click",e =>{
  console.log("clicked!")
  fullSched.style.height = 0
  fullSched.style.width = 0
  compareClass.style.visibility = "visible"
})
resetview.addEventListener("click",e =>{
  console.log("clicked!")
  fullSched.style.height = 600
  fullSched.style.width = 1014
  fullSched.style.visibility = "visible"
  compareClass.style.visibility = "hidden"
})
