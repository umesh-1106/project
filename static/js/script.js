// Wrong Parking Detection System

console.log("Wrong Parking Detection System Started");

// Show Current Time

function updateTime(){

let now=new Date();

let time=now.toLocaleString();

let element=document.getElementById("currentTime");

if(element){

element.innerHTML=time;

}

}

setInterval(updateTime,1000);

// Search Vehicle

function searchTable(){

let input=document.getElementById("searchInput");

if(!input) return;

let filter=input.value.toUpperCase();

let table=document.getElementById("historyTable");

let tr=table.getElementsByTagName("tr");

for(let i=1;i<tr.length;i++){

let td=tr[i].getElementsByTagName("td")[1];

if(td){

let txt=td.textContent||td.innerText;

tr[i].style.display=txt.toUpperCase().indexOf(filter)>-1?"":"none";

}

}

}

// Confirm Vehicle Registration

function registerSuccess(){

alert("Vehicle Registered Successfully");

}

// Camera Buttons

function startCamera(){

alert("Camera Started");

}

function stopCamera(){

alert("Camera Stopped");

}

// Detection Status

function detection(status){

let element=document.getElementById("status");

if(element){

element.innerHTML=status;

}

}
