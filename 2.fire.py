import fire

def run(
    name: str = "test", 
    case: list = ['a','b'], 
    params: dict = {},
    is_use: bool = False
):
    print(f'name: {name}, type: {type(name)}')
    print(f'case: {case}, type: {type(case)}')
    print(f'params: {params}, type: {type(params)}')
    print(f'is_use: {is_use}, type: {type(is_use)}')

if __name__ == '__main__':
    fire.Fire(run)