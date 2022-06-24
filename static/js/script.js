$(document).ready(function (){
    
    $('.btn').click(function() {
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_text: $(this).text()
            },
            success: function(response) {
                $('.btn').text(response.seconds)
            }
        })

    })

})


$(document).ready(function() {

    $('form').on('submit', function(event) {

        $.ajax({
            data: {
                nome : $('#nome').val(),
                caps : $('#caps').val(),
                volumes : $('#volumes').val(),
                autor : $('#autor').val(),
                ano : $('#ano').val()
            },
            type: 'POST',
            url: '/add_manga'
        })

        event.preventDefault();

    });

});



