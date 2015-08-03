pycd - Pythonライブラリのディレクトリにcdする
=============================================

pycd
----

あるPythonライブラリを使っているとき，
そのライブラリのコードを読みたくなることはよくあります．
その理由は様々ですが，
コードを読むための最も効率的な方法は多くの場合そのファイルのある
ディレクトリへ移動することです．

[pycd](http://github.com/wkentaro/pycd)
はそのような状況で即座にそのライブラリあるディレクトリへ移動し，
コードを読むためのツールです．

インストールは`pip`でできます:

```sh
$ pip install pycd
```

[pycd](http://github.com/wkentaro/pycd)
はカレントディレクトリを変更するツールのため，
シェル関数である必要があります．
関数をロードするために以下の行を
シェルの設定ファイル(`.bashrc`や`.zshrc`)に
追加してください．

```sh
# this is for pycd
source `which pycd.sh`
```

使い方は至ってシンプルです:

```sh
$ pycd
Usage: pycd <package_name>
$ pycd sklearn
$ pwd
/usr/local/lib/python2.7/site-packages/sklearn
```
`<package_name>`には，パッケージを`import`する際の名前を与えます．


pypack
------

`pip show <package_name>`
はそれぞれのパッケージのインストール場所を教えてくれますが，
その際指定するパッケージ名はインストールの際に指定するもので，
コード内で`import`する際のものとは異なります．

そのため，
[pycd](http://github.com/wkentaro/pycd)
は`pip`では得られない情報を得るためのコマンドラインツールとして
作られたのが`pypack`です．
これは`pycd`をインストールした際に同様にインストールされます．

`pypack`は`pip`を補うツールなので，シンプルなコマンドしかありません．

```sh
$ pypack help
pypack: command line tool to handle python packages.

Usage:
    pypack <command>
Commands:
    list - get package list
    help - show help
    find - find package path

$ pypack list
numpy
scipy
sklearn

$ pypack find numpy
/usr/local/lib/python2.7/site-packages/numpy
```
