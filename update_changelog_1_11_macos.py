#!/usr/bin/env python3
"""
Update 1.11.0-macos.json for all languages based on English version only.
"""

import json
from pathlib import Path

# Complete translations based on English version
changelog_by_locale = {
    'en': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Unified Subscription for Full Access",
        "meta_title": "Unified Subscription for Full Access - Frames",
        "meta_description": "macOS app now included with iOS subscription at no extra cost. Unified pricing lets you use all Frames features on iPhone and Mac.",
        "summary": "The Mac app is now integrated into your iOS subscription, unifying the Frames ecosystem for easier access and management across devices.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Unified Pricing for the Frames Ecosystem"
            },
            {
                "type": "paragraph",
                "content": "Based on feedback from the analog photography community, I've refined the pricing model. The Mac app no longer requires a separate subscription, it's now included with your iOS subscription at no extra cost. This unification makes it simpler to enjoy the complete Frames experience, from noting film details on iOS to integrating metadata into scanned images on Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Apple purchase icon representing the new Frames film photography app lifetime plan option",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Sidebar Polish"
            },
            {
                "type": "paragraph",
                "content": "The sidebar has been updated with improved colors that provide better contrast, making it easier to read and navigate your film metadata. Small change, but it makes a noticeable difference when you're working through your archive."
            }
        ],
        "improvements": [
            "Mac app now included with iOS subscription at no extra cost",
            "Improved sidebar colors for better contrast and readability",
            "Minor interface refinements"
        ],
        "fixes": [],
        "patches": []
    },
    'de': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Einheitliches Abo für vollen Zugriff",
        "meta_title": "Einheitliches Abo für vollen Zugriff - Frames",
        "meta_description": "Die macOS-App ist jetzt ohne Aufpreis im iOS-Abo enthalten. Einheitliche Preise ermöglichen die Nutzung aller Frames-Funktionen auf iPhone und Mac.",
        "summary": "Die Mac-App ist jetzt in Ihr iOS-Abo integriert und vereint das Frames-Ökosystem für einfacheren Zugriff und Verwaltung auf allen Geräten.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Einheitliche Preisgestaltung für das Frames-Ökosystem"
            },
            {
                "type": "paragraph",
                "content": "Basierend auf Feedback aus der analogen Fotografie-Community habe ich das Preismodell überarbeitet. Die Mac-App benötigt kein separates Abo mehr, sie ist jetzt ohne Aufpreis in Ihrem iOS-Abo enthalten. Diese Vereinheitlichung macht es einfacher, die komplette Frames-Erfahrung zu genießen – vom Notieren der Filmdetails unter iOS bis zur Integration von Metadaten in gescannte Bilder auf dem Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Apple-Kaufsymbol für die neue Frames Filmfotografie-App Lifetime-Plan-Option",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Verfeinerung der Seitenleiste"
            },
            {
                "type": "paragraph",
                "content": "Die Seitenleiste wurde mit verbesserten Farben aktualisiert, die einen besseren Kontrast bieten und das Lesen und Navigieren Ihrer Film-Metadaten erleichtern. Eine kleine Änderung, die aber einen spürbaren Unterschied macht, wenn Sie Ihr Archiv durcharbeiten."
            }
        ],
        "improvements": [
            "Mac-App jetzt ohne Aufpreis im iOS-Abo enthalten",
            "Verbesserte Farben der Seitenleiste für besseren Kontrast und Lesbarkeit",
            "Kleinere Interface-Verfeinerungen"
        ],
        "fixes": [],
        "patches": []
    },
    'fr': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Abonnement unifié pour un accès complet",
        "meta_title": "Abonnement unifié pour un accès complet - Frames",
        "meta_description": "L'app macOS est maintenant incluse dans l'abonnement iOS sans frais supplémentaires. Tarification unifiée pour utiliser toutes les fonctionnalités de Frames sur iPhone et Mac.",
        "summary": "L'app Mac est désormais intégrée à votre abonnement iOS, unifiant l'écosystème Frames pour un accès et une gestion plus faciles sur tous les appareils.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Tarification unifiée pour l'écosystème Frames"
            },
            {
                "type": "paragraph",
                "content": "Sur la base des retours de la communauté de la photographie analogique, j'ai affiné le modèle tarifaire. L'app Mac ne nécessite plus d'abonnement séparé, elle est maintenant incluse dans votre abonnement iOS sans frais supplémentaires. Cette unification rend plus simple de profiter de l'expérience complète de Frames, de la notation des détails de pellicule sur iOS à l'intégration des métadonnées dans les images scannées sur Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Icône d'achat Apple représentant la nouvelle option de plan à vie de l'app de photographie argentique Frames",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Amélioration de la barre latérale"
            },
            {
                "type": "paragraph",
                "content": "La barre latérale a été mise à jour avec des couleurs améliorées qui offrent un meilleur contraste, facilitant la lecture et la navigation de vos métadonnées de pellicule. Petit changement, mais qui fait une différence notable lorsque vous parcourez votre archive."
            }
        ],
        "improvements": [
            "App Mac maintenant incluse dans l'abonnement iOS sans frais supplémentaires",
            "Couleurs de la barre latérale améliorées pour un meilleur contraste et lisibilité",
            "Améliorations mineures de l'interface"
        ],
        "fixes": [],
        "patches": []
    },
    'it': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Abbonamento unificato per l'accesso completo",
        "meta_title": "Abbonamento unificato per l'accesso completo - Frames",
        "meta_description": "L'app macOS è ora inclusa nell'abbonamento iOS senza costi aggiuntivi. Prezzo unificato per utilizzare tutte le funzionalità di Frames su iPhone e Mac.",
        "summary": "L'app Mac è ora integrata nel tuo abbonamento iOS, unificando l'ecosistema Frames per un accesso e una gestione più semplici su tutti i dispositivi.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Prezzo unificato per l'ecosistema Frames"
            },
            {
                "type": "paragraph",
                "content": "Sulla base dei feedback dalla comunità della fotografia analogica, ho perfezionato il modello di prezzo. L'app Mac non richiede più un abbonamento separato, è ora inclusa nel tuo abbonamento iOS senza costi aggiuntivi. Questa unificazione rende più semplice godere dell'esperienza completa di Frames, dall'annotazione dei dettagli della pellicola su iOS all'integrazione dei metadati nelle immagini scansionate su Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Icona di acquisto Apple che rappresenta la nuova opzione di piano a vita dell'app di fotografia analogica Frames",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Miglioramento della barra laterale"
            },
            {
                "type": "paragraph",
                "content": "La barra laterale è stata aggiornata con colori migliorati che forniscono un contrasto migliore, rendendo più facile leggere e navigare i tuoi metadati della pellicola. Un piccolo cambiamento, ma che fa una differenza notevole quando lavori attraverso il tuo archivio."
            }
        ],
        "improvements": [
            "App Mac ora inclusa nell'abbonamento iOS senza costi aggiuntivi",
            "Colori della barra laterale migliorati per un contrasto e una leggibilità migliori",
            "Perfezionamenti minori dell'interfaccia"
        ],
        "fixes": [],
        "patches": []
    },
    'pt': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Assinatura unificada para acesso completo",
        "meta_title": "Assinatura unificada para acesso completo - Frames",
        "meta_description": "O app macOS agora está incluído na assinatura iOS sem custo adicional. Preço unificado permite usar todos os recursos do Frames no iPhone e Mac.",
        "summary": "O app Mac agora está integrado à sua assinatura iOS, unificando o ecossistema Frames para acesso e gerenciamento mais fáceis em todos os dispositivos.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Preço unificado para o ecossistema Frames"
            },
            {
                "type": "paragraph",
                "content": "Com base no feedback da comunidade de fotografia analógica, refinei o modelo de preços. O app Mac não requer mais uma assinatura separada, agora está incluído na sua assinatura iOS sem custo adicional. Esta unificação torna mais simples aproveitar a experiência completa do Frames, desde anotar detalhes do filme no iOS até integrar metadados em imagens digitalizadas no Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Ícone de compra da Apple representando a nova opção de plano vitalício do app de fotografia analógica Frames",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Aprimoramento da barra lateral"
            },
            {
                "type": "paragraph",
                "content": "A barra lateral foi atualizada com cores aprimoradas que fornecem melhor contraste, facilitando a leitura e navegação dos seus metadados de filme. Pequena mudança, mas que faz uma diferença notável quando você está trabalhando no seu arquivo."
            }
        ],
        "improvements": [
            "App Mac agora incluído na assinatura iOS sem custo adicional",
            "Cores da barra lateral aprimoradas para melhor contraste e legibilidade",
            "Refinamentos menores da interface"
        ],
        "fixes": [],
        "patches": []
    },
    'es': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Suscripción unificada para acceso completo",
        "meta_title": "Suscripción unificada para acceso completo - Frames",
        "meta_description": "La app de macOS ahora está incluida en la suscripción de iOS sin costo adicional. Precio unificado para usar todas las funciones de Frames en iPhone y Mac.",
        "summary": "La app de Mac ahora está integrada en tu suscripción de iOS, unificando el ecosistema de Frames para un acceso y gestión más fáciles en todos los dispositivos.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Precio unificado para el ecosistema Frames"
            },
            {
                "type": "paragraph",
                "content": "Basándome en los comentarios de la comunidad de fotografía analógica, he refinado el modelo de precios. La app de Mac ya no requiere una suscripción separada, ahora está incluida en tu suscripción de iOS sin costo adicional. Esta unificación hace más simple disfrutar de la experiencia completa de Frames, desde anotar detalles de película en iOS hasta integrar metadatos en imágenes escaneadas en Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Icono de compra de Apple que representa la nueva opción de plan de por vida de la app de fotografía analógica Frames",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Mejora de la barra lateral"
            },
            {
                "type": "paragraph",
                "content": "La barra lateral se ha actualizado con colores mejorados que proporcionan mejor contraste, facilitando la lectura y navegación de tus metadatos de película. Un pequeño cambio, pero que marca una diferencia notable cuando trabajas en tu archivo."
            }
        ],
        "improvements": [
            "App de Mac ahora incluida en la suscripción de iOS sin costo adicional",
            "Colores de la barra lateral mejorados para mejor contraste y legibilidad",
            "Refinamientos menores de la interfaz"
        ],
        "fixes": [],
        "patches": []
    }
}

# Continue with remaining languages...
changelog_by_locale.update({
    'nl': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Geünificeerd abonnement voor volledige toegang",
        "meta_title": "Geünificeerd abonnement voor volledige toegang - Frames",
        "meta_description": "De macOS-app is nu inbegrepen bij het iOS-abonnement zonder extra kosten. Geünificeerde prijzen voor alle Frames-functies op iPhone en Mac.",
        "summary": "De Mac-app is nu geïntegreerd in je iOS-abonnement, waardoor het Frames-ecosysteem wordt verenigd voor gemakkelijkere toegang en beheer op alle apparaten.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Geünificeerde prijzen voor het Frames-ecosysteem"
            },
            {
                "type": "paragraph",
                "content": "Op basis van feedback van de analoge fotografiegemeenschap heb ik het prijsmodel verfijnd. De Mac-app vereist geen apart abonnement meer, deze is nu zonder extra kosten inbegrepen bij je iOS-abonnement. Deze eenwording maakt het eenvoudiger om de volledige Frames-ervaring te genieten, van het noteren van filmdetails op iOS tot het integreren van metadata in gescande afbeeldingen op Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Apple aankooppictogram voor de nieuwe Frames filmfotografie-app levenslange optie",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Verfijning van de zijbalk"
            },
            {
                "type": "paragraph",
                "content": "De zijbalk is bijgewerkt met verbeterde kleuren die beter contrast bieden, waardoor je filmmetadata gemakkelijker te lezen en navigeren is. Een kleine verandering, maar die een merkbaar verschil maakt wanneer je door je archief werkt."
            }
        ],
        "improvements": [
            "Mac-app nu zonder extra kosten inbegrepen bij iOS-abonnement",
            "Verbeterde kleuren van de zijbalk voor beter contrast en leesbaarheid",
            "Kleine interface-verfijningen"
        ],
        "fixes": [],
        "patches": []
    },
    'sv': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Enhetlig prenumeration för full åtkomst",
        "meta_title": "Enhetlig prenumeration för full åtkomst - Frames",
        "meta_description": "macOS-appen ingår nu i iOS-prenumerationen utan extra kostnad. Enhetlig prissättning för alla Frames-funktioner på iPhone och Mac.",
        "summary": "Mac-appen är nu integrerad i din iOS-prenumeration, vilket förenar Frames-ekosystemet för enklare åtkomst och hantering på alla enheter.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Enhetlig prissättning för Frames-ekosystemet"
            },
            {
                "type": "paragraph",
                "content": "Baserat på feedback från den analoga fotografigemenskapen har jag förfinat prismodellen. Mac-appen kräver inte längre en separat prenumeration, den ingår nu i din iOS-prenumeration utan extra kostnad. Denna förenkling gör det enklare att njuta av den kompletta Frames-upplevelsen, från att notera filmdetaljer på iOS till att integrera metadata i skannade bilder på Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Apple-köpikon som representerar det nya livstidsalternativet för Frames filmfotografiapp",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Förbättrad sidopanel"
            },
            {
                "type": "paragraph",
                "content": "Sidopanelen har uppdaterats med förbättrade färger som ger bättre kontrast, vilket gör det lättare att läsa och navigera din filmmetadata. Liten förändring, men den gör en märkbar skillnad när du arbetar genom ditt arkiv."
            }
        ],
        "improvements": [
            "Mac-appen ingår nu i iOS-prenumerationen utan extra kostnad",
            "Förbättrade färger i sidopanelen för bättre kontrast och läsbarhet",
            "Mindre gränssnittsförbättringar"
        ],
        "fixes": [],
        "patches": []
    },
    'da': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Samlet abonnement til fuld adgang",
        "meta_title": "Samlet abonnement til fuld adgang - Frames",
        "meta_description": "macOS-appen er nu inkluderet i iOS-abonnementet uden ekstra omkostning. Samlet prissætning for alle Frames-funktioner på iPhone og Mac.",
        "summary": "Mac-appen er nu integreret i dit iOS-abonnement, hvilket forener Frames-økosystemet for lettere adgang og administration på tværs af enheder.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Samlet prissætning for Frames-økosystemet"
            },
            {
                "type": "paragraph",
                "content": "Baseret på feedback fra det analoge fotografifællesskab har jeg forfinet prismodellen. Mac-appen kræver ikke længere et separat abonnement, den er nu inkluderet i dit iOS-abonnement uden ekstra omkostning. Denne forening gør det simplere at nyde den komplette Frames-oplevelse, fra at notere filmdetaljer på iOS til at integrere metadata i scannede billeder på Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Apple købsikon der repræsenterer den nye livstidsmulighed for Frames filmfotografiapp",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Forbedret sidepanel"
            },
            {
                "type": "paragraph",
                "content": "Sidepanelet er blevet opdateret med forbedrede farver, der giver bedre kontrast, hvilket gør det lettere at læse og navigere dine filmmetadata. Lille ændring, men den gør en mærkbar forskel, når du arbejder gennem dit arkiv."
            }
        ],
        "improvements": [
            "Mac-appen er nu inkluderet i iOS-abonnementet uden ekstra omkostning",
            "Forbedrede sidepanelfarver for bedre kontrast og læsbarhed",
            "Mindre grænsefladeforbedringer"
        ],
        "fixes": [],
        "patches": []
    },
    'nb': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Samlet abonnement for full tilgang",
        "meta_title": "Samlet abonnement for full tilgang - Frames",
        "meta_description": "macOS-appen er nå inkludert i iOS-abonnementet uten ekstra kostnad. Samlet prissetting for alle Frames-funksjoner på iPhone og Mac.",
        "summary": "Mac-appen er nå integrert i ditt iOS-abonnement, noe som forener Frames-økosystemet for enklere tilgang og administrasjon på tvers av enheter.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Samlet prissetting for Frames-økosystemet"
            },
            {
                "type": "paragraph",
                "content": "Basert på tilbakemeldinger fra det analoge fotografimiljøet har jeg forbedret prismodellen. Mac-appen krever ikke lenger et separat abonnement, den er nå inkludert i ditt iOS-abonnement uten ekstra kostnad. Denne samlingen gjør det enklere å nyte den komplette Frames-opplevelsen, fra å notere filmdetaljer på iOS til å integrere metadata i skannede bilder på Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Apple kjøpsikon som representerer det nye livstidsalternativet for Frames filmfotografiapp",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Forbedret sidepanel"
            },
            {
                "type": "paragraph",
                "content": "Sidepanelet har blitt oppdatert med forbedrede farger som gir bedre kontrast, noe som gjør det lettere å lese og navigere filmmetadataene dine. Liten endring, men den gjør en merkbar forskjell når du arbeider gjennom arkivet ditt."
            }
        ],
        "improvements": [
            "Mac-appen er nå inkludert i iOS-abonnementet uten ekstra kostnad",
            "Forbedrede sidepanelfarger for bedre kontrast og lesbarhet",
            "Mindre grensesnittforbedringer"
        ],
        "fixes": [],
        "patches": []
    },
    'fi': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Yhdistetty tilaus täyteen pääsyyn",
        "meta_title": "Yhdistetty tilaus täyteen pääsyyn - Frames",
        "meta_description": "macOS-sovellus nyt mukana iOS-tilauksessa ilman lisäkustannuksia. Yhdistetty hinnoittelu kaikkiin Frames-ominaisuuksiin iPhonessa ja Macissa.",
        "summary": "Mac-sovellus on nyt integroitu iOS-tilaukseesi, yhdistäen Frames-ekosysteemin helpompaan pääsyyn ja hallintaan kaikilla laitteilla.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Yhdistetty hinnoittelu Frames-ekosysteemille"
            },
            {
                "type": "paragraph",
                "content": "Analogisen valokuvausyhteisön palautteen perusteella olen hionut hinnoittelumallia. Mac-sovellus ei enää vaadi erillistä tilausta, vaan se sisältyy nyt iOS-tilaukseesi ilman lisäkustannuksia. Tämä yhdistäminen tekee helpommaksi nauttia täydestä Frames-kokemuksesta, filmin yksityiskohtien merkitsemisestä iOS:llä metatietojen integrointiin skannattuihin kuviin Macilla."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Applen ostokuvake, joka edustaa uutta Frames-filmivalokuvaussovelluksen elinikäistä vaihtoehtoa",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Sivupalkin parannukset"
            },
            {
                "type": "paragraph",
                "content": "Sivupalkki on päivitetty paremmilla väreillä, jotka tarjoavat paremman kontrastin, tehden filmin metatietojen lukemisesta ja selailusta helpompaa. Pieni muutos, mutta se tekee huomattavan eron, kun käyt läpi arkistoasi."
            }
        ],
        "improvements": [
            "Mac-sovellus nyt mukana iOS-tilauksessa ilman lisäkustannuksia",
            "Parannetut sivupalkin värit paremman kontrastin ja luettavuuden saavuttamiseksi",
            "Pieniä käyttöliittymäparannuksia"
        ],
        "fixes": [],
        "patches": []
    }
})

# Adding Slavic languages
changelog_by_locale.update({
    'pl': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Zunifikowana subskrypcja dla pełnego dostępu",
        "meta_title": "Zunifikowana subskrypcja dla pełnego dostępu - Frames",
        "meta_description": "Aplikacja macOS jest teraz dołączona do subskrypcji iOS bez dodatkowych kosztów. Ujednolicone ceny pozwalają korzystać ze wszystkich funkcji Frames na iPhone i Mac.",
        "summary": "Aplikacja Mac jest teraz zintegrowana z subskrypcją iOS, unifikując ekosystem Frames dla łatwiejszego dostępu i zarządzania na wszystkich urządzeniach.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Ujednolicone ceny dla ekosystemu Frames"
            },
            {
                "type": "paragraph",
                "content": "Na podstawie opinii społeczności fotografii analogowej udoskonaliłem model cenowy. Aplikacja Mac nie wymaga już osobnej subskrypcji, jest teraz dołączona do subskrypcji iOS bez dodatkowych kosztów. Ta unifikacja ułatwia korzystanie z pełnego doświadczenia Frames, od notowania szczegółów filmu w iOS po integrację metadanych w zeskanowanych obrazach na Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Ikona zakupu Apple reprezentująca nową opcję planu dożywotniego aplikacji fotografii analogowej Frames",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Udoskonalenie paska bocznego"
            },
            {
                "type": "paragraph",
                "content": "Pasek boczny został zaktualizowany o ulepszone kolory zapewniające lepszy kontrast, co ułatwia czytanie i nawigację metadanych filmu. Niewielka zmiana, ale robi zauważalną różnicę podczas pracy z archiwum."
            }
        ],
        "improvements": [
            "Aplikacja Mac teraz dołączona do subskrypcji iOS bez dodatkowych kosztów",
            "Ulepszone kolory paska bocznego dla lepszego kontrastu i czytelności",
            "Drobne udoskonalenia interfejsu"
        ],
        "fixes": [],
        "patches": []
    },
    'ru': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Единая подписка для полного доступа",
        "meta_title": "Единая подписка для полного доступа - Frames",
        "meta_description": "Приложение macOS теперь включено в подписку iOS без дополнительной платы. Единая цена для использования всех функций Frames на iPhone и Mac.",
        "summary": "Приложение Mac теперь интегрировано в вашу подписку iOS, объединяя экосистему Frames для более простого доступа и управления на всех устройствах.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Единая цена для экосистемы Frames"
            },
            {
                "type": "paragraph",
                "content": "На основе отзывов сообщества аналоговой фотографии я усовершенствовал модель ценообразования. Приложению Mac больше не требуется отдельная подписка, теперь оно включено в вашу подписку iOS без дополнительной платы. Это объединение упрощает наслаждение полным опытом Frames, от записи деталей плёнки в iOS до интеграции метаданных в отсканированные изображения на Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Иконка покупки Apple, представляющая новую опцию пожизненного плана приложения для плёночной фотографии Frames",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Улучшение боковой панели"
            },
            {
                "type": "paragraph",
                "content": "Боковая панель была обновлена улучшенными цветами, которые обеспечивают лучший контраст, облегчая чтение и навигацию метаданных плёнки. Небольшое изменение, но оно заметно улучшает работу с архивом."
            }
        ],
        "improvements": [
            "Приложение Mac теперь включено в подписку iOS без дополнительной платы",
            "Улучшенные цвета боковой панели для лучшего контраста и читаемости",
            "Незначительные улучшения интерфейса"
        ],
        "fixes": [],
        "patches": []
    },
    'uk': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Єдина підписка для повного доступу",
        "meta_title": "Єдина підписка для повного доступу - Frames",
        "meta_description": "Додаток macOS тепер включений у підписку iOS без додаткової плати. Єдина ціна для використання всіх функцій Frames на iPhone і Mac.",
        "summary": "Додаток Mac тепер інтегровано у вашу підписку iOS, об'єднуючи екосистему Frames для простішого доступу та керування на всіх пристроях.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Єдина ціна для екосистеми Frames"
            },
            {
                "type": "paragraph",
                "content": "На основі відгуків спільноти аналогової фотографії я вдосконалив модель ціноутворення. Додатку Mac більше не потрібна окрема підписка, тепер він включений у вашу підписку iOS без додаткової плати. Це об'єднання спрощує насолоду повним досвідом Frames, від запису деталей плівки в iOS до інтеграції метаданих у відскановані зображення на Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Іконка покупки Apple, що представляє нову опцію довічного плану додатка для плівкової фотографії Frames",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Поліпшення бічної панелі"
            },
            {
                "type": "paragraph",
                "content": "Бічну панель оновлено поліпшеними кольорами, які забезпечують кращий контраст, полегшуючи читання та навігацію метаданих плівки. Невелика зміна, але вона помітно покращує роботу з архівом."
            }
        ],
        "improvements": [
            "Додаток Mac тепер включений у підписку iOS без додаткової плати",
            "Поліпшені кольори бічної панелі для кращого контрасту та читабельності",
            "Незначні поліпшення інтерфейсу"
        ],
        "fixes": [],
        "patches": []
    },
    'ro': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Abonament unificat pentru acces complet",
        "meta_title": "Abonament unificat pentru acces complet - Frames",
        "meta_description": "Aplicația macOS este acum inclusă în abonamentul iOS fără cost suplimentar. Preț unificat pentru toate funcțiile Frames pe iPhone și Mac.",
        "summary": "Aplicația Mac este acum integrată în abonamentul iOS, unificând ecosistemul Frames pentru acces și gestionare mai ușoare pe toate dispozitivele.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Preț unificat pentru ecosistemul Frames"
            },
            {
                "type": "paragraph",
                "content": "Pe baza feedback-ului din comunitatea fotografiei analogice, am rafinat modelul de preț. Aplicația Mac nu mai necesită un abonament separat, este acum inclusă în abonamentul iOS fără cost suplimentar. Această unificare face mai simplă bucuria experienței complete Frames, de la notarea detaliilor filmului pe iOS la integrarea metadatelor în imaginile scanate pe Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Pictogramă de achiziție Apple reprezentând noua opțiune de plan pe viață a aplicației de fotografie analogică Frames",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Îmbunătățire bară laterală"
            },
            {
                "type": "paragraph",
                "content": "Bara laterală a fost actualizată cu culori îmbunătățite care oferă contrast mai bun, facilitând citirea și navigarea metadatelor de film. Schimbare mică, dar face o diferență notabilă când lucrați prin arhivă."
            }
        ],
        "improvements": [
            "Aplicația Mac acum inclusă în abonamentul iOS fără cost suplimentar",
            "Culori îmbunătățite pentru bara laterală pentru contrast și lizibilitate mai bune",
            "Rafinamente minore ale interfeței"
        ],
        "fixes": [],
        "patches": []
    },
    'tr': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Tam erişim için birleşik abonelik",
        "meta_title": "Tam erişim için birleşik abonelik - Frames",
        "meta_description": "macOS uygulaması artık iOS aboneliğine ek ücret ödemeden dahil. iPhone ve Mac'te tüm Frames özelliklerini kullanmak için birleşik fiyatlandırma.",
        "summary": "Mac uygulaması artık iOS aboneliğinize entegre edildi, tüm cihazlarda daha kolay erişim ve yönetim için Frames ekosistemini birleştiriyor.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Frames ekosistemi için birleşik fiyatlandırma"
            },
            {
                "type": "paragraph",
                "content": "Analog fotoğraf topluluğundan gelen geri bildirimlere dayanarak fiyatlandırma modelini iyileştirdim. Mac uygulaması artık ayrı bir abonelik gerektirmiyor, şimdi iOS aboneliğinize ek ücret ödemeden dahil. Bu birleşim, iOS'ta film detaylarını not almaktan Mac'te taranan görüntülere metadata entegre etmeye kadar tam Frames deneyiminin tadını çıkarmayı daha basit hale getiriyor."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Yeni Frames film fotoğrafçılığı uygulaması ömür boyu plan seçeneğini temsil eden Apple satın alma simgesi",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Kenar çubuğu iyileştirmeleri"
            },
            {
                "type": "paragraph",
                "content": "Kenar çubuğu, daha iyi kontrast sağlayan geliştirilmiş renklerle güncellendi, film metadata'nızı okumayı ve gezinmeyi kolaylaştırıyor. Küçük bir değişiklik, ama arşivinizde çalışırken fark edilir bir fark yaratıyor."
            }
        ],
        "improvements": [
            "Mac uygulaması artık iOS aboneliğine ek ücret ödemeden dahil",
            "Daha iyi kontrast ve okunabilirlik için geliştirilmiş kenar çubuğu renkleri",
            "Küçük arayüz iyileştirmeleri"
        ],
        "fixes": [],
        "patches": []
    },
    'el': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Ενοποιημένη συνδρομή για πλήρη πρόσβαση",
        "meta_title": "Ενοποιημένη συνδρομή για πλήρη πρόσβαση - Frames",
        "meta_description": "Η εφαρμογή macOS περιλαμβάνεται τώρα στη συνδρομή iOS χωρίς επιπλέον κόστος. Ενοποιημένη τιμολόγηση για όλες τις λειτουργίες Frames σε iPhone και Mac.",
        "summary": "Η εφαρμογή Mac είναι τώρα ενσωματωμένη στη συνδρομή σας iOS, ενοποιώντας το οικοσύστημα Frames για ευκολότερη πρόσβαση και διαχείριση σε όλες τις συσκευές.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Ενοποιημένη τιμολόγηση για το οικοσύστημα Frames"
            },
            {
                "type": "paragraph",
                "content": "Με βάση τα σχόλια από την κοινότητα αναλογικής φωτογραφίας, βελτίωσα το μοντέλο τιμολόγησης. Η εφαρμογή Mac δεν απαιτεί πλέον ξεχωριστή συνδρομή, περιλαμβάνεται τώρα στη συνδρομή σας iOS χωρίς επιπλέον κόστος. Αυτή η ενοποίηση κάνει πιο απλή την απόλαυση της πλήρους εμπειρίας Frames, από τη σημείωση λεπτομερειών φιλμ στο iOS έως την ενσωμάτωση μεταδεδομένων σε σαρωμένες εικόνες στο Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Εικονίδιο αγοράς Apple που αντιπροσωπεύει τη νέα επιλογή εφ' όρου ζωής για την εφαρμογή φωτογραφίας φιλμ Frames",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Βελτίωση πλαϊνής μπάρας"
            },
            {
                "type": "paragraph",
                "content": "Η πλαϊνή μπάρα έχει ενημερωθεί με βελτιωμένα χρώματα που παρέχουν καλύτερη αντίθεση, διευκολύνοντας την ανάγνωση και την πλοήγηση στα μεταδεδομένα φιλμ σας. Μικρή αλλαγή, αλλά κάνει αισθητή διαφορά όταν εργάζεστε στο αρχείο σας."
            }
        ],
        "improvements": [
            "Η εφαρμογή Mac περιλαμβάνεται τώρα στη συνδρομή iOS χωρίς επιπλέον κόστος",
            "Βελτιωμένα χρώματα πλαϊνής μπάρας για καλύτερη αντίθεση και αναγνωσιμότητα",
            "Μικρές βελτιώσεις διεπαφής"
        ],
        "fixes": [],
        "patches": []
    }
})

# Adding Asian languages
changelog_by_locale.update({
    'ja': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "フルアクセスのための統合サブスクリプション",
        "meta_title": "フルアクセスのための統合サブスクリプション - Frames",
        "meta_description": "macOSアプリがiOSサブスクリプションに追加料金なしで含まれるようになりました。iPhoneとMacで全てのFrames機能を使える統合価格。",
        "summary": "MacアプリがiOSサブスクリプションに統合され、全デバイスでのアクセスと管理を簡単にするFramesエコシステムを統一しました。",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Framesエコシステムの統合価格"
            },
            {
                "type": "paragraph",
                "content": "アナログ写真コミュニティからのフィードバックに基づいて、価格モデルを改善しました。Macアプリは別途サブスクリプションが不要になり、追加料金なしでiOSサブスクリプションに含まれるようになりました。この統合により、iOSでのフィルム詳細の記録からMacでのスキャン画像へのメタデータ統合まで、完全なFrames体験をより簡単にお楽しみいただけます。"
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "新しいFramesフィルム写真アプリのライフタイムプランオプションを表すApple購入アイコン",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "サイドバーの改善"
            },
            {
                "type": "paragraph",
                "content": "サイドバーがより良いコントラストを提供する改善された色で更新され、フィルムメタデータの読み取りとナビゲーションが容易になりました。小さな変更ですが、アーカイブを作業する際に顕著な違いを生み出します。"
            }
        ],
        "improvements": [
            "Macアプリが追加料金なしでiOSサブスクリプションに含まれるようになりました",
            "より良いコントラストと読みやすさのためのサイドバーの色の改善",
            "小さなインターフェースの改善"
        ],
        "fixes": [],
        "patches": []
    },
    'ko': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "완전한 액세스를 위한 통합 구독",
        "meta_title": "완전한 액세스를 위한 통합 구독 - Frames",
        "meta_description": "macOS 앱이 이제 추가 비용 없이 iOS 구독에 포함됩니다. iPhone과 Mac에서 모든 Frames 기능을 사용할 수 있는 통합 가격.",
        "summary": "Mac 앱이 이제 iOS 구독에 통합되어 모든 기기에서 더 쉬운 액세스와 관리를 위해 Frames 생태계를 통합했습니다.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Frames 생태계를 위한 통합 가격"
            },
            {
                "type": "paragraph",
                "content": "아날로그 사진 커뮤니티의 피드백을 바탕으로 가격 모델을 개선했습니다. Mac 앱은 더 이상 별도의 구독이 필요하지 않으며, 이제 추가 비용 없이 iOS 구독에 포함됩니다. 이 통합으로 iOS에서 필름 세부 정보를 기록하는 것부터 Mac에서 스캔한 이미지에 메타데이터를 통합하는 것까지 완전한 Frames 경험을 더 간단하게 즐길 수 있습니다."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "새로운 Frames 필름 사진 앱 평생 플랜 옵션을 나타내는 Apple 구매 아이콘",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "사이드바 개선"
            },
            {
                "type": "paragraph",
                "content": "사이드바가 더 나은 대비를 제공하는 개선된 색상으로 업데이트되어 필름 메타데이터를 더 쉽게 읽고 탐색할 수 있습니다. 작은 변경이지만 아카이브를 작업할 때 눈에 띄는 차이를 만듭니다."
            }
        ],
        "improvements": [
            "Mac 앱이 이제 추가 비용 없이 iOS 구독에 포함됩니다",
            "더 나은 대비와 가독성을 위한 사이드바 색상 개선",
            "작은 인터페이스 개선"
        ],
        "fixes": [],
        "patches": []
    },
    'hi': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "पूर्ण एक्सेस के लिए एकीकृत सदस्यता",
        "meta_title": "पूर्ण एक्सेस के लिए एकीकृत सदस्यता - Frames",
        "meta_description": "macOS ऐप अब बिना अतिरिक्त लागत के iOS सदस्यता में शामिल है। iPhone और Mac पर सभी Frames सुविधाओं का उपयोग करने के लिए एकीकृत मूल्य निर्धारण।",
        "summary": "Mac ऐप अब आपकी iOS सदस्यता में एकीकृत है, सभी उपकरणों पर आसान पहुंच और प्रबंधन के लिए Frames इकोसिस्टम को एकीकृत करता है।",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Frames इकोसिस्टम के लिए एकीकृत मूल्य निर्धारण"
            },
            {
                "type": "paragraph",
                "content": "एनालॉग फोटोग्राफी समुदाय की प्रतिक्रिया के आधार पर, मैंने मूल्य निर्धारण मॉडल को परिष्कृत किया है। Mac ऐप को अब अलग सदस्यता की आवश्यकता नहीं है, यह अब बिना अतिरिक्त लागत के आपकी iOS सदस्यता में शामिल है। यह एकीकरण संपूर्ण Frames अनुभव का आनंद लेना आसान बनाता है, iOS पर फ़िल्म विवरण नोट करने से लेकर Mac पर स्कैन की गई छवियों में मेटाडेटा एकीकृत करने तक।"
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "नए Frames फ़िल्म फ़ोटोग्राफ़ी ऐप आजीवन योजना विकल्प का प्रतिनिधित्व करने वाला Apple खरीद आइकन",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "साइडबार सुधार"
            },
            {
                "type": "paragraph",
                "content": "साइडबार को बेहतर रंगों के साथ अपडेट किया गया है जो बेहतर कंट्रास्ट प्रदान करते हैं, जिससे आपके फ़िल्म मेटाडेटा को पढ़ना और नेविगेट करना आसान हो जाता है। छोटा परिवर्तन, लेकिन जब आप अपने संग्रह में काम कर रहे हों तो यह ध्यान देने योग्य अंतर बनाता है।"
            }
        ],
        "improvements": [
            "Mac ऐप अब बिना अतिरिक्त लागत के iOS सदस्यता में शामिल",
            "बेहतर कंट्रास्ट और पठनीयता के लिए साइडबार रंगों में सुधार",
            "मामूली इंटरफ़ेस सुधार"
        ],
        "fixes": [],
        "patches": []
    },
    'zh': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "统一订阅实现完整访问",
        "meta_title": "统一订阅实现完整访问 - Frames",
        "meta_description": "macOS 应用现已包含在 iOS 订阅中，无需额外费用。统一定价让您在 iPhone 和 Mac 上使用所有 Frames 功能。",
        "summary": "Mac 应用现已集成到您的 iOS 订阅中，统一了 Frames 生态系统，使跨设备访问和管理更加轻松。",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Frames 生态系统的统一定价"
            },
            {
                "type": "paragraph",
                "content": "根据模拟摄影社区的反馈，我改进了定价模式。Mac 应用不再需要单独订阅，现在无需额外费用即可包含在您的 iOS 订阅中。这种统一使享受完整的 Frames 体验变得更简单，从在 iOS 上记录胶片细节到在 Mac 上将元数据集成到扫描图像中。"
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "代表新 Frames 胶片摄影应用终身计划选项的 Apple 购买图标",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "侧边栏优化"
            },
            {
                "type": "paragraph",
                "content": "侧边栏已更新为改进的颜色，提供更好的对比度，使阅读和浏览您的胶片元数据更加容易。虽然是小改动，但在您浏览档案时会产生明显的差异。"
            }
        ],
        "improvements": [
            "Mac 应用现已包含在 iOS 订阅中，无需额外费用",
            "改进侧边栏颜色以获得更好的对比度和可读性",
            "小型界面改进"
        ],
        "fixes": [],
        "patches": []
    },
    'zh-hant': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "統一訂閱實現完整存取",
        "meta_title": "統一訂閱實現完整存取 - Frames",
        "meta_description": "macOS 應用程式現已包含在 iOS 訂閱中，無需額外費用。統一定價讓您在 iPhone 和 Mac 上使用所有 Frames 功能。",
        "summary": "Mac 應用程式現已整合到您的 iOS 訂閱中，統一了 Frames 生態系統，使跨裝置存取和管理更加輕鬆。",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Frames 生態系統的統一定價"
            },
            {
                "type": "paragraph",
                "content": "根據類比攝影社群的回饋，我改進了定價模式。Mac 應用程式不再需要單獨訂閱，現在無需額外費用即可包含在您的 iOS 訂閱中。這種統一使享受完整的 Frames 體驗變得更簡單，從在 iOS 上記錄膠片細節到在 Mac 上將元資料整合到掃描影像中。"
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "代表新 Frames 膠片攝影應用程式終身計劃選項的 Apple 購買圖示",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "側邊欄優化"
            },
            {
                "type": "paragraph",
                "content": "側邊欄已更新為改進的顏色，提供更好的對比度，使閱讀和瀏覽您的膠片元資料更加容易。雖然是小改動，但在您瀏覽檔案時會產生明顯的差異。"
            }
        ],
        "improvements": [
            "Mac 應用程式現已包含在 iOS 訂閱中，無需額外費用",
            "改進側邊欄顏色以獲得更好的對比度和可讀性",
            "小型介面改進"
        ],
        "fixes": [],
        "patches": []
    },
    'id': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Langganan terpadu untuk akses penuh",
        "meta_title": "Langganan terpadu untuk akses penuh - Frames",
        "meta_description": "Aplikasi macOS kini termasuk dalam langganan iOS tanpa biaya tambahan. Harga terpadu untuk semua fitur Frames di iPhone dan Mac.",
        "summary": "Aplikasi Mac kini terintegrasi ke dalam langganan iOS Anda, menyatukan ekosistem Frames untuk akses dan pengelolaan yang lebih mudah di semua perangkat.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Harga terpadu untuk ekosistem Frames"
            },
            {
                "type": "paragraph",
                "content": "Berdasarkan umpan balik dari komunitas fotografi analog, saya telah menyempurnakan model harga. Aplikasi Mac tidak lagi memerlukan langganan terpisah, sekarang sudah termasuk dalam langganan iOS Anda tanpa biaya tambahan. Penyatuan ini membuat lebih mudah untuk menikmati pengalaman Frames yang lengkap, dari mencatat detail film di iOS hingga mengintegrasikan metadata ke dalam gambar yang dipindai di Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Ikon pembelian Apple yang mewakili opsi paket seumur hidup aplikasi fotografi film Frames yang baru",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Penyempurnaan sidebar"
            },
            {
                "type": "paragraph",
                "content": "Sidebar telah diperbarui dengan warna yang lebih baik yang memberikan kontras lebih baik, memudahkan untuk membaca dan menavigasi metadata film Anda. Perubahan kecil, tetapi membuat perbedaan yang nyata saat Anda bekerja melalui arsip Anda."
            }
        ],
        "improvements": [
            "Aplikasi Mac kini termasuk dalam langganan iOS tanpa biaya tambahan",
            "Warna sidebar yang lebih baik untuk kontras dan keterbacaan yang lebih baik",
            "Penyempurnaan antarmuka kecil"
        ],
        "fixes": [],
        "patches": []
    },
    'vi': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "Đăng ký thống nhất để truy cập đầy đủ",
        "meta_title": "Đăng ký thống nhất để truy cập đầy đủ - Frames",
        "meta_description": "Ứng dụng macOS hiện được bao gồm trong đăng ký iOS mà không mất thêm phí. Giá thống nhất cho tất cả tính năng Frames trên iPhone và Mac.",
        "summary": "Ứng dụng Mac hiện đã được tích hợp vào đăng ký iOS của bạn, thống nhất hệ sinh thái Frames để truy cập và quản lý dễ dàng hơn trên tất cả các thiết bị.",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "Giá thống nhất cho hệ sinh thái Frames"
            },
            {
                "type": "paragraph",
                "content": "Dựa trên phản hồi từ cộng đồng nhiếp ảnh analog, tôi đã tinh chỉnh mô hình giá. Ứng dụng Mac không còn yêu cầu đăng ký riêng, giờ đây nó được bao gồm trong đăng ký iOS của bạn mà không mất thêm phí. Sự thống nhất này làm cho việc tận hưởng trải nghiệm Frames hoàn chỉnh trở nên đơn giản hơn, từ ghi chú chi tiết phim trên iOS đến tích hợp metadata vào hình ảnh đã quét trên Mac."
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "Biểu tượng mua hàng Apple đại diện cho tùy chọn gói trọn đời mới của ứng dụng nhiếp ảnh phim Frames",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "Cải thiện thanh bên"
            },
            {
                "type": "paragraph",
                "content": "Thanh bên đã được cập nhật với các màu sắc được cải thiện cung cấp độ tương phản tốt hơn, giúp đọc và điều hướng metadata phim của bạn dễ dàng hơn. Thay đổi nhỏ, nhưng tạo ra sự khác biệt đáng chú ý khi bạn làm việc trong kho lưu trữ của mình."
            }
        ],
        "improvements": [
            "Ứng dụng Mac hiện được bao gồm trong đăng ký iOS mà không mất thêm phí",
            "Cải thiện màu thanh bên để có độ tương phản và khả năng đọc tốt hơn",
            "Cải tiến giao diện nhỏ"
        ],
        "fixes": [],
        "patches": []
    },
    'th': {
        "version": "1.11.0",
        "version_short": "1.11",
        "url_slug": "1-11-macos",
        "platform": "macos",
        "release_date": "2025-11-29T10:00:00.000Z",
        "title": "การสมัครสมาชิกแบบรวมสำหรับการเข้าถึงเต็มรูปแบบ",
        "meta_title": "การสมัครสมาชิกแบบรวมสำหรับการเข้าถึงเต็มรูปแบบ - Frames",
        "meta_description": "แอป macOS ตอนนี้รวมอยู่ในการสมัครสมาชิก iOS โดยไม่มีค่าใช้จ่ายเพิ่มเติม ราคารวมสำหรับฟีเจอร์ Frames ทั้งหมดบน iPhone และ Mac",
        "summary": "แอป Mac ตอนนี้รวมเข้ากับการสมัครสมาชิก iOS ของคุณ รวมระบบนิเวศ Frames เพื่อการเข้าถึงและการจัดการที่ง่ายขึ้นในทุกอุปกรณ์",
        "sections": [
            {
                "type": "heading",
                "level": 3,
                "content": "ราคารวมสำหรับระบบนิเวศ Frames"
            },
            {
                "type": "paragraph",
                "content": "จากคำติชมของชุมชนถ่ายภาพอนาล็อก ฉันได้ปรับปรุงโมเดลราคา แอป Mac ไม่ต้องการการสมัครสมาชิกแยกต่างหากอีกต่อไป ตอนนี้รวมอยู่ในการสมัครสมาชิก iOS ของคุณโดยไม่มีค่าใช้จ่ายเพิ่มเติม การรวมนี้ทำให้การเพลิดเพลินกับประสบการณ์ Frames ที่สมบูรณ์ง่ายขึ้น ตั้งแต่การบันทึกรายละเอียดฟิล์มบน iOS ไปจนถึงการรวมเมตาดาต้าลงในภาพที่สแกนบน Mac"
            },
            {
                "type": "media",
                "image": "/lib/img/shared/changelog/frames-mac-1.11.0-1.png",
                "image_2x": "/lib/img/shared/changelog/frames-mac-1.11.0-1@2x.png",
                "alt": "ไอคอนการซื้อของ Apple ที่แสดงถึงตัวเลือกแพ็คเกจตลอดชีพใหม่ของแอปถ่ายภาพฟิล์ม Frames",
                "width": "400",
                "height": "300"
            },
            {
                "type": "heading",
                "level": 3,
                "content": "การปรับปรุงแถบด้านข้าง"
            },
            {
                "type": "paragraph",
                "content": "แถบด้านข้างได้รับการอัปเดตด้วยสีที่ดีขึ้นซึ่งให้ความคมชัดที่ดีกว่า ทำให้อ่านและนำทางเมตาดาต้าฟิล์มของคุณได้ง่ายขึ้น การเปลี่ยนแปลงเล็กน้อย แต่ส่งผลต่อความแตกต่างอย่างเห็นได้ชัดเมื่อคุณทำงานผ่านคลังเก็บของคุณ"
            }
        ],
        "improvements": [
            "แอป Mac ตอนนี้รวมอยู่ในการสมัครสมาชิก iOS โดยไม่มีค่าใช้จ่ายเพิ่มเติม",
            "ปรับปรุงสีแถบด้านข้างเพื่อความคมชัดและความสามารถในการอ่านที่ดีขึ้น",
            "การปรับปรุงอินเทอร์เฟซเล็กน้อย"
        ],
        "fixes": [],
        "patches": []
    }
})

def update_changelog(changelog_dir):
    """Update all 1.11.0-macos.json files."""

    updated_count = 0
    error_count = 0

    for locale_code, changelog_data in changelog_by_locale.items():
        file_path = Path(changelog_dir) / locale_code / "1.11.0-macos.json"

        if not file_path.exists():
            print(f"⚠️  File not found: {file_path}")
            error_count += 1
            continue

        try:
            # Write the complete changelog
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(changelog_data, f, ensure_ascii=False, indent=2)

            print(f"✓ Updated {locale_code:8} → {changelog_data['title'][:50]}")
            updated_count += 1

        except Exception as e:
            print(f"❌ Error updating {locale_code}: {e}")
            error_count += 1

    print()
    print("=" * 70)
    print(f"✓ Successfully updated: {updated_count} files")
    if error_count > 0:
        print(f"❌ Errors: {error_count} files")
    print("=" * 70)

if __name__ == "__main__":
    changelog_dir = "/Users/vnn/Documents/Dev/framesWeb/sources/locales/changelog"
    update_changelog(changelog_dir)
