partial class Character
{
    private int StrengthAbility;
    private int DexterityAbility;
    private int ConstitutionAbility;
    private int IntelligenceAbility;
    private int WisdomAbility;
    private int CharismaAbility;
    private Race Race { get; }

    public Character(Race race)
    {
        this.StrengthAbility = AbilityRoll();
        this.DexterityAbility = AbilityRoll();
        this.ConstitutionAbility = AbilityRoll();
        this.IntelligenceAbility = AbilityRoll();
        this.WisdomAbility = AbilityRoll();
        this.CharismaAbility = AbilityRoll();
        this.Race = race;
    }

    public Character() : this(Race.HUMAN) { }
}

partial class Character
{
    public int Strength     
    { 
        get => StrengthAbility + GetModifier(StrengthAbility) + GetRaceModifier(Abilities.STRENGTH) 
    }
    
    public int Dexterity    
    { 
        get => DexterityAbility + GetModifier(DexterityAbility) + GetRaceModifier(Abilities.DEXTERITY) 
    }
    
    public int Constitution 
    { 
        get => ConstitutionAbility + GetModifier(ConstitutionAbility) + GetRaceModifier(Abilities.CONSTITUTION) 
    }
    
    public int Intelligence 
    { 
        get => IntelligenceAbility + GetModifier(IntelligenceAbility) + GetRaceModifier(Abilities.INTELLIGENCE) 
    }
    
    public int Wisdom       
    { 
        get => WisdomAbility + GetModifier(WisdomAbility) + GetRaceModifier(Abilities.WISDOM) 
    }
    
    public int Charisma     
    { 
        get => CharismaAbility + GetModifier(CharismaAbility) + GetRaceModifier(Abilities.CHARISMA) 
    }
}

partial class Character
{
    public void Report()
    {
        Console.Write($"Strength: {Strength,2}");
        Console.Write($"Dexterity: {Dexterity,2}");
        Console.Write($"Constitution: {Constitution,2}");
        Console.Write($"Intelligence: {Intelligence,2}");
        Console.Write($"Wisdom: {Wisdom,2}");
        Console.Write($"Charisma: {Charisma,2}");
    }

    static int Roll(int ceiling)
    {
        Random rng = new Random();
        return rng.Next(1, ceiling);
    }

    static int AbilityRoll()
    {
        List<int> rolls = new List<int> { Roll(6), Roll(6), Roll(6), Roll(6) };
        rolls.Remove(rolls.Min());

        return rolls.Sum();
    }

    public static int GetModifier(int ability)
    {
        return (int)System.Math.Floor(((double)ability - 10) / 2);
    }
}