
## Mock 体温チェック

- `temperature.py` は，mock の体温を 35.8〜40.0℃ の乱数で生成するスクリプトです．
- `.github/workflows/temperature.yml` は，毎日 09:00 JST（00:00 UTC）に `temperature.py` を定期実行します．
- 必要に応じて，GitHub Actions の `workflow_dispatch` から手動実行もできます．
