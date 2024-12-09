import os

def unzipGlbs(glbs_zip_folder_path: str,
              objaverse_glbs_folder_path: str
              ) -> bool:
    if not os.path.exists(glbs_zip_folder_path):
        print('[ERROR][unzip_glbs::unzipGlbs]')
        print('\t glbs zip folder not exist!')
        print('\t glbs_zip_folder_path:', glbs_zip_folder_path)

        return False

    glbs_zip_filename_list = os.listdir(glbs_zip_folder_path)
    glbs_zip_filename_list.sort()

    for glbs_zip_filename in glbs_zip_filename_list:
        if glbs_zip_filename[:5] != '000-0' or glbs_zip_filename[-4:] != '.zip':
            continue

        glbs_zip_file_path = glbs_zip_folder_path + glbs_zip_filename

        print('[INFO][unzip_glbs::unzipGlbs]')
        print('\t start unzip file:', glbs_zip_filename, '...')
        command = 'unzip -u ' + glbs_zip_file_path + ' -d ' + objaverse_glbs_folder_path

        os.system(command)

    return True

if __name__ == "__main__":
    glbs_zip_folder_path = os.environ['HOME'] + '/Downloads/'
    objaverse_glbs_folder_path = os.environ['HOME'] + '/chLi/Dataset/Objaverse_82K/glbs/'

    unzipGlbs(glbs_zip_folder_path, objaverse_glbs_folder_path)
