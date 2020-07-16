window.addEventListener("load", function() {
  document.getElementById("txtFileUpload").onchange = function(event) {
    var reader = new FileReader();
    reader.readAsDataURL(event.srcElement.files[0]);
    var me = this;
    reader.onload = function () {
      var fileContent = reader.result;
	  console.log(fileContent);
    }
}});