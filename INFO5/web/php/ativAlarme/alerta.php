<?php

    $hora = $_GET["hora"];
    $assunto = $_GET["assunto"];
?>

<!DOCTYPE html>
<html lang="pt-BR">
    
<head>
    <meta charset="UTF-8">
    <title>ALERTA</title>
    <style>
        body{
            background-color: black;
            color: red;
            text-align: center;
            margin-top: 200px;
            font-size: 40px;
            font-family: Arial;
        }
        .pisca{
            animation: piscar 2s infinite;
        }
        @keyframes piscar {

            0% {
                opacity: 1;
            }

            50% {
                opacity: 0;
            }

            100% {
                opacity: 1;
            }
        }
    </style>
</head>

<body>
<div class="pisca">
    COMPROMISSO AGORA!<br><br>
    <?php
        echo $hora . "<br><br>";
        echo $assunto;
    ?>
</div>
</body>

</html>
