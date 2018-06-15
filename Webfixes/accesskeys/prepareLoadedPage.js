window.onload = function() {

	/////// code from the script accesskeys.js ////////////
	createAccessAnchors();

	//bind the myKeydown function to the event onkeydown
	document.onkeydown = myKeydown;
	///////////////////////////////////////////////////////



	/////// code from the script fontsize.js //////////////
	//update the font size through page changes
	if (sessionStorage.getItem('fontSizePercent')) {
		document.getElementsByTagName("html")[0].style.fontSize = sessionStorage.getItem('fontSizePercent') + '%';
	}

	document.getElementById('increase').onclick = function () {
		//increase the font size of the whole page in 20%
		increaseFontSize(document.getElementsByTagName("html")[0], 20);
	}
	
	document.getElementById('decrease').onclick = function () {
		//decrease the font size of the whole page in 20%
		increaseFontSize(document.getElementsByTagName("html")[0], -20);
	}
	
	document.getElementById('reset').onclick = function () {
		//reset the font size of the page to 100%
		resetFontSize(document.getElementsByTagName("html")[0]);
	}
	///////////////////////////////////////////////////////
}
