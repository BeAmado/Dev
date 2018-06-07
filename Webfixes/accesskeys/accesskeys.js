//get all the anchors ('a' tags) in the document
var anchors = document.getElementsByTagName('a');

//object to store all of the anchors ('a' tags) that have accesskeys
//the keys will be the respective anchor's keys and the value will be a reference to the anchor element
var accessAnchors = {};
for (var i = 0; i < anchors.length; i++) {
	if (anchors[i].hasAttribute('accesskey')) {
		//if the anchor has an accesskey store it in the accessAnchors object
		accessAnchors[anchors[i].accessKey] = anchors[i]; 
	}
}

//create a DOMElement 'anchors' to store the accessAnchors as its value
var anchorsElement = document.createElement('anchors');
anchorsElement.value = accessAnchors;
anchorsElement.id = 'accessAnchors';

//append the anchor tag to the body of the html document
document.getElementsByTagName('body')[0].appendChild(anchorsElement);


//function to test if the specified modifiers were pressed
function testModifiersPressed(evt, modKeys, testType) {
	//if there is only one modifier key to test
	if (modKeys.length == 1) {
		var modifierKey = modKeys[0];
		//test if the modifier key was already pressed
		if (evt.getModifierState(modifierKey)) {
			return true;
		}
	}
	else if (modKeys.length > 1) {
		//test for multiple modifiers pressed
		var testResult = null;
		if (testType == 'everyone') {
			//test if all the modifiers were pressed
			testResult = true;
			for (var i = 0; i < modKeys.length; i++) {
				testResult = testResult && evt.getModifierState(modKeys[i]);
			}
		}
		else if (testType == 'atLeastOne') {
			//test if at least one modifier is pressed
			testResult = false;
			for (var i = 0; i < modKeys.length; i++) {
				testResult = testResult || evt.getModifierState(modKeys[i]);
			}
		}
		return testResult;
	}

	return false;
}


//function to be called everytime a key is pressed
/**
This function might be "tweaked" to achieve the desired behaviour you want for the accesskeys.
You can tweak this function through 4 anchor points numbered from 1 to 4, that might be commented out or uncommented.
The default setting is to comment out the anchor points #2 and #4  while leaving the #1 and #3 uncommented.
This default setting will activate the accesskeys whenever they are pressed whilst pressing the "Alt" key

Examples:
1) Want to activate the accesskeys when they are pressed whilst pressing both "Alt" and "Ctrl" at the same time
uncomment anchor points 1, 3 and 4.
comment out anchor point 2.

2) Want to activate the accesskeys when they are pressed while pressing either "Alt" or "Ctrl"
uncomment anchor points 2, 3 and 4.
comment out anchor point 1.
*/
function myKeydown(e) {
	
	var testType;
	var modifierKeys = [];

	// uncomment the type of test you want to execute 
	// and comment out the one you do not want
	testType = 'everyone'; // anchor point #1
	//testType = 'atLeastOne'; // anchor point #2

	// uncomment the keys you want to have as modifiers
	// and comment out the ones you do not want
	modifierKeys.push('Alt'); // anchor point #3
	//modifierKeys.push('Control'); // anchor point #4

	axsKey = e.key;
	var accessAnchors = document.getElementById('accessAnchors').value;
	if (axsKey in accessAnchors) {
		if (testModifiersPressed(e, modifierKeys, testType)) {
			accessAnchors[axsKey].click();
		}
	}
}

//bind the myKeydown function to the event onkeydown
document.onkeydown = myKeydown;
