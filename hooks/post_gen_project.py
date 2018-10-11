import os


def main():
    remove_unused_files()
    print("All set up, enjoy.")


def remove_unused_files():
    working_dir = os.path.abspath(os.path.curdir)
    count_bases = '{{ cookiecutter.count_bases}}'
    reverse_comp = '{{ cookiecutter.reverse_comp}}'
    file_list = []
    if count_bases != 'y':
        file_list.append('feature_files/count_bases.py')
    if reverse_comp != 'y':
        file_list.append('feature_files/reverse_comp.py')
    delete_files(file_list, working_dir)


def delete_files(file_list, working_dir):
    for file in file_list:
        file_path = os.path.join(working_dir, file)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("Couldn't find file to remove in hook {}".format(file_path))


if __name__ == '__main__':
    main()
