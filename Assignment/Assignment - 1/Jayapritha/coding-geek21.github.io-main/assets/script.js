function openNav() {
  document.getElementById("myNav").style.width = "100%";
}

function closeNav() {
  document.getElementById("myNav").style.width = "0%";
}

function clickMenu(){
  document.getElementById("myNav").style.width="0%";
}

$(document).ready(function () {
  $("ul.sidebar-navigation > li > a").click(
    function (e) {
      $("ul.sidebar-navigation > li").removeClass(
        "active");
      $("ul.sidebar-navigation > li > a").css(
        "color", "");

      $(this).addClass("active");
      $(this).css("color", "#ff0173");
  });
});

