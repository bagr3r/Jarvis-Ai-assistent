from core.router import process_command


class Jarvis:

    def run(self):

        print("Jarvis iniciado.")
        print("Digite 'sair' para encerrar.\n")

        while True:

            command = input("Você: ")

            if command.lower() == "sair":
                print("Jarvis encerrado.")
                break

            response = process_command(command)

            print(f"Jarvis: {response}")