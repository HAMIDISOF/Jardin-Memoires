def extraire_messages(page, session_name: str = "session") -> list[dict]:
    # ... (garder le début : JS_EXTRACT, etc.)

    # 1. Récupérer la hauteur totale
    print("⏳ Mesure de la hauteur totale...")
    total_height = page.evaluate(JS_SCROLL_HEIGHT)
    print(f"📏 Hauteur totale : {total_height} px")

    # 2. Se replacer en haut
    print("⏳ Retour en haut de la page...")
    page.evaluate(JS_SCROLL, 0)
    page.wait_for_timeout(1000)

    # 3. Capturer par bandes de 400 px (du haut vers le bas)
    bande = 400
    position = 0
    ordre = 0
    tous_items = []
    vus = set()

    # On ne fait que 4 cycles pour le test (tu pourras ajuster)
    cycles_max = 4
    cycle = 0

    while position < total_height and cycle < cycles_max:
        # Dérouler jusqu'à la position cible (facultatif, mais on peut juste prendre la position courante)
        page.evaluate(JS_SCROLL, position)
        page.wait_for_timeout(800)

        # Extraire les éléments visibles
        items_visibles = page.evaluate(JS_EXTRACT)

        for item in items_visibles:
            if not item["text"]:
                continue
            cle = (item["role"], item["type"], item["text"][:80])
            if cle not in vus:
                vus.add(cle)
                item["ordre"] = ordre
                item["scroll_pos"] = position
                tous_items.append(item)
                ordre += 1

        print(f"Cycle {cycle+1}: position {position} px, {len(tous_items)} éléments accumulés")

        # Passer à la bande suivante
        position += bande
        cycle += 1

    # ... ensuite, le tri et la reconstruction des messages
    # (conserver le code existant après la capture)