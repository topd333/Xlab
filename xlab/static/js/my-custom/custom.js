// JavaScript Document


$(document).ready(function() {
	$(".topnav").accordion({
		accordion:false,
		speed: 500,
		closedSign: '<i class="fa fa-fw"> &#xf078; </i>',
		openedSign: '<i class="fa fa-fw"> &#xf077; </i>'
	});
});


$(function(){
				$("#shopping_list li").quickpaginate({ perpage: 9, pager : $("#shopping_list_counter") });
});

$(function(){
				$(".shopping_list li").quickpaginate({ perpage: 5, pager : $(".shopping_list_counter") });
});

$(function(){
				$(".shopping_list1 li").quickpaginate({ perpage: 5, pager : $(".shopping_list_counter1") });
});

$(function(){
				$(".shopping_list2 li").quickpaginate({ perpage: 5, pager : $(".shopping_list_counter2") });
});

$(function(){
				$(".shopping_list3 li").quickpaginate({ perpage: 4, pager : $(".shopping_list_counter3") });
});



$(function () {
			$(".gen").selectbox();
});

