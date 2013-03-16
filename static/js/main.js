$(document).ready(function(){
   $("#menu a").each(function() {   
      if (this.href == window.location.href) {
      $(this).addClass("selectedMenu");
   }
   });

   $(".sideBarTitles a").each(function() {   
      if (this.href == window.location.href) {
      $(this).addClass("selectedSideBarTitles");
   }
   });

   $('.anchorsCv a').click( function(e) {   
      $('.anchorsCv .selectedAnchors').removeClass('selectedAnchors');
      $(this).addClass('selectedAnchors');
   });


});
