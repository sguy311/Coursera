$file = gc "~/fix.txt"
$regex = "(^\W+\d+)"
foreach($line in $file){if($line -match $regex){$out = $line.replace($matches[1],"")
                                                $out | out-file "~/fixed.txt" -append -Verbose}}
                        