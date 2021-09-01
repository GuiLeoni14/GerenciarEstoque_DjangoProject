$( document ).ready(function() {
    var btnDel = $('.btnDel');
    var sair = $('#sair')

    $(btnDel).on('click', function(e) {

        e.preventDefault();

        var btnDelLink = $(this).attr('href');
        var result = confirm('Eii, psiu!! Deseja mesmo deletar? ');

        if(result) {
            window.location.href = btnDelLink;
        }

    });
});

$(document).ready(function(){
    var baseUrl = window.location.origin + '/';
    var filter = $('#filter');
    var filterAlf = $('#filterAlf');
    var baseUrl_tipo_produto = window.location.origin + '/table';
    var tipo_produto = $('#tipo_produto');


    $(filter).change(function() {
       var filter = $(this).val();
       console.log(baseUrl)
       window.location.href = baseUrl + '?filter=' + filter;
    });

    $(filterAlf).change(function() {
       var filterAlf = $(this).val();
       console.log(filterAlf)
       window.location.href = baseUrl + '?filterAlf=' + filterAlf;
    });

    $(tipo_produto).change(function() {
        var tipo_produto = $(this).val();
        console.log(tipo_produto)
        window.location.href = baseUrl_tipo_produto + '?tipo_produto=' + tipo_produto;
     });

});