
$(document).ready(function () {

    $("#btnSubmit").click(function (event) {
        //stop submit the form, we will post it manually.
        event.preventDefault();

        var query = $('#fileUploadForm').serialize();

//        console.log(query);

		// disabled the submit button
        $("#btnSubmit").prop("disabled", true);

        $.ajax({
            type: "GET",
            //enctype: 'multipart/form-data',
            url: "sendQuery",
            data: query,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
            success: function (data) {
                console.log("SUCCESS : ", data);
                var obj = JSON.parse(data);
                //console.log("obj: ", obj);

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
});

function showError() {
    console.log("empty");
    $("#empty-result").fadeIn(150);
    $("#btnSubmit").prop("disabled", false);
}

function showData(obj){
    console.log("success", obj);

    $("#btnSubmit").prop("disabled", false);

}