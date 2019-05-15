./john -wordlist=/usr/share/dict/words --rules=KoreLogicRulesL33t data.txt
./john --incremental:ASCII data.txt
./john --show data.txt > out
cat out
