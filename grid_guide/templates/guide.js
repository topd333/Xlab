window.log = function(){
	log.history = log.history || [];   // store logs to an array for reference
	log.history.push(arguments);
	if(this.console) {
		console.log( Array.prototype.slice.call(arguments) );
	}
};

var selectedGuide = 'categories';
var enableRandom = false; //instead these are sorted by population/name
var dg_data = {};
var world_api = 'http://ws.world-ng.agni.lindenlab.com/v2/destinations/';
//var world_api = "http://keywordws-phx1.damballah.lindenlab.com/v2/destinations/";

function showGuide(name) {
	if(name != selectedGuide) {
		//check to see if the guide has already been added to the page
		if($('#'+name+'_guide').length == 0) {
			createGuide(name);
		} else {
			flipGuides(name);
		}
	}
}

function flipGuides(name) {	
	var displayName = $('#'+name+'_nav h2').text();
	
	$('.list').hide(); 							//hide all current guides
	$('.tooltip').css('visibility','hidden'); 	//hide all tooltips
	$('#'+name+'_guide').show(); 				//show the active guide
	$('#view_category #categoryname').text(displayName);
	
	if(name == 'categories') {
		$('#view_category').hide();
		$('#choose_category').show();
	} else {
		$('#view_category').show();
		$('#choose_category').hide();
	}
	
	selectedGuide = name;
	
	//reset the scroll position, this way they always start on the left
	$('body').scrollLeft(0); 
}

function createGuide(name) {
	var guideData = { 'name': name };
	$("#guideTemplate").tmpl(guideData).insertAfter("#rowTemplate");
	
	//subcategory_simple_name
	var category = $('#'+name+'_nav').attr('data-category');
	var sub_category = $('#'+name+'_nav').attr('data-subcategory');
	var data = dg_data[category];

	results = [];
	for(var i=0; i<data.length; i++) {
		if(sub_category && data[i].subcategory_simplename == sub_category) {
			results[results.length] = data[i];
		} else if(!sub_category) {
			results[results.length] = data[i];
		}
	}

	for(var i=0; i<results.length; i++) {
		var itm = results[i];

		var rowData = {
			'title': itm.name,
			'description': itm.description,
			'location': itm.location,
			'slug': itm.slug
		};

		//get the midsize image
		var midsize = getAsset(itm, 'midsize');

		//Check if the rows should be inserted randomly
		if(enableRandom) {
			var row = $("#rowTemplate").tmpl(rowData);

			//fix the image now
			$(row).find('img').attr('src', midsize);
			
			if(i < 2) {
				$("#"+name+"_guide").append(row);
			} else {
				//now that we have a few items, time to randomly insert them
				var location = parseInt(Math.random() * (i-1));
				var isBefore = parseInt(Math.random() * 2) < 1 ? true : false;
				
				if(isBefore) {
					$(row).insertBefore($("#"+name+"_guide .item")[location]); 
				} else {
					$(row).insertAfter($("#"+name+"_guide .item")[location]); 
				}
			}
		} else {
			$("#rowTemplate").tmpl(rowData).appendTo("#"+name+"_guide");
			$('#'+name+'_guide .item:last-child img').attr('src', midsize);
		}
	}
	
	$('#'+name+'_guide').css('width', (results.length * 157));
	
	//show the destination count
	$('#'+name+'_guide .count .num').text(results.length);
	
	//setup the tooltips for this guide
	$("#"+name+"_guide .trigger[title]").tooltip({ 
		position: "center right",
		offset: [0,10],
		delay: 0,
		predelay: 500,
		effect: 'fade'
	}).dynamic({ left: { direction: 'left' } });
	
	//add in the enter and leave events to handle the hover states
	$('#'+name+'_guide .info').each(function() {
		$(this).hover(
			function(event) {  //mouse enter
				$('.tooltip').css('visibility','hidden');
				$('.info.hover').removeClass('hover');
				$(this).addClass('hover');
			},
			
			function(event) {  //mouse leave
				$(this).removeClass('hover');
			}
		);
	});
	
	//setup the population information
	if(data && data.length > 0) {
		for(var i=0; i<data.length; i++) {
			var pop_count = data[i].population.current;
			var pop_level = data[i].population.pop_level;
			var pop_display = pop_count;
			var slug = data[i].slug;
			var itm = $('.list [data-slug="'+slug+'"] .population');

			if(itm.length > 0 && pop_count != "0") {
				$(itm).find('.num').text(pop_display);
				$(itm).show();
			}
		}
	}
	
	flipGuides(name);
}

var showLoader = true;
var loaderTimeout = 5000; //5 seconds
function showLoading(itm) {
	if(showLoader) {
		$('#loading').show();
		setTimeout('hideLoading()', loaderTimeout);
		
		//clean hover states
		$(itm).parent().removeClass('hover');
		$('.tooltip').css('visibility','hidden');
	}
}

function hideLoading() {
	$('#loading').hide();
}

function getAsset(data, size) {
	var a = '';
	
	if(data.assets.length > 0) {
		for(var i=0; i<data.assets.length; i++){
			if(data.assets[i].type == size) {
				a = data.assets[i].data;
				break;
			}
		}
	}

	return a;
}

$(function() {
	//localize before anything else happens
	locale.translate();
	
	//special check for spanish
	if(locale.lang == 'es') {
		$('#editor_nav h2').addClass('long');
	}

	//get all the category images
	var category_url = world_api + 'categories/bychan/viewer_dg?format=jsonp';
	$.ajax({
		url: category_url,
		dataType: 'jsonp',
		success: function(data) {
			for(i in data) {
				var cat = data[i];
				$('#'+data[i].simple_name+'_nav .info a img')
					.attr('src',data[i].image)
					.css('background','none');
			}
		}
	});

	var cat_count = $('#categories_guide .item').length;
	$('#categories_guide.list').css('width', (cat_count*156));

	//pre-fetch all the feeds
	$('#categories_guide .item').each(function() {
		var category = $(this).data('category');
		var sub_category = $(this).data('subcategory');
		var page_size = $(this).data('pagesize');
		var max_pop = $(this).data('maxpop');
		var page_num = $(this).data('page');
		var random_image = $(this).data('random-image');
		
		//check to see category has been loaded up
		if(!(category in dg_data) || sub_category) {
			querystring = '?format=jsonp&maturity=gma&flatten';

			if(page_size != null) 	 { querystring += '&pagesize='+page_size; }
			if(max_pop != null) 	 { querystring += '&maxpop='+max_pop; }
			if(page_num != null) 	 { querystring = '/'+page_num+querystring; }
			if(random_image != null) { random_image = true }

			url = world_api+category+querystring;

			$.ajax({
				url: url,
				dataType: 'jsonp',
				success: function(data) {
					dg_data[category] = data;
					
					if(data && data.length > 0) {
						if(sub_category) {
							var sub_count = 0;

							for(var i=0; i<data.length; i++) {
								if(data[i].subcategory_simplename == sub_category) {
									sub_count++;
								}
							}

							if(sub_count == 0) {
								$('#'+sub_category+'_nav').hide();
								$('#categories_guide').css('width', ($('#categories_guide').width() - 157));
							} else {
								$('#'+sub_category+'_nav .count .num').text(sub_count);
							}
						} else {
							if(data.length == 0) {
								$('#'+category+'_nav').hide();
								$('#categories_guide').css('width', ($('#categories_guide').width() - 157));
							} else {
								$('#'+category+'_nav .count .num').text(data.length);
							}
						}

						//set a random image from the data results for this category
						if(random_image) {
							var rand = parseInt(Math.random() * (data.length));
							$('#'+category+'_nav img').attr('src', getAsset(data[rand], 'midsize'));
						}
					} else {
						$('#'+category+'_nav').hide();
					}
				}
			});
		}
	});
	
	//add in the enter and leave events to handle the hover states
	$('.list .item .info').each(function() {
		$(this).hover(
			function(event) {  //mouse enter
				//reset all other hovered items first
				$('.list .item .info.hover').removeClass('hover');
				$(this).addClass('hover');
			},
			
			function(event) {  //mouse leave
				$(this).removeClass('hover');
			}
		);
	});
});

