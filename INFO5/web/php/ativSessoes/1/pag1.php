<html>
    <?php
        session_start();
        if (isset($_REQUEST["login"])) {
            $_SESSION['logado'] = $_REQUEST["login"];
            echo "Sessão iniciada" ;
        }
    ?>
    <head>
        <title>Atividade sessoes - 2</title>
    </head>

    <script>
        function abrirPag() {
            window.location.href = "pag2.php";
        }
    </script>

    <body>
        <form action="pag1.php">
            Informe o login: <br>
            <input type="text" name="login"> <br><br>
            <input type="submit" value="Incluir"><br><br>
            <input type="button" value="Abrir pág 2" onclick="abrirPag()"> <br>
        </form>
    </body>
</html>