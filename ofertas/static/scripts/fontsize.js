var $z = jQuery.noConflict();
$z(document).ready(function(){
	$z("#aumentar-fonte").click(function () {
		var size = $z("#content").css('font-size');
		size = size.replace('px', '');
		size = parseInt(size) + 2;
		$z("#content").animate({'font-size' : size + 'px'});
		var sizeh1 = $z("#content h1").css('font-size');
		sizeh1 = sizeh1.replace('px', '');
		sizeh1 = parseInt(sizeh1) + 4;
		$z("#content h1").animate({'font-size' : sizeh1 + 'px'});
		return false;				
		
	});

	$z("#diminuir-fonte").click(function () {
		var size = $z("#content").css('font-size');
		size = size.replace('px', '');
		size = parseInt(size) - 2;
		$z("#content").animate({'font-size' : size + 'px'});
		var sizeh1 = $z("#content h1").css('font-size');
		sizeh1 = sizeh1.replace('px', '');
		sizeh1 = parseInt(sizeh1) - 4;
		$z("#content h1").animate({'font-size' : sizeh1 + 'px'});
			
		return false;
	});
});