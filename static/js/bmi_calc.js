
function bmi() {
	var weight = document.getElementById("weight").value;
	var height = document.getElementById("height").value;
	var height_metr = height / 100;
	var bmi_result = parseInt(weight) / Math.pow(height_metr,2);

	//window.alert(sum);
	document.getElementById("bmi_result").innerHTML = Math.round(bmi_result * 100 ) / 100;
	
	if (bmi_result < 16){
		document.getElementById("comment").innerHTML = "wygłodzenie";
		document.getElementById("bmi_result").style.backgroundColor = "red";
	} else if (bmi_result >= 16 && bmi_result < 17){
		document.getElementById("comment").innerHTML = "wychudzenie";
		document.getElementById("bmi_result").style.backgroundColor = "red";
	} else if (bmi_result >= 17 && bmi_result < 18.5){
		document.getElementById("comment").innerHTML = "niedowaga";
		document.getElementById("bmi_result").style.backgroundColor = "orange";
	} else if (bmi_result >= 18.5 && bmi_result < 25){
		document.getElementById("comment").innerHTML = "wartość prawidłowa";
		document.getElementById("bmi_result").style.backgroundColor = "green";
	} else if (bmi_result >= 25 && bmi_result < 30){
		document.getElementById("comment").innerHTML = "nadwaga";
		document.getElementById("bmi_result").style.backgroundColor = "orange";
	} else if (bmi_result >= 30 && bmi_result < 35){
		document.getElementById("comment").innerHTML = "I stopień otyłości";
		document.getElementById("bmi_result").style.backgroundColor = "red";
	} else if (bmi_result >= 35 && bmi_result < 40){
		document.getElementById("comment").innerHTML = "II stopień otyłości (otyłość kliniczna)";
		document.getElementById("bmi_result").style.backgroundColor = "red";
	} else {
		document.getElementById("comment").innerHTML = "III stopień otyłości (otyłość skrajna)";
		document.getElementById("bmi_result").style.backgroundColor = "red";
	}
/*
poniżej 16,0 – wygłodzenie
16,0–16,99 – wychudzenie
17,0–18,49 – niedowaga
18,5–24,99 – wartość prawidłowa
25,0–29,99 – nadwaga
30,0–34,99 – I stopień otyłości
35,0–39,99 – II stopień otyłości (otyłość kliniczna)
powyżej 40,0 – III stopień otyłości (otyłość skrajna)
*/
	
}

