"use strict";
function _(){
	var a = Array.apply(null, arguments);
	var img = a.map(function(x, i){
		var img = new Image();
		img.src = i+".png";
		return img;
	});
	var x = a.map(function(){return 0;});
	var c = document.getElementById("can").getContext("2d");
	(function z(){
		for(var i=0;i<a.length;i++){
			x[i]=(x[i]+a[i])%(img[i].width+a[i]);
			c.drawImage(img[i],x[i],0)
			c.drawImage(img[i],x[i]-img[i].width*(a[i]>0?1:-1),0)
		}
		setTimeout(z,25);
	})()
}