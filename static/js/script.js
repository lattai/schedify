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

const compareThings = document.querySelectorAll(".compareAnchor")
compareThings.forEach(function(anchor){
  anchor.addEventListener("click",e =>{
    console.log("clicked!")
    fullSched.style.height = "0px"
    fullSched.style.width = "0px"
    yourWeek.style.height = "300px"
    theirWeek.style.height = "300px"
    let email = anchor.id
    theirWeek.src="https://calendar.google.com/calendar/embed?src="+email+"&ctz=America%2FNew_York &amp;mode=WEEK&amp;bgcolor=%23e0ffe0"
    theirWeek.style.bgcolor= "#e0ffe0"
    theirWeek.mode = "Week"



  });
});
resetview.addEventListener("click",e =>{
  console.log("clicked!")
  fullSched.style.height = "600px"
  fullSched.style.width = "1014px"
  yourWeek.style.height = "0px"
  theirWeek.style.height = "0px"
})
