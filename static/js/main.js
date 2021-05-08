$(function () {
  $("button").click(function () {
    var user = $("#inputUsername").val();
    $.ajax({
      url: "/main",
      data: $("form").serialize(),
      type: "POST",
      success: function (response) {
        console.log(response);
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
});
