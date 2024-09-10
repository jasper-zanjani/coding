/*
Generating a Dungeons 'n Dragons character provides the opportunity to exercise a variety of OOP techniques: 
public and private fields and properties and methods using simple arithmetic.

A Dungeons 'n Dragons character has six character attributes that can be randomly assigned.
This process, called an **ability roll**, is calculated by rolling four six-sided dice (d6) 
and summing the highest three values, discarding the lowest.
The raw ability score is then modified according to a [table](/Coding/DnD/#ability-modifiers) to produce a final ability score.

In the implementations below, all ability scores are dynamically calculated using getter functions that sum the raw ability score (stored as a private field) and modifier.
Both the ability roll and modifier lookup are implemented as public static functions.


*/

enum Race { 
    HUMAN, 
    ELF, 
    DWARF
};

class Warrior : public Player {
public:
Warrior(std::string n, Race r) : Player(n, r, 200, 0) {}
std::string attack() {return "I will destroy you with my sword, foul demon!";}
};

class Priest : public Player {
public:
Priest(std::string n, Race r) : Player(n, r, 100, 200) {}
std::string attack() {return "Taste the wrath of the Two True Gods!";}
};

class Mage : public Player {
public:
Mage(std::string n, Race r) : Player(n, r, 150, 150) {}
std::string attack() {return "You are overmatched by my esoteric artifices!";}
};

#include <string>

class Player {
protected:
std::string _name{ "Johnny Bravo" };
Race _race{Race::HUMAN };
int _hp{ 100 };
int _mp{ 100 };

public:
Player(std::string n, Race r, int hp, int mp) : _name{n}, _race{r}, _hp(hp), _mp(mp) {}
virtual std::string attack()= 0;
int getHp()                 { return _hp;   }
int getMp()                 { return _mp;   }

std::string getRace()              
{
    switch (_race)
    {
    case 0:
    return "human";
    break;
    
    case 1:
    return "elf";
    break;
    case 2:
    return "dwarf";
    break;

    default:
    return "none";
    break;
    }
}
std::string getName()       { return _name; }
void setHp(int n)           { _hp = n;   }
void setMp(int n)           { _mp = n;   }
void setName(std::string s) { _name = s; }
void setRace(Race r)        { _race = r;}
};