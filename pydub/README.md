## 確認した環境
- OS: Mac OS10.15.2 Catarina
- Python: 3.7.4
- 使用パッケージ: pydub(python), ffmpeg(brew)

## ffmpegのダウンロード
### Macの場合
Homebrewインストール済で、
```bash
$ brew install ffmpeg
```
### Windowsの場合
[コチラ](https://fukatsu.tech/windows-ffmpeg)を参照

## 使用方法
### pydubのインストール
```bash
$ pip install pydub
```
### inputディレクトリにflacファイルを格納
__ディレクトリを再帰的にはみないため、ファイルのみ置くこと__
### pythonを起動
```bash
$ python flac2mp3.py
```
### outputディレクトリに返還後のmp3ファイルが格納される
同名のファイルがあった場合、上書きされる