<html>
    <body>
        <form action="index.php" method="post">
            <p>Informe o valor:</p>
            <input type="text" name="val"><br><br>
            <button type="submit">Converter</button>
        </form>

        <?php
            $val = $_POST["val"];

            if (is_numeric($val)){
                $num = floatval($val);
                $real = number_format($val, 2, ",", ".");
                echo "<p>R$ $real </p>";
            } else {
                if ($val == null){
                    
                } else {
                    echo "<p>ERRO. Digite apenas números</p>";
                }
            }
        ?>

    </body>
</html>

