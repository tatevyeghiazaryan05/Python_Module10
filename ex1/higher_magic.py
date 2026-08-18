from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
        ) -> Callable[[str, int], tuple[str, str]]:
    def combiner_spell(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return combiner_spell


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
        ) -> Callable[[str, int], str]:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
        ) -> Callable[[str, int], str]:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(
    spells: list[Callable[[str, int], str]]
        ) -> Callable[[str, int], list[str]]:
    def sequence_spell(target: str, power: int) -> list[str]:
        results: list[str] = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequence_spell


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon", 50)
    print(f"Combined spell result: {res1}, {res2}")
    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {mega_fireball('Dragon', 10)}")
    print("\nTesting conditional caster...")

    def is_strong_enough(target: str, power: int) -> bool:
        return power >= 20
    safe_fireball = conditional_caster(is_strong_enough, fireball)
    print(f"Power 30: {safe_fireball('Goblin', 30)}")
    print(f"Power 10: {safe_fireball('Goblin', 10)}")
    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, heal])
    print(f"Sequence results: {combo('Dragon', 20)}")
