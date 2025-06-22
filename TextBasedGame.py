# Malik Spruill

game_title = '[Space Lover and the Saturn Stone]'
game_items = ('Fire Hose', 'Beak', 'Titanium Plate', 'Space-Bot Screen', 'Saturn Sack', 'Horned Skull')
move_commands = ('move North', 'move South', 'move East', 'move West')

def show_instructions():
    print(game_title)
    print(f'Collect {len(game_items)} items to win the game')
    print('Move commands:', end=' ')

    for index, move in enumerate(move_commands):
        if not (index == (len(move_commands) - 1)):
            print(f'{move} |', end=' ')
        else:
            print(move)
    print('How to add to Inventory, type: \'item name\'')
    print('Type \'Show Status\' to see current room, inventory, and the item in the current room if any')
    print('Type \'Show Instructions\' to see the instructions again')
    input('Tap enter to continue')
    return


def show_status(current_room, inventory, rooms):
    print(f'You are in the {current_room}.\n')
    print(f'Inventory: {inventory}')

    if 'item' in rooms[current_room]:
        print(f'Item in room: {rooms[current_room]["item"]}')  # could error
    else:
        print('No item in this room')

    input('Tap enter to continue')


def boss_fight_sequence(current_room, inventory):
    if (current_room == 'Great Room') and (len(inventory) == len(game_items)):
        print("""
            You've scanned for Los' weaknesses with the space-roaming bot's screen.
            Los smiles wickedly and unimpressed. While mocking you, you take the lava
            hose and melt the armor from Los' nickel neck-piece and pierce his neck with
            your found horned-skull.  Los jumps in the air, attempting to slash your head.
            You block with the titanium plate, blowing into the beak at close range, disorienting
            Los.  Then, you pierce Los again in the heart, destroying the monster and using the Saturn
            sack to obtain the Saturn stone.  You have won the game! Congratulations!
        """)
    else:
        print('You lose. Los notices your lack of confidence, and attacks your heart before remembering you have one')
    return


def game_sequence(current_room, inventory, rooms):
    item_in_room = False
    print(f'You are in the {current_room}.\n')
    print(f'Inventory: {inventory}')

    if current_room == 'Great Room':
        return boss_fight_sequence(current_room, inventory)

    if 'item' in rooms[current_room]:
        print(f'You\'re wandering and locate a {(rooms[current_room])["item"]}')
        print('----<>----<>----<>----<>----<>----')
        item_in_room = True

    user_choice = input(f'Check instructions, Show status, Or make a move.\n')

    if user_choice in rooms[current_room]:
        for room_keys in rooms[current_room]:
            if user_choice == room_keys:
                current_room = rooms[current_room][room_keys]
                print(f'After moving {user_choice}, you have now entered the {current_room}.')
                game_sequence(current_room, inventory, rooms)
    elif (item_in_room) and (user_choice == rooms[current_room]['item']):
        inventory.append(rooms[current_room]['item'])
        print(f'You\'ve now obtained {rooms[current_room]["item"]} Saturn cave dweller!')
        (rooms[current_room]).pop('item')

        if (len(inventory)) == (len(game_items)):
            print('You now have all of the resources you need to defeat Los!')
            print('Find the room the flesh and nickel monster is in and obtain the Saturn Stone to save your wife!')

        game_sequence(current_room, inventory, rooms)
    elif user_choice == 'Show Instructions':
        print('Pulling up instructions scroll\n')
        show_instructions()
        game_sequence(current_room, inventory, rooms)
    elif user_choice == 'Show Status':
        print('Pulling up status scanner now')
        show_status(current_room, inventory, rooms)
        game_sequence(current_room, inventory, rooms)
    else:
        print(f'This doesn\'t appear to be a choice in {current_room}.')
        print('Let\'s confirm which room you\'re in again and go from there.')
        game_sequence(current_room, inventory, rooms)


def main():
    rooms = {
        'Cave Entry Room': {move_commands[0]: 'The Room Above', move_commands[1]: 'Dark Hall',
                            move_commands[3]: 'Great Room'},
        'The Room Above': {move_commands[2]: 'Wind Room', move_commands[1]: 'Cave Entry Room', 'item': game_items[0]},
        'Wind Room': {move_commands[3]: 'The Room Above', 'item': game_items[1]},
        'Dark Hall': {move_commands[0]: 'Cave Entry Room', move_commands[1]: 'Fell Bones Room',
                      move_commands[2]: 'Room of Skin', move_commands[3]: 'Hallow Room', 'item': game_items[3]},
        'Room of Skin': {move_commands[3]: 'Dark Hall', 'item': game_items[4]},
        'Fell Bones Room': {move_commands[0]: 'Dark Hall', 'item': game_items[5]},
        'Hallow Room': {move_commands[0]: 'Great Room', move_commands[2]: 'Dark Hall', 'item': game_items[2]},
        'Great Room': {move_commands[2]: 'Cave Entry Room', move_commands[1]: 'Hallow Room'}
    }
    current_room = 'Cave Entry Room'
    inventory = []

    show_instructions()
    game_sequence(current_room, inventory, rooms)

    decided = False
    while not decided:
        decision = input('Would you like to play again? Type Yes or No')
        if decision == 'Yes':
            decided = True
            main()
        elif decision == 'No':
            print('Come back and play again soon!')
            decided = True
        else:
            print('You didn\'t choose Yes or No, try again.')
            continue
    return


main()
