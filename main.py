Test python env

def print_hello():
    animals = ['dog', 'cat','hamster','tiger'] #in one line
    foods = [
	'burgers',
	'salad',
	'taco'
	] #without trailing comma
    names = [
	'John',
	'Jane',
	'Gil-dong',
	'Dong-Eun',
	] #with trailing comma
    for f_name in names:
	print(f'hello, {f_name}')
    print('hello')

if __name__ == '__main__':
    print_hello()

