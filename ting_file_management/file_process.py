from ting_file_management import file_management as my_function


def process(path_file, instance):
    for element in instance.queue:
        if element.get("nome_do_arquivo") == path_file:
            return None

    file_list = my_function.txt_importer(path_file)
    content = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_list),
            "linhas_do_arquivo": file_list,
        }
    instance.enqueue(content)
    print(
        content
    )


def remove(instance):
    if len(instance.queue) == 0:
        return print("Não há elementos")

    path_file = instance.dequeue()
    return print("Arquivo {} removido com sucesso".format(path_file['nome_do_arquivo']))

def file_metadata(instance, position):
    """Aqui irá sua implementação"""
