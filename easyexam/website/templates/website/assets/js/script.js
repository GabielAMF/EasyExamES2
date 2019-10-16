/// <reference path="../../typings/globals/jquery/index.d.ts" />

$(function () {
    $('[data-toggle="tooltip"]').tooltip({ boundary: 'window' });
    $('[data-toggle="popover"]').popover();

    // $("#nome").addEventListener("blur", function() { nomeValidoFunction() }, false)
    $("#id-form").submit(function (e) { validaTudoFunction(e) })

    //$("#").addEventListener("click", rankFunction());

    $("#btn1").click(function () {
        let like = $("#like").data("like")
        let dislike = $("#dislike").data("dislike")

        $("#like").data("like", like+1)

        $("#like").addClass("badge badge-secondary")
        $("#dislike").addClass("badge badge-secondary")

        $("#like").text(like)
        $("#dislike").text(dislike)
    })

    $("#btn2").click(function() {
        let like = $("#like").data("like")
        let dislike = $("#dislike").data("dislike")
  
        $("#dislike").data("dislike", dislike+1)

        $("#like").addClass("badge badge-secondary")
        $("#dislike").addClass("badge badge-secondary")

        $("#like").text(like)
        $("#dislike").text(dislike)
     })
});


function validaTudoFunction(e) {
    //alert("valida tudo")
    e.preventDefault()

    let nome_valido = nomeValidoFunction()
    let pgto_valido = pgtoValidoFunction()
    let arranjo_valido = arranjoValidoFunction()
    let cores_valida = coresValidaFunction()
    let email_valido = emailValidoFunction()
    let telefone_valido = telefoneValidoFunction()
    let endereco_valido = enderecoValidoFunction()

    if (nome_valido && pgto_valido && arranjo_valido && cores_valida && email_valido && telefone_valido && endereco_valido) {
        alert("Tudo Ok!")
        //$("#id-form").submit()
    }
    else {
        alert("Deu erro!")
    }
}

function coresValidaFunction() {
    let branca = $("#branca")
    let amarela = $("#amarela")
    let azul = $("#azul")
    let verde = $("#verde")
    let vermelha = $("#vermelha")
    let rosa = $("#rosa")
    let laranja = $("#laranja")
    let cores_feedback = $("#cores-feedback")

    let botoes = $("input.cores:checked")
    if (botoes.length === 0) {
        branca.addClass("is-invalid")
        branca.removeClass("is-valid")
        amarela.addClass("is-invalid")
        amarela.removeClass("is-valid")
        azul.addClass("is-invalid")
        azul.removeClass("is-valid")
        verde.addClass("is-invalid")
        verde.removeClass("is-valid")
        vermelha.addClass("is-invalid")
        vermelha.removeClass("is-valid")
        rosa.addClass("is-invalid")
        rosa.removeClass("is-valid")
        laranja.addClass("is-invalid")
        laranja.removeClass("is-valid")
        cores_feedback.addClass("d-block")
        return false
    }
    else {
        branca.addClass("is-valid")
        branca.removeClass("is-invalid")
        amarela.addClass("is-valid")
        amarela.removeClass("is-invalid")
        azul.addClass("is-valid")
        azul.removeClass("is-invalid")
        verde.addClass("is-valid")
        verde.removeClass("is-invalid")
        vermelha.addClass("is-valid")
        vermelha.removeClass("is-invalid")
        rosa.addClass("is-valid")
        rosa.removeClass("is-invalid")
        laranja.addClass("is-valid")
        laranja.removeClass("is-invalid")
        cores_feedback.removeClass("d-block")
        return true
    }
}

function arranjoValidoFunction() {
    let arranjo = $("#arranjo")

    if (arranjo.val() === '') {
        arranjo.addClass("is-invalid")
        arranjo.removeClass("is-valid")
        return false
    }
    else {
        arranjo.removeClass("is-invalid")
        arranjo.addClass("is-valid")
        return true
    }
}

function pgtoValidoFunction() {
    let pgto_cred = $("#pgto-cred")
    let pgto_deb = $("#pgto-deb")
    let pgto_din = $("#pgto-din")

    let pgto_feedback = $("#pgto-feedback")

    let botoes = $("input[name='pgto']:checked")
    if (botoes.length === 0) {
        pgto_cred.addClass("is-invalid")
        pgto_cred.removeClass("is-valid")
        pgto_deb.addClass("is-invalid")
        pgto_deb.removeClass("is-valid")
        pgto_din.addClass("is-invalid")
        pgto_din.removeClass("is-valid")
        pgto_feedback.addClass("d-block")
        return false
    }
    else {
        pgto_cred.removeClass("is-invalid")
        pgto_cred.addClass("is-valid")
        pgto_deb.removeClass("is-invalid")
        pgto_deb.addClass("is-valid")
        pgto_din.removeClass("is-invalid")
        pgto_din.addClass("is-valid")
        pgto_feedback.removeClass("d-block")
        return true
    }
}

function nomeValidoFunction() {
    //alert("nome valido")
    let nome = $("#nome")

    if (nome.val() === '') {
        nome.addClass("is-invalid")
        nome.removeClass("is-valid")
        return false
    }
    else {
        nome.removeClass("is-invalid")
        nome.addClass("is-valid")
        return true
    }
}

function emailValidoFunction() {
    //alert("nome valido")
    let email = $("#email")

    if (email.val() === '') {
        email.addClass("is-invalid")
        email.removeClass("is-valid")
        return false
    }
    else {
        email.removeClass("is-invalid")
        email.addClass("is-valid")
        return true
    }
}

function enderecoValidoFunction() {
    let endereco = $("#endereco")

    if (endereco.val() === '') {
        endereco.addClass("is-invalid")
        endereco.removeClass("is-valid")
        return false
    }
    else {
        endereco.removeClass("is-invalid")
        endereco.addClass("is-valid")
        return true
    }
}

function telefoneValidoFunction() {
    let telefone = $("#telefone")

    if (telefone.val() === '') {
        telefone.addClass("is-invalid")
        telefone.removeClass("is-valid")
        return false
    }
    else {
        telefone.removeClass("is-invalid")
        telefone.addClass("is-valid")
        return true
    }
}