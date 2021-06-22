const toggleMenu = document.querySelector(".inner-nav");
const menu = document.querySelector(".inner-nav-btn");

const clickMenu = () => {
  menu.classList.toggle("active");
};

toggleMenu.addEventListener("click", clickMenu);

$("a.popper").hover(
  function (e) {
    var target = "#" + $(this).attr("data-popbox");
    $(target).show();
    moveLeft = $(this).outerWidth();
    moveDown = $(target).outerHeight() / 2;
  },
  function () {
    var target = "#" + $(this).attr("data-popbox");
    if (!$("a.popper").hasClass("show")) {
      $(target).hide();
    }
  }
);
$("a.popper").click(function (e) {
  var target = "#" + $(this).attr("data-popbox");
  if (!$(this).hasClass("show")) {
    $(target).show();
  }
  $(this).toggleClass("show");
});
