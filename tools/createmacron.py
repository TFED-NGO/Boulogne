CHARACTERS_TO_CONVERT = [
    'N', 'm', 'r', 'h', 'p', 'd', 'g', 'c', 's', 't', 'l', 'n', 'b', 'q'
]

def main():
    with open('test.txt','w',encoding='utf-8-sig') as f:
        for char in CHARACTERS_TO_CONVERT:
            print(f'{char}\u0304',file=f)

if __name__ == '__main__':
    main()