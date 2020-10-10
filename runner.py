import argparse


def main(args):
    print(args.serial)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
    parser.add_argument('-s', '--serial', help='phone serial number')
    parser.add_argument('-h', '--high', default='high', help='high/low performance phone')
    main(parser.parse_args())
