$num = $('.ui-card').length;
$even = $num / 2;
$odd = ($num + 1) / 2;
 
if ($num % 2 == 0) {
  $('.ui-card:nth-child(' + $even + ')').addClass('active');
  $('.ui-card:nth-child(' + $even + ')').prev().addClass('prev');
  $('.ui-card:nth-child(' + $even + ')').next().addClass('next');
} else {
  $('.ui-card:nth-child(' + $odd + ')').addClass('active');
  $('.ui-card:nth-child(' + $odd + ')').prev().addClass('prev');
  $('.ui-card:nth-child(' + $odd + ')').next().addClass('next');
}
 
$('.ui-card').click(function() {
  $slide = $('.active').width();
  console.log($('.active').position().left);
 
  if ($(this).hasClass('next')) {
    $('.container').stop(false, true).animate({left: '-=' + $slide});
  } else if ($(this).hasClass('prev')) {
    $('.container').stop(false, true).animate({left: '+=' + $slide});
  }
 
  $(this).removeClass('prev next');
  $(this).siblings().removeClass('prev active next');
 
  $(this).addClass('active');
  $(this).prev().addClass('prev');
  $(this).next().addClass('next');
});

