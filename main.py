import sys
from termcolor import colored
from scripts import predict, train, update, compare


def main(argv):
    try:
        if argv == "-p" or argv == "predict":
            predict.predict_main()
            colored("Predictions are done!", "green")
        elif argv == "-t" or argv == "train":
            train.train_main()
            colored("Training is done!", "green")
            update.update()
            colored("Active AI updated!", "green")
        elif argv == "-c" or argv == "compare":
            compare.compare_main()
        elif argv == "-r" or argv == "restore":
            update.restore()
            colored("Restore is done!", "green")
        elif argv == "-u" or argv == "update":
            update.update()
            colored("Update is done!", "green")
        else:
            print("\nUse a command line argument to execute the specified action:\n"
                  "    -p: Make predictions\n"
                  "    -t: Train AI (AI has to be set active with -u)\n"
                  "    -c: Compare new trained and active AI performance\n"
                  "    -u: Use new trained AI\n"
                  "    -r: Restore old AI and discard AI currently in use\n")
    except ModuleNotFoundError as err:
        print(colored(f"error raised: {err}", "red"))
    finally:
        return


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            print(colored(f"{len(sys.argv) - 1} command-line argument found, "
                          "use --help for command-line arguments", "yellow"))
        else:
            main(sys.argv[1])
    except Exception as e:
        print(colored("An unexpected error occurred", "red"))
        print(e)
        print(colored("application crashed", "red"))
