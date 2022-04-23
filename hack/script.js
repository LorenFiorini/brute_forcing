

function Generate() {
    var passes = 11;
	var crypto = new bCrypt();
	var salt = crypto.gensalt(passes);
	var val = document.getElementById("crypto").value;
	crypto.hashpw(val, salt, function(hash){
		document.getElementById("output").value = hash;
		document.getElementById("checkbtn").disabled = false;
		console.log(hash); 
	}, function() {
		done = false;
	});
}

function Verify() {
	var crypto = new bCrypt();
	var val = document.getElementById("crypto").value;
	var hash = document.getElementById("output").value;
        //hash = "$2a$11$OFNOTFR2fvNMgWGybJL2YuSnAU245e0X1ceO.3Ql9x4TtpsoKYIQK";
        //hash = "$2a$11$KKGSCNmcQFJFv5sSoh7JqObKUoKnSdZoJLuctYla74fIOie5cy3Zu";
        //hash = "$2a$11$HfRBwflyEQvZSvQUYp.uWO/33WeM7/4Me3y7yA58ibT1gaQYWbtge";
        //hash = "$2a$11$erx1/aHNBXch8vBCHSYUj.00mr7hnLyeKv73VjsFaPlWdz2kuQePi";
	hash = "$2a$11$PMmOUSKkkhJJHLvjO/GV7uxpdDYxHvs58jGAMrfD9hKJEkv/pIgY.";

	crypto.checkpw(
		val,
		hash,
		function(res){
			document.getElementById("result").innerHTML = (res == true)?"Valid":"Invalid";
			document.getElementById("result").style = (res == true)?"color: green;":"color: red;";
			window.dataLayer.push({event: (res == true)?'curiousu-code-valid':'curiousu-code-invalid'});
		},
		function() {
			// No-op
			done = false;
		});
	}

function CheckValue(value, hash) {
	if(checkresult != undefined)
		checkresult = undefined;

	var crypto = new bCrypt();
	crypto.checkpw(
		value,
		hash,
		function(res) {
			checkresult = res;
			console.log(checkresult?"Valid":"Invalid");
		}, function(){
			done = false;
		}
	);	
}

function GetResult() {
	return checkresult;
}

var checkresult;
var done;
window.check = CheckValue;
window.generate = Generate;







