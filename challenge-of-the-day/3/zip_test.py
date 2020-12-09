import pytest
import zip

assert zip.zipped("String","Fridge") == "SFtrriidngge"

assert zip.zipped("Dog","Cat") == "DCoagt"

assert zip.zipped("True","Tree") == "TTrrueee" 

assert zip.zipped("return","letter") == "rleettutrenr"

assert zip.zipped("dog", "kitten") == "these strings are different lengths!"

assert zip.zipped("walRus", "FreedO") == "wFarleReudsO"