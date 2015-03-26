$(document).ready(function() {

    $("#start_date").datepicker();
    $("#end_date").datepicker();
    $("#button1").click(function() {
        var start = $("#start_date").val();
        var end = $("#end_date").val();
        var purpose = $("#purpose").val();
     

        if (start === ""){
            document.getElementById("error_start_date").innerHTML = "Required";
        } 
        else {
            document.getElementById("error_start_date").innerHTML = "";
        } 

        if (end === ""){
            document.getElementById("error_end_date").innerHTML= "Required";
        } 
        else{
        document.getElementById("error_end_date").innerHTML = "";
        } 
        if (purpose === ""){
            document.getElementById("error_purpose").innerHTML = "Required";
        }
        else{ 
        document.getElementById("error_purpose").innerHTML = "";
        } 
    });
});
