from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(
            mages: list[dict[str, Any]],
            min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    powers = list(map(lambda m: m['power'], mages))
    max_power = max(powers)
    min_power = min(powers)
    avg_power = round(sum(powers) / len(powers), 2)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
        }


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
        {
            'name': 'Crystal Orb',
            'power': 85,
            'type': 'focus'
        },
        {
            'name': 'Fire Staff',
            'power': 92,
            'type': 'weapon'
        }
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']}"
        f"({sorted_artifacts[0]['power']} power) comes before"
        f"{sorted_artifacts[1]['name']}"
        f"({sorted_artifacts[1]['power']} power)"
        )

    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    for spell in transformed:
        print(spell, end=' ')
    print()
