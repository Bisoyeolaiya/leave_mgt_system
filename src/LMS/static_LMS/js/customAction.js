$('#more').click(function () {
if($('button span').hasClass('glyphicon-chevron-down'))
{
    $('#more').html('<span class="glyphicon glyphicon-chevron-up"></span> Less Info'); 
}
else
{      
    $('#more').html('<span class="glyphicon glyphicon-chevron-down"></span> More Info'); 
}
}); 