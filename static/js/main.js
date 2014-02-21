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
      if (this.href.indexOf("publication") !== -1 && window.location.href("publication") !== -1) {
         $(this).addClass("selectedSideBarTitles");
      }
   });

   $('.anchorsCv a').eq(0).addClass('selectedAnchors');

   $('.anchorsCv a').click( function(e) {   
      $('.anchorsCv .selectedAnchors').removeClass('selectedAnchors');
      $(this).addClass('selectedAnchors');
   });
      
   $(".anchorsExhibition a").each(function() {   
      if (window.location.href.indexOf(this.href) != -1) {
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
