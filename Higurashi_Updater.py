import os
import shutil
import filecmp

# Define source directories of Higurashi_Korean Git folder
# 쓰르라미 한패 Git 경로 설정
# Windows Example: C:\Users\Rena\Higurashi_Korean_Mac\Ch1\Contents\Resources\Data\StreamingAssets
# UNIX/macOS Example: /Users/Rena/Higu Kor/Higurashi_Korean_Mac/Ch1/Contents/Resources/Data/StreamingAssets
source_dirs = [
    "[PATH TO GIT FOLDER]/Higurashi_Korean_Mac/Ch1/Contents/Resources/Data/StreamingAssets",
    "[PATH TO GIT FOLDER]/Higurashi_Korean_Mac/Ch2/Contents/Resources/Data/StreamingAssets",
    "[PATH TO GIT FOLDER]/Higurashi_Korean_Mac/Ch3/Contents/Resources/Data/StreamingAssets",
    "[PATH TO GIT FOLDER]/Higurashi_Korean_Mac/Ch4/Contents/Resources/Data/StreamingAssets",
    "[PATH TO GIT FOLDER]/Higurashi_Korean_Mac/Ch5/Contents/Resources/Data/StreamingAssets",
    "[PATH TO GIT FOLDER]/Higurashi_Korean_Mac/Ch6/Contents/Resources/Data/StreamingAssets",
    "[PATH TO GIT FOLDER]/Higurashi_Korean_Mac/Ch7/Contents/Resources/Data/StreamingAssets",
    "[PATH TO GIT FOLDER]/Higurashi_Korean_Mac/Ch8/Contents/Resources/Data/StreamingAssets",
    "[PATH TO GIT FOLDER]/Higurashi_Korean_Mac/Ch9/Contents/Resources/Data/StreamingAssets"
]

# Define destination for folders containing korean patch files (in a folder) for release
# 쓰르라미 한패 배포 파일 폴더 경로 설정
# Windows Example: C:\Users\Rena\쓰르라미_1챕터_한글패치\HigurashiEp01_Data\StreamingAssets
# UNIX/macOS Example: /Users/Rena/Higurashi Patch Files/Higu_Ch1_Kor/Data/Contents/Resources/Data/StreamingAssets
first_dest_dirs = [
    "[PATCH FILES FOR CH1 DEST]/StreamingAssets",
    "[PATCH FILES FOR CH2 DEST]/StreamingAssets",
    "[PATCH FILES FOR CH3 DEST]/StreamingAssets",
    "[PATCH FILES FOR CH4 DEST]/StreamingAssets",
    "[PATCH FILES FOR CH5 DEST]/StreamingAssets",
    "[PATCH FILES FOR CH6 DEST]/StreamingAssets",
    "[PATCH FILES FOR CH7 DEST]/StreamingAssets",
    "[PATCH FILES FOR CH8 DEST]/StreamingAssets",
    "[PATCH FILES FOR CH9 DEST]/StreamingAssets"
]

# Define destination for StreamingAssets folder of each Higurashi Steam installations for each chapters (Ch1 to Ch9)
# 쓰르라미 스팀 설치 StreamingAssets 폴더 경로 설정 
# Windows Example: C:\Program Files (x86)\Steam\steamapps\common\Higurashi When They Cry\HigurashiEp01_Data\StreamingAssets
# UNIX/macOS Example: /Users/Rena/Library/Application Support/Steam/steamapps/common/Higurashi When They Cry/HigurashiEp01.app/Contents/Resources/Data/StreamingAssets
second_dest_dirs = [
    "[HIGURASHI CH1 STEAM DEST]/StreamingAssets",
    "[HIGURASHI CH2 STEAM DEST]/StreamingAssets",
    "[HIGURASHI CH3 STEAM DEST]/StreamingAssets",
    "[HIGURASHI CH4 STEAM DEST]/StreamingAssets",
    "[HIGURASHI CH5 STEAM DEST]/StreamingAssets",
    "[HIGURASHI CH6 STEAM DEST]/StreamingAssets",
    "[HIGURASHI CH7 STEAM DEST]/StreamingAssets",
    "[HIGURASHI CH8 STEAM DEST]/StreamingAssets",
    "[HIGURASHI CH9 STEAM DEST]/StreamingAssets"
]

# Define destination for CompiledUpdateScripts folder of each Higurashi Steam installations for each chapters (Ch1 to Ch9)
# 쓰르라미 컴파일 스크립트 폴더 경로 설정
# Windows Example: C:\Program Files (x86)\Steam\steamapps\common\Higurashi When They Cry\HigurashiEp01_Data\StreamingAssets\CompiledUpdateScripts
# UNIX/macOS Example: /Users/Rena/Library/Application Support/Steam/steamapps/common/Higurashi When They Cry/HigurashiEp01.app/Contents/Resources/Data/StreamingAssets/CompiledUpdateScripts
compiled_sources = [
    "[HIGURASHI CH1 STEAM DEST]/StreamingAssets/CompiledUpdateScripts",
    "[HIGURASHI CH2 STEAM DEST]/StreamingAssets/CompiledUpdateScripts",
    "[HIGURASHI CH3 STEAM DEST]/StreamingAssets/CompiledUpdateScripts",
    "[HIGURASHI CH4 STEAM DEST]/StreamingAssets/CompiledUpdateScripts",
    "[HIGURASHI CH5 STEAM DEST]/StreamingAssets/CompiledUpdateScripts",
    "[HIGURASHI CH6 STEAM DEST]/StreamingAssets/CompiledUpdateScripts",
    "[HIGURASHI CH7 STEAM DEST]/StreamingAssets/CompiledUpdateScripts",
    "[HIGURASHI CH8 STEAM DEST]/StreamingAssets/CompiledUpdateScripts",
    "[HIGURASHI CH9 STEAM DEST]/StreamingAssets/CompiledUpdateScripts"
]

# Define destination for CompiledUpdateScripts of each korean patch files folder for each chapters (Ch1 to Ch9)
# 쓰르라미 한패 배포 컴파일 스크립트 폴더 경로 설정
# Windows Example: C:\Users\Rena\쓰르라미_1챕터_한글패치\HigurashiEp01_Data\StreamingAssets\CompiledUpdateScripts
# UNIX/macOS Example: /Users/Rena/Higurashi Patch Files/Higu_Ch1_Kor/Data/Contents/Resources/Data/StreamingAssets/CompiledUpdateScripts
compiled_destinations = [
    "[PATCH FILES FOR CH1 DEST]/StreamingAssets/CompiledUpdateScripts",
    "[PATCH FILES FOR CH2 DEST]/StreamingAssets/CompiledUpdateScripts",
    "[PATCH FILES FOR CH3 DEST]/StreamingAssets/CompiledUpdateScripts",
    "[PATCH FILES FOR CH4 DEST]/StreamingAssets/CompiledUpdateScripts",
    "[PATCH FILES FOR CH5 DEST]/StreamingAssets/CompiledUpdateScripts",
    "[PATCH FILES FOR CH6 DEST]/StreamingAssets/CompiledUpdateScripts",
    "[PATCH FILES FOR CH7 DEST]/StreamingAssets/CompiledUpdateScripts",
    "[PATCH FILES FOR CH8 DEST]/StreamingAssets/CompiledUpdateScripts",
    "[PATCH FILES FOR CH9 DEST]/StreamingAssets/CompiledUpdateScripts"
]

# Function to copy only different files and log only copied files
def copy_if_different(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for root, dirs, files in os.walk(source):
        relative_root = os.path.relpath(root, source)
        dest_root = os.path.join(destination, relative_root)

        if not os.path.exists(dest_root):
            os.makedirs(dest_root)

        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(dest_root, file)

            if not os.path.exists(dest_file) or not filecmp.cmp(source_file, dest_file, shallow=False):
                shutil.copy2(source_file, dest_file)
                print(f"Change detected, copying: {source_file} to {dest_file}")

# Copy only different files to both sets of destinations
for i in range(len(source_dirs)):
    source = source_dirs[i]
    first_dest = first_dest_dirs[i]
    second_dest = second_dest_dirs[i]

    print(f"Copying from {source} to {first_dest}")
    copy_if_different(source, first_dest)

    print(f"Copying from {source} to {second_dest}")
    copy_if_different(source, second_dest)

# User prompt to confirm continuing with the second part
while True:
    proceed = input("Are all Higurashi scripts compiled on the game (y/n)? ").strip().lower()
    if proceed in ['y', 'n']:
        break
    print("Please answer 'y' or 'n'.")

if proceed == 'y':
    # Copy the `CompiledUpdateScripts` folders to their destinations
    for i in range(len(compiled_sources)):
        source = compiled_sources[i]
        destination = compiled_destinations[i]

        print(f"Copying from {source} to {destination}")
        copy_if_different(source, destination)

    print("All Korean Assets Have Been Applied to the Game and Patch Files (Ch1 to Ch9).")
else:
    print("Operation aborted.")
