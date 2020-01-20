

function GuardarPor(){

	alert("s1");
/*
	var p_tit = document.getElementById('p_tit').value;	
	var p_titu = document.getElementById('p_titu').value;	
	var p_desc = document.getElementById('p_desc').value;	
	var p_cal = document.getElementById('p_cal').value;	
	var p_cat = document.getElementById('p_cat').value;	
	var p_fec = document.getElementById('p_fec').value;	
	var p_fot = document.getElementById('id_foto').value;	
	var p_lug = document.getElementById('p_lug').value;
	
	alert("s");

	var xhr = new XMLHttpRequest();
	var cad = "/por_reg/?p_tit="+p_tit+"&&p_titu="+p_titu+"&&p_lug="+p_lug+"&&p_desc="+p_desc+"&&p_cal="+p_cal+"&&p_cat="+p_cat
				+"&&p_fec="+p_fec+"&&p_fot="+p_fot;

	//alert("  >>  "+cad);

	xhr.open('GET',cad,true); // sincrono o asincrono
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4 && xhr.status == 200){
			console.log("return successfull");
		}
		else{
			console.log("fail");
		}
	}
	xhr.send();
	*/
}


function Comentar(){

	var nam = document.getElementById('name');
	var email = document.getElementById('email');
	var phone = document.getElementById('phone');
	var mes = document.getElementById('message');
	var act = true
	var msj_val = "Por favor estos datos son inportantes para ponernos en contacto con usted: ";
	if(nam.value ==""){
		msj_val += " nombre,";
		act = false;
	}
	if (/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i.test(email.value)){
	   console.log("La dirección de email " + email.value + " es correcta!.");
	} else {
		msj_val += " un correo válido,";
		act = false;
	}
	if(phone.value ==""){
		msj_val += " su celular,";
		act = false;
	}
	if(mes.value ==""){
		msj_val += " su consulta,";
		act = false;
	}
	if(act == true){
		GuardarComentario(nam.value,email.value,phone.value,mes.value);
		nam.value ="";
		email.value = "";
		phone.value = "";
		mes.value = "";
	}else{
		alert(msj_val+" gracias!");
	}	
}
 

function GuardarComentario(nam,email,phone,message){

	var xhr = new XMLHttpRequest();
	var cad = "/guar_comn/?nam="+nam+"&&email="+email+"&&phone="+phone+"&&message="+message;

	xhr.open('GET',cad,true); // sincrono o asincrono
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4 && xhr.status == 200){
			console.log("retornó successfull");

			var rpta ='"<div class="alert alert-success alert-dismissible fade show" role="alert">'+
              '<strong>Gracias!!</strong> Nosotros nos pondremos en contacto con usted en la brevedad posible.'+
              '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'+
                '<span aria-hidden="true">&times;</span>'+
              '</button>'+
            '</div>';

			document.getElementById('rpta_msj').innerHTML=rpta;
		}
		else{
			var rpta ='"<div class="alert alert-danger alert-dismissible fade show" role="alert">'+
              '<strong>Algo salió mal!!</strong> Nuestra área de tecnología lo resolverá cuanto antes,'+
              ' por favor comuniquese con nosotros por cualquier otro de nuestros medios disponibles.'+
              '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'+
                '<span aria-hidden="true">&times;</span>'+
              '</button>'+
            '</div>';

			document.getElementById('rpta_msj').innerHTML=rpta;
		}
	}
	xhr.send();

 }

function SeePassword(){
	var eye = document.getElementById("eye-password");
	var passw = document.getElementById("password");

	var classEye = eye.className.split(" ");
	if(classEye[1] == "fa-eye"){
		eye.classList.remove("fa-eye");
		eye.classList.add("fa-eye-slash");
		passw.type = "text";
	}else{
		eye.classList.remove("fa-eye-slash");
		eye.classList.add("fa-eye");
		passw.type = "password";
	}
}



function Loginn(){
	var us = document.getElementById("user");
	var ps = document.getElementById("password");

	var cad = "/logon/?ps="+ps.value+"&&us="+us.value;

	var xhr = new XMLHttpRequest();
	xhr.open('GET',cad,true); // sincrono o asincrono
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4 && xhr.status == 200){
			console.log("retornó successfull");
			window.location="/cuerpo/";
		}
		else{
			console.log("err");
		}
	}
	xhr.send();
 }
