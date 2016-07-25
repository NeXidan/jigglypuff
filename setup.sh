pip install -U -r requirements.txt

mkdir tmp
rm -R -f modules
git clone --branch V2.0 https://github.com/AHAAAAAAA/PokemonGo-Map.git modules/PokemonGoMap
pip install -U -r modules/PokemonGoMap/requirements.txt

cp config.ini modules/PokemonGoMap/config/config.ini
python ./app.py -t 10 -se
