
$(document).ready(function () {
    $("#btnSubmit").click(function (event) {
        //stop submit the form, we will post it manually.
        event.preventDefault();
        var query = $('#fileUploadForm').serialize();
		// disabled the submit button
        $("#btnSubmit").prop("disabled", true);

        $.ajax({
            type: "GET",
            //enctype: 'multipart/form-data',
            url: "get_highlights",
            data: query,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
            success: function (data) {
                var obj = JSON.parse(data);
                if(jQuery.isEmptyObject(obj)){
                    showError();
                }
                else{
                    showData(obj)
                }
            },
            error: function (e) {
                $("#result").text(e.responseText);
                console.log("ERROR : ", e);
                $("#btnSubmit").prop("disabled", false);
            }
        });
    });
    $("#btnSubmit-POI").click(function (event) {
        //stop submit the form, we will post it manually.
        event.preventDefault();
        var query = $('#UploadFormPOI').serialize();
		// disabled the submit button
        $("#btnSubmit-POI").prop("disabled", true);

        $.ajax({
            type: "GET",
            //enctype: 'multipart/form-data',
            url: "get_closest",
            data: query,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
            success: function (data) {
                var obj = JSON.parse(data);
                if(jQuery.isEmptyObject(obj)){
                    showError();
                }
                else{
                    showData_poi(obj)
                }
            },
            error: function (e) {
                $("#result").text(e.responseText);
                console.log("ERROR : ", e);
                $("#btnSubmit-POI").prop("disabled", false);
            }
        });
    });
});
function showError() {
    console.log("empty");
    $("#empty-result").fadeIn(150);
    $("#btnSubmit").prop("disabled", false);
    $("#btnSubmit-POI").prop("disabled", false);
}
function showData(obj){
    console.log("success", obj);
    $('#show-highlights').append(obj)
    $("#btnSubmit").prop("disabled", false);
}
function showData_poi(obj){
    console.log("success - closest poi", obj);
//    $('#show-highlights').text(JSON.stringify(obj))
    $('#show-nearest-poi').append(obj)
    $("#btnSubmit-POI").prop("disabled", false);
}