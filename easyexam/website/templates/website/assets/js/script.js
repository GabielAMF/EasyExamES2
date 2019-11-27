/// <reference path="../../typings/globals/jquery/index.d.ts" />

function validaTudoFunction(e) {
    //alert("valida tudo")
    e.preventDefault()

    let nome_valido = nomeValidoFunction()
    let sobren_valido = sobrenValidoFunction()
    let email_valido = emailValidoFunction()
    let peso_valido = pesoValidoFunction()
    let altura_valido = alturaValidoFunction()
    let idade_valido = idadeValidoFunction()
    let telefone_valido = telefoneValidoFunction()
    let endereco_valido = enderecoValidoFunction()

    if (nome_valido && sobren_valido && peso_valido && altura_valido && email_valido && telefone_valido && endereco_valido && idade_valido) {
        alert("Tudo Ok!")
        //$("#id-form").submit()
    }
    else {
        alert("Deu erro!")
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