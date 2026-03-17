var lista = [];

function incluir(){
    nome = document.getElementById("nome").value;
    tel = document.getElementById("tel").value;
    email = document.getElementById("email").value;
    endereco = document.getElementById("endereco").value;

    if (nome == ""){
        alert("Insira o nome");
    } else{ if (tel == ""){
            alert("Insira o telefone")
        } else{
            lista.push(nome);
            lista.push(email);
            lista.push(endereco);
            lista.push(tel);
        }
    }
}

function listar(){
    
    html = "<table border='1'>";
    html += "<br>";
    html += "<tr><th>Nome</th><th>Email</th><th>Endereço</th><th>Telefone</th></tr>";

    for(let i=0; i<lista.length; i+=4){
        html += "<tr>";
        html += "<td>"+lista[i]+"</td>";
        html += "<td>"+lista[i+1]+"</td>";
        html += "<td>"+lista[i+2]+"</td>";
        html += "<td>"+lista[i+3]+"</td>";
        html += "</tr>";
    }
    html += "</table>";
    document.getElementById("tabela").innerHTML = html;
}

function pesquisarNome(){
    nome = document.getElementById("pesquisa").value;

    for(let i = 0; i < lista.length; i+=4){
        if (nome == lista[i]){
            html = "<table border='1'>";
            html += "<tr><th>Nome</th><th>Email</th><th>Endereço</th><th>Telefone</th></tr>";

            html += "<tr>";
            html += "<td>"+lista[i]+"</td>";
            html += "<td>"+lista[i+1]+"</td>";
            html += "<td>"+lista[i+2]+"</td>";
            html += "<td>"+lista[i+3]+"</td>";
            html += "</tr>";
            
            html += "</table>";
            document.getElementById("tabelaPesquisa").innerHTML = html;
            var deuCerto = 1;   
        }
    }
    if (deuCerto != 1){
        alert("Nome não encontrado");
        document.getElementById("tabelaPesquisa").innerHTML = "";
    }
}

function apagarDados(){
    nome = document.getElementById("apagar").value;

    for(let i = 0; i < lista.length; i+=4){
        if (nome == lista[i]){
            lista.splice(i, 4)
            var deuCerto = 1;   
        }
    }
    if (deuCerto != 1){
        alert("Nome não encontrado");
    } else{
        alert("Apagado com sucesso")
    }

    listar()

}

function alterarDados(){
    var nome = document.getElementById("alterar").value;
    indice = -1;

    for (let i = 0; i < lista.length; i += 4) {
        if (nome == lista[i]) {
            indice = i;
            break;
        }
    }

    if (indice == -1) {
        alert("Nome não encontrado");
        return;
    }

    var html = `
        <br>
        <input type="text" id="novoNome" value="${lista[indice]}">
        <input type="text" id="novoEmail" value="${lista[indice + 1]}">
        <input type="text" id="novoEndereco" value="${lista[indice + 2]}">
        <input type="text" id="novoTel" value="${lista[indice + 3]}">
        <input type="button" value="Confirmar Alteração" onclick="confirmarAlteracao()">`;

    document.getElementById("tabelaAlterar").innerHTML = html;
}

function confirmarAlteracao() {
    var novoNome = document.getElementById("novoNome").value;
    var novoEmail = document.getElementById("novoEmail").value;
    var novoEndereco = document.getElementById("novoEndereco").value;
    var novoTel = document.getElementById("novoTel").value;

    if (novoNome == "") {
        alert("Insira o nome");
        return;
    }
    if (novoTel == "") {
        alert("Insira o telefone");
        return;
    }

    lista[indice] = novoNome;
    lista[indice + 1] = novoEmail;
    lista[indice + 2] = novoEndereco;
    lista[indice + 3] = novoTel;

    alert("Dados alterados com sucesso");
    listar();
    document.getElementById("tabelaAlterar").innerHTML = "";
}
