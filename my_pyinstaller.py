from os.path import split
from os import remove
from sys import argv
from shutil import move, rmtree
import subprocess

file_path = argv[1]
file_dir, file_name = split(file_path)

def MyPyinstaller():
    """Customized pyinstaller
    Run pyinstaller, 

    move the generated exe file to the same directory as the original py file, 
    
    and delete the dist, build directories and spec file.
    
    static parameter : --onefile --exclude numpy --exclude pandas

    required parameter : file_path...py file(full path) to be converted to exe

    optional parameter : console...add console or not

    Ex1:python my_pyinstaller.py path/to/py/file.py  ...adding console
    
    Ex2:python my_pyinstaller.py path/to/py/file.py n...not adding console
    """

    # pyinstaller実行部分
    console = '--noconsole' if len(argv) == 3 else ''
    subprocess.call(f'python -m PyInstaller -F {console} --onefile --exclude numpy --exclude pandas {file_path}')
    print('pyinstaller complited.')

    # exe移動、不要ファイル・ディレクトリ削除
    move(f'dist/{file_name[:-3]}.exe', file_dir) 
    print(f'{file_name[:-3]}.exe moved.')
    rmtree('dist')
    rmtree('build')
    remove(f'{file_name[:-3]}.spec')
    print(f'dist,build,{file_name[:-3]}.spec removed.')
    print(f'complited. check {file_dir}')

if __name__ == '__main__':
    MyPyinstaller()