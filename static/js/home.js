jarallax(document.querySelectorAll('.jarallax'), {
    speed: 0.2
});
$(window).scroll(function() {

  var scrollTop = $(window).scrollTop();
  var blurFactor = 25; // Decrease number for more intensity
  var blurstring = "blur("+scrollTop/blurFactor+"px)";
  $("#image").css({
    "-webkit-filter": blurstring,
    "filter": blurstring
  });

  var newCov = ('0.1' * scrollTop) / 80;
  // Decrease last number above to fade faster
  $('#cover').css('opacity', newCov);
  $("#cover").css({
    "-webkit-filter": blurstring,
    "filter": blurstring
  });

});