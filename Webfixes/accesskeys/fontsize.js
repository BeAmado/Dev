/**
This function increases the element's font size by the specified step in percentage 
If the step is negative the font size will be decreased
*/
function increaseFontSize(element, step) {

	var fontSizePercent;
	step = parseInt(step);

	if (!sessionStorage.getItem('fontSizePercent')) {
		sessionStorage.setItem('fontStoragePercent', 100);
		fontSizePercent = 100;
	}
	else {
		fontSizePercent = parseInt(sessionStorage.getItem('fontSizePercent'));
	}

	//increase the font size in step %
	fontSizePercent += step; 
	
	//save the increased font size in the sessionStorage
	sessionStorage.setItem('fontSizePercent', fontSizePercent); 
	
	//set the element font size
	element.style.fontSize = fontSizePercent + '%';
}


//function to reset the font size to 100%
function resetFontSize(element) {
	sessionStorage.setItem('fontSizePercent', 100); 
	element.style.fontSize = '100%';
}
