class View(object):

    @staticmethod
    def show_start_print():
        print("==================================================================")
        print("================ Welcome to NOTES CONSOLE PROGRAM ================")
        print("==================================================================")

    @staticmethod
    def show_start_commands():
        print("Enable commands: \nadd    =  Создать заметку\n"
                                "read   =  Прочитать заметку\n"
                                "edit   =  Редактировать заметку\n"
                                "delete =  Удалить заметку\n"
                                "show   =  Показать список заметок\n"
                                "exit   =  Завершить программу\n")
    @staticmethod
    def show_add_command():
