$(function() {
    $( ".datepicker" ).datepicker({
    changeMonth: true,
    changeYear: true,
    yearRange: "1940:2000",
    dateFormat: "yy-mm-dd",
    defaultDate: new Date(2000, 01, 01)
    });
});
	