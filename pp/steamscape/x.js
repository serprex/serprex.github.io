"use strict";
function _(){
	var rain=[]
	var ragi=[]
	for(var i=0;i<200;i++){
		rain.push(32768*Math.random());
		ragi.push(130+3*Math.random());
	}
	var a = [];
	for (var i=0; i<arguments.length; i++) a.push(arguments[i]);
	var img = a.map(function(x, i){
		var img = new Image();
		img.src = i+".png";
		return img;
	});
	var x = a.map(function(){return 0;});
	var c=document.getElementById("can").getContext("2d");
	(function z(){
		var t = new Date();
		for(var i=0; i<a.length; i++){
			x[i]=(x[i]+a[i])%(543+a[i]);
			c.drawImage(img[i],x[i],0);
			c.drawImage(img[i],x[i]-543*(a[i]>0?1:-1),0);
		}
		var s=t.getSeconds()*Math.PI/30, m=t.getMinutes()*Math.PI/30, h=t.getHours()*Math.PI/12;
		var xx=(x[0]+291)%543;
		c.beginPath();
		c.moveTo(xx,26);c.lineTo(xx+Math.sin(s)*6,26-Math.cos(s)*6);
		c.moveTo(xx,26);c.lineTo(xx+Math.sin(m)*5,26-Math.cos(m)*5);
		c.moveTo(xx,26);c.lineTo(xx+Math.sin(h)*4,26-Math.cos(h)*4);
		c.closePath();c.stroke();
		c.beginPath();
		for(var i=0;i<200;i++){
			xx=rain[i];
			rain[i]+=ragi[i]
			if((rain[i]>>6&511)>(xx>>6&511)&&(rain[i]&63)>(xx&63)){
				c.moveTo(xx>>6&511,xx&63);c.lineTo(rain[i]>>6&511,rain[i]&63);
			}
		}
		c.closePath();c.stroke();
		setTimeout(z,25);
	})();
}
