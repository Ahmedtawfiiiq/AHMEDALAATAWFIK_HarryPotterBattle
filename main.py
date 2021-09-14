import xml.etree.ElementTree as ET
from HarryPotter import HarryPotter
from Voldemort import Voldemort

# Related to XML file
data = ET.Element("MIA Game")
element1 = ET.SubElement(data, 'Opening')

harry_spell = None
voldemort_spell = None

one_player_voldemort = False
one_player_harry = False

# Low energy means the wizards has energy less than 20 and used all of his shields
# so that wizard can't cast any spell
low_Energy_Harry = False
low_Energy_Voldemort = False

winner_harry = False
winner_voldemort = False

# Creating Objects of wizards
wizard_harry = HarryPotter()
wizard_voldemort = Voldemort()


# Function which prints the winner name
def winner(name):
    print(f"\t\t{name} is the winner ..")
    s_elem5.set("type", f'{name}')
    s_elem5.text = f'{name} is the winner ..'


while True:

    # Voldemort only attacking
    if low_Energy_Harry:
        print("Enter one spell (voldemort)")
        one_player_voldemort = True
        voldemort_spell = input()
        wizard_voldemort.cast_spell(voldemort_spell)
        wizard_voldemort.one_player_standing(wizard_harry)

    # Harry only attacking
    if low_Energy_Voldemort:
        print("Enter one spell (harry)")
        one_player_harry = True
        harry_spell = input()
        wizard_harry.cast_spell(harry_spell)
        wizard_harry.one_player_standing(wizard_voldemort)

    # Normal case when both players are playing
    if not one_player_harry and not one_player_voldemort:
        print("Enter the two spells (harry then voldemort)")
        harry_spell, voldemort_spell = input().split()
        wizard_harry.cast_spell(harry_spell)
        wizard_voldemort.cast_spell(voldemort_spell)
        wizard_harry.two_players_game(wizard_voldemort)
        wizard_voldemort.two_players_game(wizard_harry)
        wizard_harry.reset_spell_energy()
        wizard_voldemort.reset_spell_energy()

    print('{:>19} {:>13}'.format(wizard_harry.get_name(), wizard_voldemort.get_name()))  # Printing start

    print(f"Health : {wizard_harry.get_health():<14} {wizard_voldemort.get_health()}")
    print(f"Energy : {wizard_harry.get_energy():<14} {wizard_voldemort.get_energy()}")

    s_elem1 = ET.SubElement(element1, f'{wizard_harry.get_name()}')
    s_elem2 = ET.SubElement(element1, f'{wizard_harry.get_name()}')

    s_elem1.set('type', 'Health')
    s_elem1.text = f'{wizard_harry.get_health()}'

    s_elem2.set('type', 'Energy')
    s_elem2.text = f'{wizard_harry.get_energy()}'

    s_elem3 = ET.SubElement(element1, f'{wizard_voldemort.get_name()}')
    s_elem4 = ET.SubElement(element1, f'{wizard_voldemort.get_name()}')

    s_elem3.set('type', 'Health')
    s_elem3.text = f'{wizard_voldemort.get_health()}'

    s_elem4.set('type', 'Energy')
    s_elem4.text = f'{wizard_voldemort.get_energy()}'

    s_elem5 = ET.SubElement(element1, "Winner")  # printing end

    if wizard_harry.get_energy() < 20 and wizard_harry.get_shields_number() == 0:  # Start of winning logic
        low_Energy_Harry = True

    if wizard_voldemort.get_energy() < 20 and wizard_voldemort.get_shields_number() == 0:
        low_Energy_Voldemort = True

    if wizard_harry.get_health() == 0:
        winner_voldemort = True

    if wizard_voldemort.get_health() == 0:
        winner_harry = True

    # If both harry and voldemort reach low energy case we decide the winner according to who has higher health
    if low_Energy_Harry and low_Energy_Voldemort:
        # If harry has higher health
        if wizard_harry.get_health() < wizard_voldemort.get_health():
            winner(wizard_voldemort.get_name())
            break
        # If voldemort has higher health
        elif wizard_harry.get_health() > wizard_voldemort.get_health():
            winner(wizard_harry.get_name())
            break
        # If both have the same health they reach Draw
        else:
            print("\t\tDraw ..")
            s_elem5.set("type", "Draw")
            s_elem5.text = 'Draw ..'
            break

    if winner_voldemort:
        winner(wizard_voldemort.get_name())
        break
    if winner_harry:
        winner(wizard_harry.get_name())
        break  # End of winning logic

# Related to XML file
b_xml = ET.tostring(data)
with open("MyXML.xml", "wb") as f:
    f.write(b_xml)
