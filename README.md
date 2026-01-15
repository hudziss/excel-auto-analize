# Excel Auto-Analīze (Streamlit)

## Ko šī lietotne dara
Šī ir Streamlit lietotne, kas ļauj augšupielādēt Excel (.xlsx) failu un automātiski:
- parāda datu priekšskatījumu (preview),
- atrod skaitliskās un kategoriskās kolonnas,
- izveido pivot tabulu (sum/mean/count),
- uzzīmē 2 grafikus (stabiņu grafiku no pivot Top 15 un histogrammu),
- ļauj lejupielādēt pivot rezultātu kā CSV.

## Kā palaist (lokāli)
### Prasības
- Python 3.9+ (ieteicams 3.10–3.12)

### Instalācija
Atver termināli projekta mapē un izpildi:


python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py

## Kā lietot

1. Atver lietotni pārlūkā:
http://localhost:8502

2. Augšupielādē Excel failu ar paplašinājumu `.xlsx`.

3. Apskati:
- datu priekšskatījumu (preview),
- automātiski atpazītās skaitliskās un kategoriskās kolonnas.

4. Izvēlies pivot tabulas parametrus:
- **Rindu dimensiju** (kategoriskā kolonna),
- **Vērtību kolonnu** (skaitliskā kolonna),
- **Agregāciju** (`sum`, `mean` vai `count`).

5. Apskati:
- pivot tabulu,
- stabiņu grafiku (Top 15 pēc pivot),
- histogrammu izvēlētajai skaitliskajai kolonnai.

6. Lejupielādē pivot rezultātu kā CSV failu.

---

## Galvenās tehnoloģijas / bibliotēkas

- **Streamlit** – lietotnes lietotāja interfeiss un palaišana pārlūkā
- **Pandas** – datu apstrāde un pivot tabulu veidošana
- **Openpyxl** – Excel (`.xlsx`) failu lasīšana
- **Plotly Express** – interaktīvo grafiku ģenerēšana

