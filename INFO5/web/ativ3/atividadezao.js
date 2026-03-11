var lista = [];

function incluir(){
    nome = document.getElementById("nome").value;
    tel = document.getElementById("tel").value;
    email = document.getElementById("email").value;
    endereco = document.getElementById("endereco").value;

    if (nome == ""){
        alert("Insira o nome");
    } else{
        if (tel == ""){
            alert("Insira o telefone");
        } else{
            lista.push(nome);
            lista.push(tel);
            lista.push(email);
            lista.push(endereco);
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

