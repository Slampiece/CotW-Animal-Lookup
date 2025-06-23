def format_animal(name, data):
    output = []
    output.append(f"Animal Name: {data['animal_name']} ({data['wiki_url']})")
    output.append(f"Class: {data['class']}")
    output.append(f"Level Range: {data['level_range']}")

    output.append("\nFur Types:")
    for fur in data["fur_types"]:
        output.append(fur)

    output.append(f"\nSilver: {data['silver']}")
    output.append(f"Gold: {data['gold']}")
    output.append(f"Diamond: {data['diamond']}")
    output.append(f"\nGreat One: {'Yes' if data['great_one'] else 'No'}")

    output.append(f"\nMax Weight (KG): {data['max_weight_kg']}")
    output.append(f"Max Weight (LBs): {data['max_weight_lbs']}")

    output.append("\nReserves:")
    for res in data["reserves"]:
        output.append(f"{res['Name']} ({res['MapURL']})")

    output.append("\nNeed Zones:")
    for zone in data["need_zones"]:
        output.append(zone)

    output.append("\nPHASE STRATEGY (ANCHOR SYSTEM):")
    output.append("\n• Phase 1 –")
    for line in data["phase_strategy"]["Phase 1"].split("\n"):
        output.append(line)

    output.append("\n• Phase 2 –")
    for line in data["phase_strategy"]["Phase 2"].split("\n"):
        output.append(line)

    return "\n".join(output)
