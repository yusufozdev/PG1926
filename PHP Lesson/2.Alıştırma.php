<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asal Sayı Alıştırması</title>
    
</head>
<body>
    <div>
    <h1>Asal Sayı</h1>

        
        <form>
            <label>Lütfen sayı giriniz:</label>
            <input type="number" id="sadı" name="sayi" value="Sayıyı Giriniz"><br><br>
            <input type="submit" value="Sayı asal mı ?">
        </form><br>
            <?php 
                
                $variable = $_GET["sayi"];

                $asalsayı=0; $i=2;
 
                do
                {
                    if ($variable % $i == 0)
                    {
                        $asalsayı = 1;
                    }
                    $i++;
                }
                while($i<$variable);
                 
                if ($asalsayı != 1)
                {
                    $result="Sayı asaldır.";
                }
                else if ($variable == 2)
                {
                    $result="Sayı asaldır.";
                }
                else 
                {
                    $result="Sayı asal değildir."; 
                }

                echo $variable;
                echo $result;
                ?>
                
                
                    
            
     </div>

    </body>
</html>
