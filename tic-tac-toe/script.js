/*
* @Author: ravi
* @Date:   2021-03-08 18:44:35
* @Last Modified by:   ravi
* @Last Modified time: 2021-03-08 19:45:00
*/
// Here onwards, functions check turn of the player  
// and put accordingly value X or 0 
// flag = 1; 
// function rotate(id) { 
//     if (flag == 1) { 
//         document.getElementById(id).innerHTML = 'X'; 
//         document.getElementById(id).disabled = true; 
//         flag = 0; 
//     } 
//     else { 
//         document.getElementById(id).innerHTML = 'O'; 
//         document.getElementById(id).disabled = true; 
//         flag = 1; 
//     } 
// } 
  
// function myfunc_2(id) { 
//     if (flag == 1) { 
//         document.getElementById("1").innerHTML = "X"; 
//         document.getElementById("1").disabled = true; 
//         flag = 0; 
//     } 
//     else { 
//         document.getElementById("1").innerHTML = "0"; 
//         document.getElementById("1").disabled = true; 
//         flag = 1; 
//     } 
// } 
  
// function myfunc_3(id) { 
//     if (flag == 1) { 
//         document.getElementById("2").innerHTML = "X"; 
//         document.getElementById("2").disabled = true; 
//         flag = 0; 
//     } 
//     else { 
//         document.getElementById("2").innerHTML = "0"; 
//         document.getElementById("2").disabled = true; 
//         flag = 1; 
//     } 
// } 
  
// function myfunc_4() { 
//     if (flag == 1) { 
//         document.getElementById("3").innerHTML = "X"; 
//         document.getElementById("3").disabled = true; 
//         flag = 0; 
//     } 
//     else { 
//         document.getElementById("3").innerHTML = "0"; 
//         document.getElementById("3").disabled = true; 
//         flag = 1; 
//     } 
// } 
  
// function myfunc_5() { 
//     if (flag == 1) { 
//         document.getElementById("4").innerHTML = "X"; 
//         document.getElementById("4").disabled = true; 
//         flag = 0; 
//     } 
//     else { 
//         document.getElementById("4").innerHTML = "0"; 
//         document.getElementById("4").disabled = true; 
//         flag = 1; 
//     } 
// } 
  
// function myfunc_6() { 
//     if (flag == 1) { 
//         document.getElementById("5").innerHTML = "X"; 
//         document.getElementById("5").disabled = true; 
//         flag = 0; 
//     } 
//     else { 
//         document.getElementById("5").innerHTML = "0"; 
//         document.getElementById("5").disabled = true; 
//         flag = 1; 
//     } 
// } 
  
// function myfunc_7() { 
//     if (flag == 1) { 
//         document.getElementById("6").innerHTML = "X"; 
//         document.getElementById("6").disabled = true; 
//         flag = 0; 
//     } 
//     else { 
//         document.getElementById("6").innerHTML = "0"; 
//         document.getElementById("6").disabled = true; 
//         flag = 1; 
//     } 
// } 
  
// function myfunc_8() { 
//     if (flag == 1) { 
//         document.getElementById("7").innerHTML = "X"; 
//         document.getElementById("7").disabled = true; 
//         flag = 0; 
//     } 
//     else { 
//         document.getElementById("7").innerHTML = "0"; 
//         document.getElementById("7").disabled = true; 
//         flag = 1; 
//     } 
// } 
  
// function myfunc_9() { 
//     if (flag == 1) { 
//         document.getElementById("8").innerHTML = "X"; 
//         document.getElementById("8").disabled = true; 
//         flag = 0; 
//     } 
//     else { 
//         document.getElementById("8").innerHTML = "0"; 
//         document.getElementById("8").disabled = true; 
//         flag = 1; 
//     } 
// } 


flag = 1;

function changeSign(id) {
	// document.getElementById(id).innerHTML = 'X'

	
	if (flag == 1) { 
        document.getElementById(id).innerHTML = "X"; 
        document.getElementById(id).disabled = true; 
        flag = 0; 
    } 
    else { 
        document.getElementById(id).innerHTML = "O"; 
        document.getElementById(id).disabled = true; 
        flag = 1; 
    } 

	// Rows win check
	if (document.getElementById('0').innerHTML == "X" 
		&& document.getElementById('1').innerHTML == "X"
		&& document.getElementById('2').innerHTML == "X") {
		alert("Win 🏆")
	}

	if (document.getElementById('3').innerHTML == "X" 
		&& document.getElementById('4').innerHTML == "X"
		&& document.getElementById('5').innerHTML == "X") {
		alert("Win 🏆")
	}

	if (document.getElementById('6').innerHTML == "X" 
		&& document.getElementById('7').innerHTML == "X"
		&& document.getElementById('8').innerHTML == "X") {
		alert("Win 🏆")
	}

	// Columns Win check
	if (document.getElementById('0').innerHTML == "X" 
		&& document.getElementById('3').innerHTML == "X"
		&& document.getElementById('6').innerHTML == "X") {
		alert("Win 🏆")
	}
	
	if (document.getElementById('1').innerHTML == "X" 
		&& document.getElementById('4').innerHTML == "X"
		&& document.getElementById('7').innerHTML == "X") {
		alert("Win 🏆")
	}

	if (document.getElementById('2').innerHTML == "X" 
		&& document.getElementById('5').innerHTML == "X"
		&& document.getElementById('8').innerHTML == "X") {
		alert("Win 🏆")
	}

	// Diagonal Win check
	if (document.getElementById('0').innerHTML == "X" 
		&& document.getElementById('4').innerHTML == "X"
		&& document.getElementById('8').innerHTML == "X") {
		alert("Win 🏆")
	}
	
	if (document.getElementById('2').innerHTML == "X" 
		&& document.getElementById('4').innerHTML == "X"
		&& document.getElementById('6').innerHTML == "X") {
		alert("Win 🏆")
	}

	// Rows win check
	if (document.getElementById('0').innerHTML == "O" 
		&& document.getElementById('1').innerHTML == "O"
		&& document.getElementById('2').innerHTML == "O") {
		alert("Win 🏆")
	}

	if (document.getElementById('3').innerHTML == "O" 
		&& document.getElementById('4').innerHTML == "O"
		&& document.getElementById('5').innerHTML == "O") {
		alert("Win 🏆")
	}

	if (document.getElementById('6').innerHTML == "O" 
		&& document.getElementById('7').innerHTML == "O"
		&& document.getElementById('8').innerHTML == "O") {
		alert("Win 🏆")
	}

	// Columns Win check
	if (document.getElementById('0').innerHTML == "O" 
		&& document.getElementById('3').innerHTML == "O"
		&& document.getElementById('6').innerHTML == "O") {
		alert("Win 🏆")
	}
	
	if (document.getElementById('1').innerHTML == "O" 
		&& document.getElementById('4').innerHTML == "O"
		&& document.getElementById('7').innerHTML == "O") {
		alert("Win 🏆")
	}

	if (document.getElementById('2').innerHTML == "O" 
		&& document.getElementById('5').innerHTML == "O"
		&& document.getElementById('8').innerHTML == "O") {
		alert("Win 🏆")
	}

	// Diagonal Win check
	if (document.getElementById('0').innerHTML == "O" 
		&& document.getElementById('4').innerHTML == "O"
		&& document.getElementById('8').innerHTML == "O") {
		alert("Win 🏆")
	}
	
	if (document.getElementById('2').innerHTML == "O" 
		&& document.getElementById('4').innerHTML == "O"
		&& document.getElementById('6').innerHTML == "O") {
		alert("Win 🏆")
	}


}