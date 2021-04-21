#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Module Name

    Description...

"""

__author__ = "Vinícius Pereira"
__copyright__ = "Copyright 2021, Vinícius Pereira"
__credits__ = ["Vinícius Pereira","etc."]
__date__ = "2021/04/12"
__license__ = "GPL"
__version__ = "1.0.0"
__pythonversion__ = "3.9.1"
__maintainer__ = "Vinícius Pereira"
__contact__ = "viniciuspsb@gmail.com"
__status__ = "Development"

import sys, os, shutil; sys.path.insert(0,os.getcwd())
import subprocess as sp
import time
import yaml
import main as mn
import enums.buildmode as bm


def build_py_script(script: str, 
                    buildmode: bm.BuildMode,
                    appmode: bm.ApplicationMode,
                    exe_name: str = None,
                    icon_file: str = None,
                    version_file: str = None,
                    resource_file: str = None,
                    hidden_imports: list = None,
                    dist_path: str = None,
                    build_path: str = None,
                    spec_path: str = None,
                    clean_cache: bool = False,
                    force_ascii: bool = False,
                    reset_build: bool = False,
                    standardize_dist: bool = False,
                    update_version_file: bool = True,
                    update_requeriments_file: bool = True,
                    update_setup_py: bool = True,
                    open_exe: bool = False) -> None:
    """
    Builds an executable from python script using pyinstaller.

    Args:
        script (str): The python script name to be built. 
        buildmode (bm.BuildMode): Build mode enum, which can be onedir or onefile.
        appmode (bm.ApplicationMode): Application mode enum, which can be console or 
            windowed.
        exe_name (str): Custom name to the executable to be built. Defaults to None.
        icon_file (str): A .ico file and path to the executable. Defaults to None.
        version_file (str): A version file and path to document the executable. Defaults
            to None.
        resource_file (str): A .qrc file and path to the executable. Defaults to None.
        hidden_imports (list): List of hidden module imports to the executable. Defaults
            to None.
        dist_path (str): Custom dist output directory. Defaults to None.
        build_path (str): Custom build output directory. Defaults to None.
        spec_path (str): Custom .spec file output directory. Defaults to None.
        clean_cache (bool): Clean PyInstaller cache and remove temporary files before 
            building. Defaults to False.
        force_ascii (bool): Do not include unicode encoding support. Defaults to False.
        reset_build (bool): Deletes build and dist folders before build the executable. 
            Defaults to False.
        standardize_dist (bool): Copy assets and fonts folders and README.md to the dist 
            folder. Defaults to False.
        update_version_file (bool): Updates the version file with pyinstaller-versionfile.
            Defaults to True.
        update_requeriments_file (bool): Updates the requeriments.txt with pigar.
            Defaults to True.
        update_setup_py (bool): Updates the setup.py script with setuppy-generator.
            Defaults to True.
        open_exe (bool): Opens the executable after the building. Defaults to False.

    Returns:
        None.
    """

    start = time.time()
    
    if update_version_file:
        try:
            with open(r'metadata.yml', 'w', encoding='utf-8') as file:
                documents = yaml.dump(mn.METADATA_DICT, file, sort_keys=False, allow_unicode=True)

            os.system("cd {} & create-version-file {} --outfile {}"
            .format(os.path.abspath(""), "metadata.yml", mn.VERSION_FILE))

            print("Python Builder Info: Version file created / updated.")
        except:
            print("Python Builder Error: Couldn't create / update the version file.")

    if update_requeriments_file:
        try:
            # os.system("cd {} & pigar -p ./requeriments.txt -P ./".format(os.path.abspath("")))
            p = sp.Popen("pigar --without-referenced-comments -p ./requirements.txt -P ./", stdin=sp.PIPE)
            p.communicate(b'n\n')
            print("Python Builder Info: Requeriments file created / updated.")
        except:
            print("Python Builder Error: Couldn't create / update the requirements file.")

    if update_setup_py:
        try:
            os.system("python -m setuppy_generator > setup.py")
            os.system("python -m setupcfg_generator & cat setup.cfg")
            print("Python Builder Info: setup.py script created / updated.")
        except:
            print("Python Builder Error: Couldn't create / update the setup.py script.")


    if reset_build:
        try:
            print("Python Builder Alert: The .spec files aren't deleted by the program.")
            shutil.rmtree(os.path.abspath("build"))
            shutil.rmtree(os.path.abspath("dist"))
            print("Python Builder Info: build and dist folders reseted.")
        except:
            print("Python Builder Error: Couldn't delete build and/or dist folders.")


    script_name = script.split(".")[0]
    command = "cd {} & pyinstaller".format(os.path.abspath(""))


    if buildmode == bm.BuildMode.onedir:
        command += " -D"
    elif buildmode == bm.BuildMode.onefile:
        command += " -F"
    
    if appmode == bm.ApplicationMode.console:
        command += " -c"
    elif appmode == bm.ApplicationMode.windowed:
        command += " -w"

    if exe_name:
        command += " -n {}".format(exe_name)

    if icon_file:
        command += " -i {}".format(icon_file)
    
    if version_file:
        command += " --version-file {}".format(version_file)

    if resource_file:
        command += " -r {}".format(resource_file)
    
    if hidden_imports:
        for module in hidden_imports:
           command += " --hiddenimport {}".format(module) 

    if dist_path:
        command += " --distpath {}".format(dist_path)

    if build_path:
        command += " --workpath {}".format(build_path)
    
    if spec_path:
        command += " --specpath {}".format(spec_path)

    if clean_cache:
        command += " --clean"
    
    if force_ascii:
        command += " --ascii"

    command += " {}".format(script)

    print("---------------------------------------------")
    print("Python Builder Command:", command)
    print("---------------------------------------------")
    
    try:
        print("=============================================")
        print("Python Builder Info: Starting the building...")
        print("=============================================")
        os.system(command)
    except Exception as e:
        print("=============================================")
        print("Python Builder Error:", e)
    else:
        print("=============================================")
        print("Python Builder Info: Building completed.")
        print("=============================================")

    if standardize_dist:
        try:
            if  buildmode == bm.BuildMode.onefile:
                shutil.copytree(os.path.abspath("assets"),os.path.abspath("dist/assets"))
                shutil.copytree(os.path.abspath("fonts"),os.path.abspath("dist/fonts"))
                shutil.copyfile(os.path.abspath("README.md"),os.path.abspath("dist/README.md"))
            else:
                if exe_name:
                    shutil.copytree(os.path.abspath("assets"),os.path.abspath("dist/{}/assets".format(exe_name)))
                    shutil.copytree(os.path.abspath("fonts"),os.path.abspath("dist/{}/fonts".format(exe_name)))
                    shutil.copyfile(os.path.abspath("README.md"),os.path.abspath("dist/{}/README.md".format(exe_name)))
                else:
                    shutil.copytree(os.path.abspath("assets"),os.path.abspath("dist/{}/assets".format(script_name)))
                    shutil.copytree(os.path.abspath("fonts"),os.path.abspath("dist/{}/fonts".format(script_name)))
                    shutil.copyfile(os.path.abspath("README.md"),os.path.abspath("dist/{}/README.md".format(script_name)))
            
            print("Python Builder Info: dist folder standardized.")
        except:
            print("Python Builder Error: Failed to standardize the dist folder.")
    
    end = time.time()
    print("Python Builder Info: Time elapsed - {} seconds.".format(format(end - start, ".3f")))

    if open_exe: 
        try:
            print("Python Builder Info: Opening the executable...")
            if buildmode == bm.BuildMode.onefile and exe_name:
                os.system(os.path.abspath("dist\{}.exe".format(exe_name)))
            elif buildmode == bm.BuildMode.onedir and exe_name:
                os.system(os.path.abspath("dist\{0}\{0}.exe".format(exe_name)))
            elif buildmode == bm.BuildMode.onefile and not exe_name:
                os.system(os.path.abspath("dist\{}.exe".format(script_name)))
            elif buildmode == bm.BuildMode.onedir and not exe_name:
                os.system(os.path.abspath("dist\{0}\{0}.exe".format(script_name)))
        except:
            print("Python Builder Error: Failed to open executable.")
        

if __name__ == "__main__":
    build_py_script("main.py",bm.BuildMode.onedir, bm.ApplicationMode.windowed, mn.EXE_NAME, mn.ICON_FILE, mn.VERSION_FILE, 
                    reset_build=True, standardize_dist=True, open_exe=True)