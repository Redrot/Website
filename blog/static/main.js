$(function() {
  $.scrollify({
		section: ".post",
    afterRender: function() {
      $(".recent-post").on("click", $.scrollify.move);
    }
  });
});
