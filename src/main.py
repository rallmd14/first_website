import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    for root, dirs, files in os.walk(dir_path_content):
        for filename in files:
            if filename =="index.md":
                to_path = os.path.join(dir_path_public, root.replace(dir_path_content, ""))
                generate_page(
                    os.path.join(root, "index.md"),
                    template_path,
                    os.path.join(dir_path_public, os.path.relpath(os.path.join(root, "index.md"), dir_path_content)).replace(".md", ".html"),
                )


main()
