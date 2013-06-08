$(document).ready(function(){
   $(".menu li a").each(function() {   
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
   
   $(".anchorsExhibition a").each(function() {   
      if (this.href == window.location.href) {
      $(this).addClass("selectedAnchors");
   }
   });
   
   
/*   $('.anchorsExhibition a').click( function(e) {   
      $('.anchorsExhibition .selectedAnchors').removeClass('selectedAnchors');
      $(this).addClass('selectedAnchors');
   });   
*/

/*delete comments later*/
});
