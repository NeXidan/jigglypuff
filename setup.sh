pip install -U -r requirements.txt

mkdir tmp/
rm -R -f modules/
git clone --branch 2.0 https://github.com/AHAAAAAAA/PokemonGo-Map.git modules/PokemonGoMap
pip install -U -r modules/PokemonGoMap/requirements.txt

python ./app.py -u Dimitrinol -p asdfg987 -st 4 -l '27,51' --threads 10
