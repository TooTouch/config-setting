import argparse


parser = argparse.ArgumentParser(description='argparse example')
parser.add_argument('filepath', type=str, help='file path')
parser.add_argument('-n', '--name', metavar='str', type=str, default='test', help='exp name')
parser.add_argument('-v', '--value', metavar='int', type=int, default=223, help='value')
parser.add_argument('--is_use', action='store_true', help='whether use or not')
parser.add_argument('-s', '--select_type', type=str, choices=['a','b','c'], help='select type')
parser.add_argument('-m', '--model', type=str, required=True, help='model name')
parser.add_argument('nb_run', type=int, help='the number of run')
parser.add_argument('-c', '--case', metavar='case list', type=str, nargs='+', help='case list')
args = parser.parse_args()

print('args:', args)

print('filepath: ',args.filepath)
print('nb_run: ',args.nb_run)
print('args.name: ',args.name)
 