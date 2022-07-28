from argparse import ArgumentParser

def myfunc(msg):
    print(msg)

if __name__ == '__main__':
    print("인터프리터로 사용됨")
    print(__name__)
    parser = ArgumentParser()
    parser.add_argument("--msg", type=str, required=True, help="Path to the directory containing recordings to be trained on")
    args = parser.parse_args()
    myfunc(args.msg)

else:
    print("임포트되어 사용됨")
    print(__name__)