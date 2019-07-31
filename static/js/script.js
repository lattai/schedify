console.log("clicked!")

const compareClass = document.querySelector('.compare');//compare div



const fullSched = document.querySelector("#your-month")
const yourWeek = document.querySelector("#your-week")
const theirWeek = document.querySelector("#their-week")


const compare1 = document.querySelector("#compare1")
const compare2 = document.querySelector("#compare2")
const compare3 = document.querySelector("#compare3")
const resetview = document.querySelector("#resetScheduleView")

yourWeek.style.height = "0px"
theirWeek.style.height = "0px"

compare1.addEventListener("click",e =>{
  console.log("clicked!")
  fullSched.style.height = "0px"
  fullSched.style.width = "0px"
  yourWeek.style.height = "300px"
  theirWeek.style.height = "300px"
  console.log("week height: "+ yourWeek.style.height)
})
compare2.addEventListener("click",e =>{
  console.log("clicked!")
  fullSched.style.height = "0px"
  fullSched.style.width = "0px"
  yourWeek.style.height = "300px"
  theirWeek.style.height = "300px"

})
compare3.addEventListener("click",e =>{
  console.log("clicked!")
  fullSched.style.height = "0px"
  fullSched.style.width = "0px"
  yourWeek.style.height = "300px"
  theirWeek.style.height = "300px"
})
resetview.addEventListener("click",e =>{
  console.log("clicked!")
  fullSched.style.height = "600px"
  fullSched.style.width = "1014px"
  yourWeek.style.height = "0px"
  theirWeek.style.height = "0px"
})
