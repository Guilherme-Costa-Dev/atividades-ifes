<html>
    <body>
        <?php
            date_default_timezone_set("America/Sao_Paulo");

            $agora    = date("d/m/Y H:i:s");
            $amanha   = date("d/m/Y", strtotime("+1 day"));
            $semana = date("d/m/Y", strtotime("+7 days"));

            echo "<p>Data e hora atual: $agora </p>";
            echo "<p>Amanhã: $amanha </p>";
            echo "<p>Daqui a 7 dias: $semana </p>";
        ?>

    </body>
</html>