$(function() {
  $.scrollify({
		section: ".scrollable",
    afterRender: function() {
      $(".recent-post").on("click", $.scrollify.move);
    }
  });
});
