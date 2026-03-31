<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Verificar Valor</title>
</head>
<body>

<h2>1 - Digite um valor:</h2>

<form method="post">
    <input type="number" name="valor">
    <button type="submit">Enviar</button>
    <br><br>
</form>

<?php
    $valor = $_POST["valor"];

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
    <input type="number" name="a">
    <input type="number" name="b">
    <input type="number" name="c">
    <input type="number" name="d">
    <button type="submit">Enviar</button>
</form>
<br>

<?php
    $a = $_POST["a"];
    $b = $_POST["b"];
    $c = $_POST["c"];
    $d = $_POST["d"];

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
    <input type="number" name="a">
    <input type="number" name="b">
    <button type="submit">Enviar</button>
</form>
<br>

<?php
    $a = $_POST["a"];
    $b = $_POST["b"];

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
    <input type="number" name="a">
    <input type="number" name="b">
    <button type="submit">Enviar</button>
</form>

<?php
    $a = $_POST["a"];
    $b = $_POST["b"];

    if ($a < $b) {
        for ($i = $a; $i <= $b; $i++) {
            echo $i;
        }
    } elseif ($a > $b) {
        echo "Primeiro numero é maior que o segundo";
    }
?>

</body>
</html>