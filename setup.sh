pip install -U -r requirements.txt

mkdir tmp/
rm -R -f modules/
git clone https://github.com/AHAAAAAAA/PokemonGo-Map.git modules/PokemonGoMap
pip install -U -r modules/PokemonGoMap/requirements.txt

python ./app.py
