
function services(){
	document.getElementById("services").style = "box-shadow:3px 3px black; transform: translateY(-15px) translateX(-5px); transition: .3s ease-out";
	
}

function servicesOut(){
	document.getElementById('services').style = "box-shadow: none; transtion-delay:2s; transtion: 2s ease-out; "
}


function onClickMenu(){
	document.getElementById('nav').classList.toggle('change');
	document.getElementById('nav-links').classList.toggle('nav-change');


}




var burger = document.getElementById('burger')

