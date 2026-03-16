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
    }
}

function apagarDados(){
    nome = document.getElementById("pesquisa").value;

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

function alterar(){
    let nomePesquisa = document.getElementById("pesquisa").value;
    let novoNome = document.getElementById("nome").value;
    let novoTel = document.getElementById("tel").value;
    let novoEmail = document.getElementById("email").value;
    let novoEndereco = document.getElementById("endereco").value;

    if (nomePesquisa == "") {
        alert("Digite o nome no campo de pesquisa para alterar");
        return;
    }

    let deuCerto = 0;

    for (let i = 0; i < lista.length; i += 4) {
        if (nomePesquisa == lista[i]) {
            lista[i] = novoNome || lista[i];
            lista[i+1] = novoEmail || lista[i+1];
            lista[i+2] = novoEndereco || lista[i+2];
            lista[i+3] = novoTel || lista[i+3];
            deuCerto = 1;
            break;
        }
    }

    if (deuCerto != 1) {
        alert("Nome não encontrado");
    } else {
        alert("Alterado com sucesso!");
        listar();
    }
}

