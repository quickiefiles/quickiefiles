import os
import shutil

# [('/home/kingvcheese/Pictures', ['Screenshots'], ['JPEG_20240506_185336_758548092891764605.jpg', 'blackhole_upscayl_4x_realesrgan-x4plus.png', 'blackhole.jpg', 'layout-quickiefiles-website.png', 'JPEG_20240506_185314_995646919486069230.jpg', 'JPEG_20240501_174456_2071543589026879187.jpg']), ('/home/kingvcheese/Pictures/Screenshots', [], ['Screenshot from 2024-05-01 19-42-00.png', 'Screenshot from 2024-05-03 17-29-36.png', 'Screenshot from 2024-05-06 18-25-41.png'])]

class search:
    def __init__(self) -> None:
        self.base_search_path = "/home/kingvcheese/Pictures"

    
    def search_recursive(self, search_path):
        search_results = []
        
        for root, d_names, f_names in os.walk(search_path):
            search_results.append((root, d_names, f_names))
            
        return search_results
    
    def get_folders(self, Search_path):
        folders = []
        recursive = self.search_recursive(Search_path)

        for i in range(len(recursive)):
            folders.append(recursive[i][0])
        
        folders.remove(Search_path) # <--- if something goes wrong blame this single peice of fart >:(
        
        return folders
    
    def get_files(self, Search_path):
        files = []
        
        for item in os.listdir(Search_path):
            if os.path.isfile(os.path.join(Search_path, item)):
                files.append(item)
                
        return files
    
class htmlgen:
    def __init__(self) -> None:
        pass
    
    def gen_folder(self):
        pass
    
    def gen_preview(self):
        pass
    
    def gen_history(self):
        pass
    
    def gen_settings(self):
        pass
    
    def gen_properties(self):
        pass
    