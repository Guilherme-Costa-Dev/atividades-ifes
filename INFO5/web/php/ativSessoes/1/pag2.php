<html>
    <body>
        <?php
            session_start();
            if (! empty($_SESSION['logado']) ) {
                echo "Usuário logado como: <h1>  $_SESSION[logado] </h1>" ;
            } else {
                echo "é necessário iniciar a sessão";
            }
        ?>
    </body>
</html>