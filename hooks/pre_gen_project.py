
def validate():
    full_name = '{{ cookiecutter.full_name }}'
    if full_name.strip() == 'required':
        raise Exception("Must specify a full name to use this template")

if __name__ == '__main__':
    validate()
