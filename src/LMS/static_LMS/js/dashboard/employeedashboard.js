$(document).ready(
function () {
    $('.descText').hide();
    $('select#leave_type').on("change",function () {
    var toshow = $('p#desc'+$(this).val())
    console.log(toshow)
    toshow.show()
    }
    )
    
  })

 
