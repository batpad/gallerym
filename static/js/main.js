$(document).ready(function(){
   $("#menu a").each(function() {   
      if (this.href == window.location.href) {
      $(this).parents("li").children('a').addClass("selectedMenu");
   }
   });
});