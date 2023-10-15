// 当页面加载完成后执行的代码
"use strict";
$(document).ready(function () {
  // 使用Ajax请求获取数据
  $.ajax({
    url: "/get_data",
    type: "GET",
    success: function (response) {
      // 在页面上显示从Flask获取的数据
      $("#data-container").text(response.message);
      // console.log(response);
    },
    error: function () {
      alert("无法获取数据。");
    },
  });
});
