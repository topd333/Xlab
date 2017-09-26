// JavaScript Document

 $(function (){
                    $("#wizard").steps({
                        headerTag: "h2",
                        bodyTag: "section",
                        transitionEffect: "slideLeft",
                        onStepChanged: function(event, currentIndex, priorIndex){
                          resizeJquerySteps(currentIndex);
                        
                        },
                        onStepChanging: function(event, currentIndex, newIndex){
                          
                          if(currentIndex==3 || currentIndex==4){
                            if(currentIndex < newIndex){
                              return true;
                            }
                            return false;
                          }
                          return true;
                        }
                    });
                    resizeJquerySteps();
                    function resizeJquerySteps(currentIndex) {
                        var hg = $('.body.current').outerHeight();
                        if(currentIndex==1 || currentIndex==2 || currentIndex==3 || currentIndex==4){                            
                            hg = hg + 30;
                        }
                        if(currentIndex==undefined){
                          hg = hg - 69;
                        }
                        $('.wizard .content').animate({ height: hg }, "slow");
                        }

});




function carousel(){

var showcase = $("#showcase"), title = $('#item-title'), index = $('#item-index')

     showcase.Cloud9Carousel( {
        yOrigin: 42,
        yRadius: 48,
        mirror: {
          gap: 12,
          height: 0.2
        },
        buttonLeft: $("#nav > .left"),
        buttonRight: $("#nav > .right"),
        autoPlay: 1,
        bringToFront: true,
        onRendered: rendered,
        onLoaded: function() {
          showcase.css( 'visibility', 'visible' )
          showcase.css( 'display', 'none' )
          showcase.fadeIn( 1500 )
        }
      } )

      function rendered( carousel ) {
        title.val( carousel.nearestItem().element.alt )
        index.val(carousel.nearestIndex())
        // Fade in based on proximity of the item
        var c = Math.cos((carousel.floatIndex() % 1) * 2 * Math.PI)
        title.css('opacity', 0.5 + (0.5 * c))
      }

      //
      // Simulate physical button click effect
      //
      $('#nav > button').click( function( e ) {
        var b = $(e.target).addClass( 'down' )
        setTimeout( function() { b.removeClass( 'down' ) }, 80 )
      } )

      $(document).keydown( function( e ) {
        //
        // More codes: http://www.javascripter.net/faq/keycodes.htm
        //
        switch( e.keyCode ) {
          /* left arrow */
          case 37:
            $('#nav > .left').click()
            break

          /* right arrow */
          case 39:
            $('#nav > .right').click()
        }
      } )

}

$(function() {
      carousel();
    })

