$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $(".dropdown-trigger").dropdown();
    $('.modal').modal();
    $('.tooltipped').tooltip();
    $('.carousel').carousel(
        {
            shift : 0,
            numVisible: 1
        }
    );
    setInterval(function() {
        $('.carousel').carousel('next');
    }, 15000);        
  });


