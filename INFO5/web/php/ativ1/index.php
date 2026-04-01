<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Atividade 1 php</title>
</head>
<body>

<h2>1 - Digite um valor:</h2>

<form method="post">
    <input type="number" name="valor1">
    <button type="submit">Enviar</button>
    <br><br>
</form>

<?php
    $valor = $_POST["valor1"];

    if ($valor > 0) {
        echo "Valor Positivo";
    } elseif ($valor < 0) {
        echo "Valor Negativo";
    } elseif ($valor == 0) {
        echo "Igual a Zero";
    }
?>

<h2>2 - Digite os valores: </h2>

<form method="post">
    <input type="number" name="a2">
    <input type="number" name="b2">
    <input type="number" name="c2">
    <input type="number" name="d2">
    <button type="submit">Enviar</button>
</form>
<br>

<?php
    $a = $_POST["a2"];
    $b = $_POST["b2"];
    $c = $_POST["c2"];
    $d = $_POST["d2"];

    $soma = $a + $c;
    $mult = $b * $d;

    if ($soma > $mult) {
        echo "A+C é maior que B*D";
    } elseif ($mult > $soma) {
        echo "A+C é menor que B*D";
    } elseif ($mult == $soma) {
        echo "A+C é igual a B*D";
    }
?>

<h2>3 - Digite A e B: </h2>

<form method="post">
    <input type="number" name="a3">
    <input type="number" name="b3">
    <button type="submit">Enviar</button>
</form>
<br>

<?php
    $a = $_POST["a3"];
    $b = $_POST["b3"];

    if ($a > $b) {
        echo $b, $a;
    } elseif ($a < $b) {
        echo $a, $b;
    } elseif ($a == $b) {
        echo $a, $a;
    }
?>

<h2>4 - Digite o salario: </h2>

<form method="post">
    <input type="number" name="sal">
    <button type="submit">Enviar</button>
</form>
<br>

<?php
    $sal = $_POST["sal"];
    if ($sal <= 300) {
        $sal = $sal+$sal*0.50;
    } elseif ($sal >= 300) {
        $sal = $sal+$sal*0.70;
    }
    echo $sal;
?>

<h2>5 - Digite 2 valores: </h2>

<form method="post">
    <input type="number" name="a5">
    <input type="number" name="b5">
    <button type="submit">Enviar</button>
</form>

<?php
    $a = $_POST["a5"];
    $b = $_POST["b5"];

    if ($a <= $b) {
        for ($i = $a; $i <= $b; $i++) {
            echo "$i ";
        }
    } elseif ($a > $b) {
        echo "Primeiro numero é maior que o segundo";
    }
?>

<h2>6 - Digite 2 valores: </h2>

<form method="post">
    <input type="number" name="a6">
    <input type="number" name="b6">
    <button type="submit">Enviar</button>
</form> 

<?php
    $a = $_POST["a6"];
    $b = $_POST["b6"];

    $listaPar = [];
    $listaImpar = [];

    if ($a <= $b) {
        for ($i = $a; $i <= $b; $i++) {
            if ($i%2 == 0) {
                $listaPar[] = $i;
            } else {
                $listaImpar[] = $i;
            }
        }
        echo "Par: ";
        foreach($listaPar as $sim) {
            echo "$sim, ";
        }
        echo "Impar: ";
        foreach($listaImpar as $sim) {
            echo "$sim, ";
        }
    } else{
        echo "Primeiro numero é maior que o segundo";
    }
?>
</body>
</html>