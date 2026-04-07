<?php
    include 'calc.php';

    $resultado = null;

    $valor1 = $_POST['valor1'];
    $valor2 = $_POST['valor2'];
    $operacao = $_POST['select'];

    switch ($operacao) {
        case "somar":
            $resultado = somar($valor1, $valor2);
            break;
        case "subtrair":
            $resultado = subtrair($valor1, $valor2);
            break;
        case "multiplicar":
            $resultado = multiplicar($valor1, $valor2);
            break;
        case "dividir":
            $resultado = dividir($valor1, $valor2);
            break;
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ativ2</title>
</head>
<body>
    <form method="post">
        <h2>Valor 1</h2>
        <input type="number" name="valor1" id="valor1" value="<?php echo $valor1; ?>"><br>
        <h2>Valor 2</h2>
        <input type="number" name="valor2" id="valor2" value="<?php echo $valor2; ?>"><br>
        <h2>Função</h2>
        <select name="select" id="select">
            <option value="somar">Somar</option>
            <option value="subtrair">Subtrair</option>
            <option value="multiplicar">Multiplicar</option>
            <option value="dividir">Dividir</option>
        </select><br><br>
        <button type="submit">Enviar</button>
        <button type="button" onclick="limpar()">Limpar</button>
    </form>
    <br>
    <input type="text" value="<?php echo $resultado; ?>" readonly>
</body>

<script>
    function limpar() {
        document.getElementById("valor1").value="";
        document.getElementById("valor2").value="";
    }
</script>

</html>