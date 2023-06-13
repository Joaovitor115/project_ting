from ting_file_management import file_management as my_function


def process(path_file, instance):
    if path_file in instance.queue:
        return None

    file_list = my_function.txt_importer(path_file)
    instance.enqueue(file_list)
    print(
        {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_list),
            "linhas_do_arquivo": file_list,
        }
    )


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
