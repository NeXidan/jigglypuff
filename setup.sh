pip install -U -r requirements.txt

rm -R -f pip_modules/
git clone https://github.com/AHAAAAAAA/PokemonGo-Map.git modules/PokemonGo-Map
pip install -U -r modules/PokemonGo-Map/requirements.txt
