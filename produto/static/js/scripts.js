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
});

/*
$(document).ready(function(){ //cuaso queria mudar é só tirar o '{{request.get_full_path}}&'
    const b = document.querySelector(".page_next");
    const bpro = document.querySelector(".page_next");
    var base = window.location.href
    var baseUrl = window.location.origin + '/?page=2'
    console.log(base);

    if ((base === 'http://localhost:8000/') || (base === 'http://192.168.0.189:8000/')){
        b.href = baseUrl
        b.pro
        console.log('funcionou');
    }    
});*/