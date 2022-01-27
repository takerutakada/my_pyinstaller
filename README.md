# my_pyinstaller

**概要**  
pyinstallerを実行後、以下を実行（exeファイル以外の生成物を掃除する）  
*生成されたexeファイルを元のpyファイルと同じディレクトリに移動  
*dist、buildディレクトリ及びディレクトリ内のファイル、specファイルを削除  


**引数**  
*関数に格納されている固定引数  
--onefile --exclude numpy --exclude pandas  
*必須引数  
exe化したいpyファイルのフルパス  
*オプション引数  
exe化した際コンソールを表示するか否か。  
必須引数の次に何らかの文字列を入れれば「--noconsole」がpyinstallerの引数に追加される  

**実行方法**  
コマンドラインで以下実行  
```  
python my_pyinstaller.py path/to/py/file.py 　←コンソールを表示する場合  
python my_pyinstaller.py path/to/py/file.py n ←コンソールを表示しない場合  
```
