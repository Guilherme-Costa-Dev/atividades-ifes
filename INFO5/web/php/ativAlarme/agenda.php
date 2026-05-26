<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Agenda</title>
</head>
<body>
    <h2>Relógio:</h2>
    <h1 id="relogio"></h1>

    <h3>Adicionar Compromisso</h3>
    <form id="formCompromisso">
        Horário (HH:MM): <input type="text" id="hora" required><br><br>
        Assunto: <input type="text" id="assunto" required><br><br>
        <button type="button" onclick="incluirComp()" >Gravar compromisso</button>
    </form>

    <script>
        // Cria o vetor dos compromissos salvos
        var compromissos = [];

        // Atualiza o relógio
        function atualizarRelogio() {
            // Pega a hora atual e formata
            var agora = new Date();
            var horas = String(agora.getHours()).padStart(2, '0');
            var minutos = String(agora.getMinutes()).padStart(2, '0');
            var segundos = String(agora.getSeconds()).padStart(2, '0');
            relogio = horas + ":" + minutos + ":" + segundos;

            document.getElementById("relogio").innerHTML = relogio; // Coloca a hora atual no html
            
            horaAtual = horas + ":" + minutos; // Formata a hora para comparar com a hora do compromisso
            
            // Verifica se está na hora do compromisso
            for (var i = 0; i < compromissos.length; i++) {
                if (compromissos[i].hora == horaAtual) {
                    alert("Lembrete: " + compromissos[i].assunto + " às " + compromissos[i].hora);
                    window.location.href = "alerta.php?hora=" +compromissos[i].hora + "&assunto=" + compromissos[i].assunto;
                }
            }
        }

        setInterval(atualizarRelogio, 1000);    // Atualiza o relógio a cada 1s

        // Cria objeto compromisso
        function compromisso(h, a) {
            this.hora = h;
            this.assunto = a;
        }

        // Função que inclui o compromisso no vetor
        function incluirComp () { 
            // Adiciona compromisso
            var hora = document.getElementById("hora").value;
            var assunto = document.getElementById("assunto").value;

            compromissos.push( new compromisso (hora, assunto) );
            alert("Compromisso salvo: " + assunto + " às " + hora);

        }
    </script>
</body>
</html>