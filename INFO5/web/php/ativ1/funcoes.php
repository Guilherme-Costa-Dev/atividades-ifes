
<?php
    // Funcao A
    function Asdf($valor) {}
    $valor = $_POST["valor1"];
    if ($valor > 0) {
        echo "Valor Positivo";
    } elseif ($valor < 0) {
        echo "Valor Negativo";
    } elseif ($valor == 0) {
        echo "Igual a Zero";
    }
?>
