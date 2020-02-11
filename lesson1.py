def step1():
    print(
        '\nПривет! Меня зовут Нора, мне 7 и я потерялась. '
        'Мама и папа куда-то ушли... Надо их найти. \n'
        'Торговый центр такой большой и страшный... '
        'Куда пойти в первую очередь? \n'
    )
    options = {'1': '1. Папа был голодный, может, они в кафе?',
               '2': '2. Наверное остались в магазине игрушек, пойду туда.',
               '3': '3. Мама выглядела уставшей... Надо проверить бар.'}

    for option, value in options.items():
        print(value)

    next_step = ''
    while not next_step:
        print('(пожалуйста, введите номер ответа):\n')
        answer = input()
        next_step = options.get(answer, False)

    if answer == '1':
        return goto_cafe()
    elif answer == '2':
        return goto_shop()
    else:
        return goto_bar()


def goto_cafe():
    print('Кажется, звучит логично, тоже хочется кушать... '
          'Куда бы они могли пойти?\n')
    options_21 = {'1': '1. В макдональдс! Там игрушки с покемонами...',
                  '2': '2. В тот японский ресторанчик, куда мы обычно ходим есть суши?',
                  '3': '3. В чайхону?'}

    for option, value in options_21.items():
        print(value)

    next_step = ''
    while not next_step:
        print('(пожалуйста, введите номер ответа):\n')
        answer = input()
        next_step = options_21.get(answer, False)
        if answer == '1':
            print('Тут полно народу, но мамы с папой нигде не видно... Попробую еще раз')
            next_step = ''
        elif answer == '2':
            print('В японском ресторанчике тетенька на входе сказала, '
                  'что мест не было и мама и папа пошли в бар напротив... '
                  'Надо посмотреть там')
            return goto_bar()
        elif answer == '3':
            print('Кальян воняет отвратительно, и у мамы на него аллергия... Надо проверить что-то еще')
            next_step = ''


def goto_shop():
    print('zhopa2')
    return


def goto_bar():
    print('zhopa3')
    return


#if name == '__main__':
step1()









