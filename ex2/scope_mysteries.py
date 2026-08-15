from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    def added(amount: int) -> int:
        nonlocal initial_power
        initial_power += amount
        return initial_power
    return added


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def text_maker(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return text_maker


def memory_vault() -> dict[str, Callable[..., Any]]:
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        if key not in vault:
            return "Memory not found"
        return vault[key]
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print()
    print("Testing spell accumulator...")
    speling = spell_accumulator(100)
    print(f"Base 100, add 20: {speling(20)}")
    print(f"Base 100, add 30: {speling(30)}")
    print()
    print("Testing enchantment factory...")
    flameling = enchantment_factory("Flaming")
    print(flameling("Sword"))
    frozen = enchantment_factory("Frozen")
    print(frozen("Shield"))
    print()
    print("Testing memory vault...")
    mem = memory_vault()
    store_fn = mem["store"]
    recall_fn = mem["recall"]
    print("Store 'secret' = 42")
    store_fn("secret", 42)
    print(f"Recall 'secret': {recall_fn("secret")}")
    print(f"Recall 'unknown': {recall_fn("unknown")}")
