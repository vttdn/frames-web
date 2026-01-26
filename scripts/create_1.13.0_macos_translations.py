#!/usr/bin/env python3
"""
Script to create 1.13.0-macos.json changelog files for all supported languages.
Professional translations adapted for film photography terminology.
"""

import json
from pathlib import Path

# Base path for changelog locales
BASE_PATH = Path(__file__).parent.parent / "sources" / "locales" / "changelog"

# Base structure that's the same for all languages
BASE_STRUCTURE = {
    "version": "1.13.0",
    "version_short": "1.13",
    "url_slug": "1-13-macos",
    "platform": "macos",
    "release_date": "2026-01-26T10:00:00.000Z",
}

# Media section (same for all languages except alt text)
def get_media_section(alt_text):
    return {
        "type": "media",
        "image": "/lib/img/shared/changelog/frames-mac-1.13.0-1.png",
        "image_2x": "/lib/img/shared/changelog/frames-mac-1.13.0-1@2x.png",
        "alt": alt_text,
        "width": "400",
        "height": "300"
    }

# All translations
TRANSLATIONS = {
    "da": {
        "title": "Fokusafstand i sidebjælke og EXIF",
        "meta_title": "Fokusafstand i sidebjælke og EXIF - Frames",
        "meta_description": "Fokusafstand vises nu i sidebjælken og skrives til EXIF-metadata. Subject Distance Range beregnes ud fra fokusafstand og brændvidde.",
        "summary": "Denne opdatering bringer understøttelse af fokusafstand til Mac-appen. Hvis du registrerer fokusafstand i Frames til iOS, vises disse data nu i sidebjælken og skrives til EXIF-metadata, når du eksporterer dine scanninger. Opdateringen forbedrer også håndteringen af visse metadataværdier og inkluderer visuelle forbedringer til macOS Sequoia.",
        "alt": "Frames macOS-app viser fokusafstand i sidebjælken",
        "heading_1": "Fokusafstand og Subject Distance Range",
        "paragraph_1": "Fokusafstand er nu synlig i sidebjælken sammen med dine andre optagedata. Når du eksporterer til DNG, JPG eller TIFF, skrives denne værdi til Subject Distance-feltet i EXIF-metadata. Appen beregner også et Subject Distance Range ved at kombinere fokusafstanden med den brændvidde, du brugte til rammen, hvilket giver billedvisere og katalogiseringssoftware mere kontekst om dit billede.",
        "paragraph_2": "Denne funktion fungerer med fokusafstandsdata registreret i Frames til iOS (version 1.21.0 og senere). Hvis du har logget fokusafstand på din telefon, følger disse oplysninger nu med til dine eksporterede filer på Mac.",
        "improvements": [
            "Fokusafstand vises i sidebjælken",
            "Subject Distance skrives til EXIF-metadata for DNG-, JPG- og TIFF-eksport",
            "Subject Distance Range beregnes ud fra fokusafstand og brændvidde",
            "Flash Off skrives nu til metadata i stedet for at blive sprunget over",
            "0 EV eksponeringskompensation skrives nu til metadata i stedet for at blive sprunget over",
            "Visuelle forbedringer til macOS Sequoia, herunder sidebjælkens udseende"
        ]
    },
    "de": {
        "title": "Aufnahmeentfernung in Seitenleiste und EXIF",
        "meta_title": "Aufnahmeentfernung in Seitenleiste und EXIF - Frames",
        "meta_description": "Aufnahmeentfernung erscheint jetzt in der Seitenleiste und wird in EXIF-Metadaten geschrieben. Subject Distance Range wird berechnet.",
        "summary": "Dieses Update bringt Unterstützung für Aufnahmeentfernung in die Mac-App. Wenn du Aufnahmeentfernung in Frames für iOS erfasst, erscheinen diese Daten jetzt in der Seitenleiste und werden beim Export deiner Scans in die EXIF-Metadaten geschrieben. Das Update verbessert auch die Handhabung bestimmter Metadatenwerte und enthält visuelle Verfeinerungen für macOS Sequoia.",
        "alt": "Frames macOS-App zeigt Aufnahmeentfernung in der Seitenleiste",
        "heading_1": "Aufnahmeentfernung und Subject Distance Range",
        "paragraph_1": "Die Aufnahmeentfernung ist jetzt in der Seitenleiste neben deinen anderen Aufnahmedaten sichtbar. Beim Export in DNG, JPG oder TIFF wird dieser Wert in das Subject Distance-Feld der EXIF-Metadaten geschrieben. Die App berechnet auch einen Subject Distance Range, indem sie die Aufnahmeentfernung mit der verwendeten Brennweite kombiniert, was Bildbetrachtern und Katalogisierungssoftware mehr Kontext über deine Aufnahme gibt.",
        "paragraph_2": "Diese Funktion arbeitet mit Aufnahmeentfernungsdaten, die in Frames für iOS (Version 1.21.0 und später) erfasst wurden. Wenn du Aufnahmeentfernung auf deinem Telefon protokolliert hast, werden diese Informationen jetzt in deine exportierten Dateien auf dem Mac übernommen.",
        "improvements": [
            "Aufnahmeentfernung in der Seitenleiste angezeigt",
            "Subject Distance wird in EXIF-Metadaten für DNG-, JPG- und TIFF-Exporte geschrieben",
            "Subject Distance Range wird aus Aufnahmeentfernung und Brennweite berechnet",
            "Flash Off wird jetzt in Metadaten geschrieben statt übersprungen",
            "0 EV Belichtungskorrektur wird jetzt in Metadaten geschrieben statt übersprungen",
            "Visuelle Verfeinerungen für macOS Sequoia, einschließlich Seitenleisten-Erscheinungsbild"
        ]
    },
    "el": {
        "title": "Απόσταση εστίασης στην πλαϊνή μπάρα και EXIF",
        "meta_title": "Απόσταση εστίασης στην πλαϊνή μπάρα και EXIF - Frames",
        "meta_description": "Η απόσταση εστίασης εμφανίζεται τώρα στην πλαϊνή μπάρα και εγγράφεται στα μεταδεδομένα EXIF. Υπολογισμός Subject Distance Range.",
        "summary": "Αυτή η ενημέρωση φέρνει υποστήριξη απόστασης εστίασης στην εφαρμογή Mac. Αν καταγράφετε απόσταση εστίασης στο Frames για iOS, αυτά τα δεδομένα εμφανίζονται τώρα στην πλαϊνή μπάρα και εγγράφονται στα μεταδεδομένα EXIF όταν εξάγετε τις σαρώσεις σας. Η ενημέρωση βελτιώνει επίσης τον χειρισμό ορισμένων τιμών μεταδεδομένων και περιλαμβάνει οπτικές βελτιώσεις για το macOS Sequoia.",
        "alt": "Εφαρμογή Frames macOS που δείχνει την απόσταση εστίασης στην πλαϊνή μπάρα",
        "heading_1": "Απόσταση εστίασης και Subject Distance Range",
        "paragraph_1": "Η απόσταση εστίασης είναι πλέον ορατή στην πλαϊνή μπάρα μαζί με τα άλλα δεδομένα λήψης σας. Όταν εξάγετε σε DNG, JPG ή TIFF, αυτή η τιμή εγγράφεται στο πεδίο Subject Distance των μεταδεδομένων EXIF. Η εφαρμογή υπολογίζει επίσης ένα Subject Distance Range συνδυάζοντας την απόσταση εστίασης με την εστιακή απόσταση που χρησιμοποιήσατε για το καρέ, δίνοντας στα προγράμματα προβολής και καταλογογράφησης περισσότερο πλαίσιο για τη λήψη σας.",
        "paragraph_2": "Αυτή η λειτουργία λειτουργεί με δεδομένα απόστασης εστίασης που καταγράφηκαν στο Frames για iOS (έκδοση 1.21.0 και μεταγενέστερες). Αν έχετε καταγράψει απόσταση εστίασης στο τηλέφωνό σας, αυτές οι πληροφορίες μεταφέρονται τώρα στα εξαγόμενα αρχεία σας στο Mac.",
        "improvements": [
            "Απόσταση εστίασης εμφανίζεται στην πλαϊνή μπάρα",
            "Subject Distance εγγράφεται στα μεταδεδομένα EXIF για εξαγωγές DNG, JPG και TIFF",
            "Subject Distance Range υπολογίζεται από την απόσταση εστίασης και την εστιακή απόσταση",
            "Το Flash Off εγγράφεται τώρα στα μεταδεδομένα αντί να παραλείπεται",
            "Η αντιστάθμιση έκθεσης 0 EV εγγράφεται τώρα στα μεταδεδομένα αντί να παραλείπεται",
            "Οπτικές βελτιώσεις για macOS Sequoia, συμπεριλαμβανομένης της εμφάνισης της πλαϊνής μπάρας"
        ]
    },
    "es": {
        "title": "Distancia de enfoque en barra lateral y EXIF",
        "meta_title": "Distancia de enfoque en barra lateral y EXIF - Frames",
        "meta_description": "La distancia de enfoque aparece ahora en la barra lateral y se escribe en los metadatos EXIF. Subject Distance Range se calcula automáticamente.",
        "summary": "Esta actualización trae soporte de distancia de enfoque a la app de Mac. Si registras la distancia de enfoque en Frames para iOS, esos datos ahora aparecen en la barra lateral y se escriben en los metadatos EXIF cuando exportas tus escaneos. La actualización también mejora el manejo de ciertos valores de metadatos e incluye refinamientos visuales para macOS Sequoia.",
        "alt": "App Frames macOS mostrando la distancia de enfoque en la barra lateral",
        "heading_1": "Distancia de enfoque y Subject Distance Range",
        "paragraph_1": "La distancia de enfoque ahora es visible en la barra lateral junto con tus otros datos de disparo. Cuando exportas a DNG, JPG o TIFF, este valor se escribe en el campo Subject Distance de los metadatos EXIF. La app también calcula un Subject Distance Range combinando la distancia de enfoque con la distancia focal que usaste para el fotograma, dando a los visores de imágenes y software de catalogación más contexto sobre tu toma.",
        "paragraph_2": "Esta función trabaja con datos de distancia de enfoque registrados en Frames para iOS (versión 1.21.0 y posteriores). Si has estado registrando la distancia de enfoque en tu teléfono, esa información ahora se traslada a tus archivos exportados en Mac.",
        "improvements": [
            "Distancia de enfoque mostrada en la barra lateral",
            "Subject Distance escrito en metadatos EXIF para exportaciones DNG, JPG y TIFF",
            "Subject Distance Range calculado a partir de la distancia de enfoque y la distancia focal",
            "Flash Off ahora se escribe en los metadatos en lugar de omitirse",
            "La compensación de exposición 0 EV ahora se escribe en los metadatos en lugar de omitirse",
            "Refinamientos visuales para macOS Sequoia, incluyendo la apariencia de la barra lateral"
        ]
    },
    "fi": {
        "title": "Tarkennusetäisyys sivupalkissa ja EXIF:ssä",
        "meta_title": "Tarkennusetäisyys sivupalkissa ja EXIF:ssä - Frames",
        "meta_description": "Tarkennusetäisyys näkyy nyt sivupalkissa ja kirjoitetaan EXIF-metatietoihin. Subject Distance Range lasketaan automaattisesti.",
        "summary": "Tämä päivitys tuo tarkennusetäisyyden tuen Mac-sovellukseen. Jos tallennat tarkennusetäisyyden Frames iOS:ssa, nämä tiedot näkyvät nyt sivupalkissa ja kirjoitetaan EXIF-metatietoihin, kun viet skannauksesi. Päivitys parantaa myös tiettyjen metatietoarvojen käsittelyä ja sisältää visuaalisia parannuksia macOS Sequoialle.",
        "alt": "Frames macOS -sovellus näyttää tarkennusetäisyyden sivupalkissa",
        "heading_1": "Tarkennusetäisyys ja Subject Distance Range",
        "paragraph_1": "Tarkennusetäisyys näkyy nyt sivupalkissa muiden kuvaustietojesi rinnalla. Kun viet DNG-, JPG- tai TIFF-muotoon, tämä arvo kirjoitetaan EXIF-metatietojen Subject Distance -kenttään. Sovellus laskee myös Subject Distance Range -arvon yhdistämällä tarkennusetäisyyden kehykselle käyttämääsi polttoväliin, antaen kuvankatseluohjelmille ja luettelointisovelluksille enemmän tietoa kuvauksestasi.",
        "paragraph_2": "Tämä toiminto toimii Frames iOS:ssa (versio 1.21.0 ja uudemmat) tallennettujen tarkennusetäisyystietojen kanssa. Jos olet kirjannut tarkennusetäisyyttä puhelimellasi, nämä tiedot siirtyvät nyt vietyihin tiedostoihisi Macilla.",
        "improvements": [
            "Tarkennusetäisyys näkyy sivupalkissa",
            "Subject Distance kirjoitetaan EXIF-metatietoihin DNG-, JPG- ja TIFF-vienneissä",
            "Subject Distance Range lasketaan tarkennusetäisyydestä ja polttovälistä",
            "Flash Off kirjoitetaan nyt metatietoihin ohittamisen sijaan",
            "0 EV valotuksen korjaus kirjoitetaan nyt metatietoihin ohittamisen sijaan",
            "Visuaalisia parannuksia macOS Sequoialle, mukaan lukien sivupalkin ulkoasu"
        ]
    },
    "fr": {
        "title": "Distance de mise au point dans la barre latérale et EXIF",
        "meta_title": "Distance de mise au point dans la barre latérale et EXIF - Frames",
        "meta_description": "La distance de mise au point apparaît dans la barre latérale et est inscrite dans les métadonnées EXIF. Calcul automatique du Subject Distance Range.",
        "summary": "Cette mise à jour apporte la prise en charge de la distance de mise au point dans l'app Mac. Si vous enregistrez la distance de mise au point dans Frames pour iOS, ces données apparaissent maintenant dans la barre latérale et sont inscrites dans les métadonnées EXIF lors de l'exportation de vos scans. La mise à jour améliore également la gestion de certaines valeurs de métadonnées et inclut des améliorations visuelles pour macOS Sequoia.",
        "alt": "App Frames macOS affichant la distance de mise au point dans la barre latérale",
        "heading_1": "Distance de mise au point et Subject Distance Range",
        "paragraph_1": "La distance de mise au point est maintenant visible dans la barre latérale avec vos autres données de prise de vue. Lors de l'exportation en DNG, JPG ou TIFF, cette valeur est inscrite dans le champ Subject Distance des métadonnées EXIF. L'app calcule également un Subject Distance Range en combinant la distance de mise au point avec la focale utilisée pour la frame, donnant aux visionneuses d'images et aux logiciels de catalogage plus de contexte sur votre prise de vue.",
        "paragraph_2": "Cette fonctionnalité fonctionne avec les données de distance de mise au point enregistrées dans Frames pour iOS (version 1.21.0 et ultérieures). Si vous avez enregistré la distance de mise au point sur votre téléphone, ces informations sont maintenant transférées dans vos fichiers exportés sur Mac.",
        "improvements": [
            "Distance de mise au point affichée dans la barre latérale",
            "Subject Distance inscrit dans les métadonnées EXIF pour les exports DNG, JPG et TIFF",
            "Subject Distance Range calculé à partir de la distance de mise au point et de la focale",
            "Flash Off est maintenant inscrit dans les métadonnées au lieu d'être ignoré",
            "La correction d'exposition 0 EV est maintenant inscrite dans les métadonnées au lieu d'être ignorée",
            "Améliorations visuelles pour macOS Sequoia, y compris l'apparence de la barre latérale"
        ]
    },
    "hi": {
        "title": "साइडबार और EXIF में फोकस दूरी",
        "meta_title": "साइडबार और EXIF में फोकस दूरी - Frames",
        "meta_description": "फोकस दूरी अब साइडबार में दिखाई देती है और EXIF मेटाडेटा में लिखी जाती है। Subject Distance Range की गणना स्वचालित रूप से होती है।",
        "summary": "यह अपडेट Mac ऐप में फोकस दूरी समर्थन लाता है। यदि आप Frames for iOS में फोकस दूरी रिकॉर्ड करते हैं, तो वह डेटा अब साइडबार में दिखाई देता है और जब आप अपने स्कैन निर्यात करते हैं तो EXIF मेटाडेटा में लिखा जाता है। अपडेट कुछ मेटाडेटा मानों के संचालन में भी सुधार करता है और macOS Sequoia के लिए दृश्य सुधार शामिल करता है।",
        "alt": "Frames macOS ऐप साइडबार में फोकस दूरी दिखा रहा है",
        "heading_1": "फोकस दूरी और Subject Distance Range",
        "paragraph_1": "फोकस दूरी अब आपके अन्य शूटिंग डेटा के साथ साइडबार में दिखाई देती है। जब आप DNG, JPG या TIFF में निर्यात करते हैं, तो यह मान EXIF मेटाडेटा के Subject Distance फ़ील्ड में लिखा जाता है। ऐप फ्रेम के लिए उपयोग की गई फोकल लेंथ के साथ फोकस दूरी को मिलाकर Subject Distance Range की भी गणना करता है, जिससे इमेज व्यूअर और कैटलॉगिंग सॉफ़्टवेयर को आपके शॉट के बारे में अधिक संदर्भ मिलता है।",
        "paragraph_2": "यह सुविधा Frames for iOS (संस्करण 1.21.0 और बाद के) में रिकॉर्ड किए गए फोकस दूरी डेटा के साथ काम करती है। यदि आप अपने फोन पर फोकस दूरी लॉग कर रहे हैं, तो वह जानकारी अब Mac पर आपकी निर्यात की गई फ़ाइलों में स्थानांतरित हो जाती है।",
        "improvements": [
            "फोकस दूरी साइडबार में प्रदर्शित",
            "Subject Distance DNG, JPG और TIFF निर्यात के लिए EXIF मेटाडेटा में लिखा गया",
            "Subject Distance Range फोकस दूरी और फोकल लेंथ से गणना किया गया",
            "Flash Off अब छोड़े जाने के बजाय मेटाडेटा में लिखा जाता है",
            "0 EV एक्सपोज़र बायस अब छोड़े जाने के बजाय मेटाडेटा में लिखा जाता है",
            "macOS Sequoia के लिए दृश्य सुधार, साइडबार उपस्थिति सहित"
        ]
    },
    "id": {
        "title": "Jarak fokus di sidebar dan EXIF",
        "meta_title": "Jarak fokus di sidebar dan EXIF - Frames",
        "meta_description": "Jarak fokus kini muncul di sidebar dan ditulis ke metadata EXIF. Subject Distance Range dihitung secara otomatis.",
        "summary": "Pembaruan ini membawa dukungan jarak fokus ke aplikasi Mac. Jika Anda merekam jarak fokus di Frames untuk iOS, data tersebut kini muncul di sidebar dan ditulis ke metadata EXIF saat Anda mengekspor scan. Pembaruan ini juga memperbaiki penanganan nilai metadata tertentu dan menyertakan penyempurnaan visual untuk macOS Sequoia.",
        "alt": "Aplikasi Frames macOS menampilkan jarak fokus di sidebar",
        "heading_1": "Jarak fokus dan Subject Distance Range",
        "paragraph_1": "Jarak fokus kini terlihat di sidebar bersama data pemotretan lainnya. Saat Anda mengekspor ke DNG, JPG, atau TIFF, nilai ini ditulis ke bidang Subject Distance dalam metadata EXIF. Aplikasi juga menghitung Subject Distance Range dengan menggabungkan jarak fokus dengan panjang fokus yang Anda gunakan untuk frame tersebut, memberikan penampil gambar dan perangkat lunak katalog lebih banyak konteks tentang pengambilan gambar Anda.",
        "paragraph_2": "Fitur ini bekerja dengan data jarak fokus yang direkam di Frames untuk iOS (versi 1.21.0 dan yang lebih baru). Jika Anda telah mencatat jarak fokus di ponsel, informasi tersebut kini terbawa ke file yang diekspor di Mac.",
        "improvements": [
            "Jarak fokus ditampilkan di sidebar",
            "Subject Distance ditulis ke metadata EXIF untuk ekspor DNG, JPG, dan TIFF",
            "Subject Distance Range dihitung dari jarak fokus dan panjang fokus",
            "Flash Off kini ditulis ke metadata alih-alih dilewati",
            "Bias eksposur 0 EV kini ditulis ke metadata alih-alih dilewati",
            "Penyempurnaan visual untuk macOS Sequoia, termasuk tampilan sidebar"
        ]
    },
    "it": {
        "title": "Distanza di messa a fuoco nella barra laterale e EXIF",
        "meta_title": "Distanza di messa a fuoco nella barra laterale e EXIF - Frames",
        "meta_description": "La distanza di messa a fuoco appare nella barra laterale e viene scritta nei metadati EXIF. Calcolo automatico del Subject Distance Range.",
        "summary": "Questo aggiornamento porta il supporto della distanza di messa a fuoco nell'app Mac. Se registri la distanza di messa a fuoco in Frames per iOS, quei dati ora appaiono nella barra laterale e vengono scritti nei metadati EXIF quando esporti le tue scansioni. L'aggiornamento migliora anche la gestione di alcuni valori dei metadati e include perfezionamenti visivi per macOS Sequoia.",
        "alt": "App Frames macOS che mostra la distanza di messa a fuoco nella barra laterale",
        "heading_1": "Distanza di messa a fuoco e Subject Distance Range",
        "paragraph_1": "La distanza di messa a fuoco è ora visibile nella barra laterale insieme agli altri dati di scatto. Quando esporti in DNG, JPG o TIFF, questo valore viene scritto nel campo Subject Distance dei metadati EXIF. L'app calcola anche un Subject Distance Range combinando la distanza di messa a fuoco con la lunghezza focale usata per il fotogramma, fornendo ai visualizzatori di immagini e ai software di catalogazione più contesto sul tuo scatto.",
        "paragraph_2": "Questa funzione lavora con i dati di distanza di messa a fuoco registrati in Frames per iOS (versione 1.21.0 e successive). Se hai registrato la distanza di messa a fuoco sul tuo telefono, queste informazioni ora vengono trasferite nei file esportati su Mac.",
        "improvements": [
            "Distanza di messa a fuoco visualizzata nella barra laterale",
            "Subject Distance scritto nei metadati EXIF per esportazioni DNG, JPG e TIFF",
            "Subject Distance Range calcolato dalla distanza di messa a fuoco e dalla lunghezza focale",
            "Flash Off ora viene scritto nei metadati invece di essere saltato",
            "La compensazione dell'esposizione 0 EV ora viene scritta nei metadati invece di essere saltata",
            "Perfezionamenti visivi per macOS Sequoia, incluso l'aspetto della barra laterale"
        ]
    },
    "ja": {
        "title": "サイドバーとEXIFに撮影距離を表示",
        "meta_title": "サイドバーとEXIFに撮影距離を表示 - Frames",
        "meta_description": "撮影距離がサイドバーに表示され、EXIFメタデータに書き込まれるようになりました。Subject Distance Rangeは自動計算されます",
        "summary": "このアップデートでは、Macアプリに撮影距離のサポートが追加されました。Frames for iOSで撮影距離を記録している場合、そのデータがサイドバーに表示され、スキャンをエクスポートする際にEXIFメタデータに書き込まれます。また、特定のメタデータ値の処理が改善され、macOS Sequoia向けの視覚的な改良も含まれています。",
        "alt": "Frames macOSアプリのサイドバーに撮影距離が表示されている画面",
        "heading_1": "撮影距離とSubject Distance Range",
        "paragraph_1": "撮影距離が他の撮影データと一緒にサイドバーに表示されるようになりました。DNG、JPG、TIFFにエクスポートすると、この値がEXIFメタデータのSubject Distanceフィールドに書き込まれます。アプリはまた、撮影距離とコマに使用した焦点距離を組み合わせてSubject Distance Rangeを計算し、画像ビューアやカタログソフトウェアに撮影に関するより詳しい情報を提供します。",
        "paragraph_2": "この機能は、Frames for iOS（バージョン1.21.0以降）で記録された撮影距離データと連携します。スマートフォンで撮影距離を記録していた場合、その情報がMacでエクスポートしたファイルに引き継がれます。",
        "improvements": [
            "撮影距離をサイドバーに表示",
            "DNG、JPG、TIFFエクスポート時にSubject DistanceをEXIFメタデータに書き込み",
            "撮影距離と焦点距離からSubject Distance Rangeを計算",
            "Flash Offがスキップされずにメタデータに書き込まれるように",
            "0 EVの露出補正がスキップされずにメタデータに書き込まれるように",
            "macOS Sequoia向けの視覚的な改良（サイドバーの外観を含む）"
        ]
    },
    "ko": {
        "title": "사이드바 및 EXIF에 초점 거리 표시",
        "meta_title": "사이드바 및 EXIF에 초점 거리 표시 - Frames",
        "meta_description": "초점 거리가 이제 사이드바에 표시되고 EXIF 메타데이터에 기록됩니다. Subject Distance Range가 자동으로 계산됩니다.",
        "summary": "이번 업데이트는 Mac 앱에 초점 거리 지원을 추가합니다. Frames for iOS에서 초점 거리를 기록하면 해당 데이터가 이제 사이드바에 표시되고 스캔을 내보낼 때 EXIF 메타데이터에 기록됩니다. 또한 특정 메타데이터 값의 처리가 개선되었으며 macOS Sequoia를 위한 시각적 개선이 포함되어 있습니다.",
        "alt": "Frames macOS 앱의 사이드바에 초점 거리가 표시된 화면",
        "heading_1": "초점 거리 및 Subject Distance Range",
        "paragraph_1": "초점 거리가 이제 다른 촬영 데이터와 함께 사이드바에 표시됩니다. DNG, JPG 또는 TIFF로 내보낼 때 이 값이 EXIF 메타데이터의 Subject Distance 필드에 기록됩니다. 앱은 또한 초점 거리와 프레임에 사용된 초점 거리를 결합하여 Subject Distance Range를 계산하여 이미지 뷰어와 카탈로그 소프트웨어에 촬영에 대한 더 많은 정보를 제공합니다.",
        "paragraph_2": "이 기능은 Frames for iOS(버전 1.21.0 이상)에서 기록된 초점 거리 데이터와 함께 작동합니다. 휴대폰에서 초점 거리를 기록했다면 해당 정보가 이제 Mac에서 내보낸 파일로 전달됩니다.",
        "improvements": [
            "사이드바에 초점 거리 표시",
            "DNG, JPG, TIFF 내보내기 시 Subject Distance를 EXIF 메타데이터에 기록",
            "초점 거리와 초점 거리에서 Subject Distance Range 계산",
            "Flash Off가 건너뛰지 않고 메타데이터에 기록됨",
            "0 EV 노출 보정이 건너뛰지 않고 메타데이터에 기록됨",
            "사이드바 모양을 포함한 macOS Sequoia용 시각적 개선"
        ]
    },
    "nb": {
        "title": "Fokusavstand i sidefelt og EXIF",
        "meta_title": "Fokusavstand i sidefelt og EXIF - Frames",
        "meta_description": "Fokusavstand vises nå i sidefeltet og skrives til EXIF-metadata. Subject Distance Range beregnes automatisk.",
        "summary": "Denne oppdateringen bringer støtte for fokusavstand til Mac-appen. Hvis du registrerer fokusavstand i Frames for iOS, vises disse dataene nå i sidefeltet og skrives til EXIF-metadata når du eksporterer skanningene dine. Oppdateringen forbedrer også håndteringen av visse metadataverdier og inkluderer visuelle forbedringer for macOS Sequoia.",
        "alt": "Frames macOS-app som viser fokusavstand i sidefeltet",
        "heading_1": "Fokusavstand og Subject Distance Range",
        "paragraph_1": "Fokusavstand er nå synlig i sidefeltet sammen med de andre opptaksdataene dine. Når du eksporterer til DNG, JPG eller TIFF, skrives denne verdien til Subject Distance-feltet i EXIF-metadata. Appen beregner også et Subject Distance Range ved å kombinere fokusavstanden med brennvidden du brukte for rammen, noe som gir bildevisere og katalogiseringsprogramvare mer kontekst om bildet ditt.",
        "paragraph_2": "Denne funksjonen fungerer med fokusavstandsdata registrert i Frames for iOS (versjon 1.21.0 og senere). Hvis du har logget fokusavstand på telefonen din, overføres denne informasjonen nå til de eksporterte filene dine på Mac.",
        "improvements": [
            "Fokusavstand vises i sidefeltet",
            "Subject Distance skrives til EXIF-metadata for DNG-, JPG- og TIFF-eksporter",
            "Subject Distance Range beregnes fra fokusavstand og brennvidde",
            "Flash Off skrives nå til metadata i stedet for å hoppes over",
            "0 EV eksponeringskompensasjon skrives nå til metadata i stedet for å hoppes over",
            "Visuelle forbedringer for macOS Sequoia, inkludert sidefeltets utseende"
        ]
    },
    "nl": {
        "title": "Scherpstelafstand in zijbalk en EXIF",
        "meta_title": "Scherpstelafstand in zijbalk en EXIF - Frames",
        "meta_description": "Scherpstelafstand verschijnt nu in de zijbalk en wordt naar EXIF-metadata geschreven. Subject Distance Range wordt automatisch berekend.",
        "summary": "Deze update brengt ondersteuning voor scherpstelafstand naar de Mac-app. Als je scherpstelafstand vastlegt in Frames voor iOS, verschijnen die gegevens nu in de zijbalk en worden ze naar de EXIF-metadata geschreven wanneer je je scans exporteert. De update verbetert ook de verwerking van bepaalde metadatawaarden en bevat visuele verfijningen voor macOS Sequoia.",
        "alt": "Frames macOS-app toont scherpstelafstand in de zijbalk",
        "heading_1": "Scherpstelafstand en Subject Distance Range",
        "paragraph_1": "Scherpstelafstand is nu zichtbaar in de zijbalk naast je andere opnamegegevens. Bij het exporteren naar DNG, JPG of TIFF wordt deze waarde naar het Subject Distance-veld in de EXIF-metadata geschreven. De app berekent ook een Subject Distance Range door de scherpstelafstand te combineren met de brandpuntafstand die je voor de filmframe hebt gebruikt, waardoor beeldviewers en catalogussoftware meer context over je opname krijgen.",
        "paragraph_2": "Deze functie werkt met scherpstelafstandgegevens die zijn vastgelegd in Frames voor iOS (versie 1.21.0 en later). Als je scherpstelafstand op je telefoon hebt geregistreerd, wordt die informatie nu overgebracht naar je geëxporteerde bestanden op Mac.",
        "improvements": [
            "Scherpstelafstand weergegeven in zijbalk",
            "Subject Distance geschreven naar EXIF-metadata voor DNG-, JPG- en TIFF-exports",
            "Subject Distance Range berekend uit scherpstelafstand en brandpuntafstand",
            "Flash Off wordt nu naar metadata geschreven in plaats van overgeslagen",
            "0 EV belichtingscorrectie wordt nu naar metadata geschreven in plaats van overgeslagen",
            "Visuele verfijningen voor macOS Sequoia, inclusief het uiterlijk van de zijbalk"
        ]
    },
    "pl": {
        "title": "Odległość ostrości w pasku bocznym i EXIF",
        "meta_title": "Odległość ostrości w pasku bocznym i EXIF - Frames",
        "meta_description": "Odległość ostrości pojawia się teraz w pasku bocznym i jest zapisywana w metadanych EXIF. Subject Distance Range jest obliczany automatycznie.",
        "summary": "Ta aktualizacja wprowadza obsługę odległości ostrości do aplikacji Mac. Jeśli rejestrujesz odległość ostrości w Frames dla iOS, te dane pojawiają się teraz w pasku bocznym i są zapisywane w metadanych EXIF podczas eksportowania skanów. Aktualizacja poprawia również obsługę niektórych wartości metadanych i zawiera ulepszenia wizualne dla macOS Sequoia.",
        "alt": "Aplikacja Frames macOS pokazująca odległość ostrości w pasku bocznym",
        "heading_1": "Odległość ostrości i Subject Distance Range",
        "paragraph_1": "Odległość ostrości jest teraz widoczna w pasku bocznym obok innych danych fotografowania. Podczas eksportu do DNG, JPG lub TIFF ta wartość jest zapisywana w polu Subject Distance metadanych EXIF. Aplikacja oblicza również Subject Distance Range, łącząc odległość ostrości z ogniskową użytą dla klatki, dając przeglądarkom obrazów i oprogramowaniu katalogującemu więcej kontekstu o Twoim zdjęciu.",
        "paragraph_2": "Ta funkcja działa z danymi odległości ostrości zarejestrowanymi w Frames dla iOS (wersja 1.21.0 i nowsze). Jeśli rejestrowałeś odległość ostrości na telefonie, te informacje są teraz przenoszone do eksportowanych plików na Macu.",
        "improvements": [
            "Odległość ostrości wyświetlana w pasku bocznym",
            "Subject Distance zapisywana w metadanych EXIF dla eksportów DNG, JPG i TIFF",
            "Subject Distance Range obliczana z odległości ostrości i ogniskowej",
            "Flash Off jest teraz zapisywany w metadanych zamiast być pomijany",
            "Kompensacja ekspozycji 0 EV jest teraz zapisywana w metadanych zamiast być pomijana",
            "Ulepszenia wizualne dla macOS Sequoia, w tym wygląd paska bocznego"
        ]
    },
    "pt": {
        "title": "Distância de focagem na barra lateral e EXIF",
        "meta_title": "Distância de focagem na barra lateral e EXIF - Frames",
        "meta_description": "A distância de focagem aparece agora na barra lateral e é escrita nos metadados EXIF. Subject Distance Range é calculado automaticamente.",
        "summary": "Esta atualização traz suporte de distância de focagem para a app Mac. Se registar a distância de focagem no Frames para iOS, esses dados aparecem agora na barra lateral e são escritos nos metadados EXIF quando exporta as suas digitalizações. A atualização também melhora o tratamento de certos valores de metadados e inclui refinamentos visuais para macOS Sequoia.",
        "alt": "App Frames macOS a mostrar a distância de focagem na barra lateral",
        "heading_1": "Distância de focagem e Subject Distance Range",
        "paragraph_1": "A distância de focagem está agora visível na barra lateral juntamente com os outros dados de disparo. Ao exportar para DNG, JPG ou TIFF, este valor é escrito no campo Subject Distance dos metadados EXIF. A app também calcula um Subject Distance Range combinando a distância de focagem com a distância focal usada para o fotograma, dando aos visualizadores de imagens e software de catalogação mais contexto sobre o seu disparo.",
        "paragraph_2": "Esta funcionalidade trabalha com dados de distância de focagem registados no Frames para iOS (versão 1.21.0 e posteriores). Se tem registado a distância de focagem no seu telefone, essa informação é agora transferida para os ficheiros exportados no Mac.",
        "improvements": [
            "Distância de focagem apresentada na barra lateral",
            "Subject Distance escrito nos metadados EXIF para exportações DNG, JPG e TIFF",
            "Subject Distance Range calculado a partir da distância de focagem e distância focal",
            "Flash Off é agora escrito nos metadados em vez de ser ignorado",
            "Compensação de exposição 0 EV é agora escrita nos metadados em vez de ser ignorada",
            "Refinamentos visuais para macOS Sequoia, incluindo a aparência da barra lateral"
        ]
    },
    "ro": {
        "title": "Distanța de focalizare în bara laterală și EXIF",
        "meta_title": "Distanța de focalizare în bara laterală și EXIF - Frames",
        "meta_description": "Distanța de focalizare apare acum în bara laterală și este scrisă în metadatele EXIF. Subject Distance Range este calculat automat.",
        "summary": "Această actualizare aduce suport pentru distanța de focalizare în aplicația Mac. Dacă înregistrezi distanța de focalizare în Frames pentru iOS, acele date apar acum în bara laterală și sunt scrise în metadatele EXIF când exporti scanările. Actualizarea îmbunătățește și gestionarea anumitor valori de metadate și include îmbunătățiri vizuale pentru macOS Sequoia.",
        "alt": "Aplicația Frames macOS afișând distanța de focalizare în bara laterală",
        "heading_1": "Distanța de focalizare și Subject Distance Range",
        "paragraph_1": "Distanța de focalizare este acum vizibilă în bara laterală alături de celelalte date de fotografiere. Când exporti în DNG, JPG sau TIFF, această valoare este scrisă în câmpul Subject Distance din metadatele EXIF. Aplicația calculează și un Subject Distance Range combinând distanța de focalizare cu distanța focală folosită pentru cadru, oferind vizualizatoarelor de imagini și software-ului de catalogare mai mult context despre fotografia ta.",
        "paragraph_2": "Această funcție funcționează cu datele de distanță de focalizare înregistrate în Frames pentru iOS (versiunea 1.21.0 și ulterior). Dacă ai înregistrat distanța de focalizare pe telefon, acele informații sunt acum transferate în fișierele exportate pe Mac.",
        "improvements": [
            "Distanța de focalizare afișată în bara laterală",
            "Subject Distance scris în metadatele EXIF pentru exporturile DNG, JPG și TIFF",
            "Subject Distance Range calculat din distanța de focalizare și distanța focală",
            "Flash Off este acum scris în metadate în loc să fie omis",
            "Compensarea expunerii 0 EV este acum scrisă în metadate în loc să fie omisă",
            "Îmbunătățiri vizuale pentru macOS Sequoia, inclusiv aspectul barei laterale"
        ]
    },
    "ru": {
        "title": "Дистанция фокусировки в боковой панели и EXIF",
        "meta_title": "Дистанция фокусировки в боковой панели и EXIF - Frames",
        "meta_description": "Дистанция фокусировки теперь отображается в боковой панели и записывается в метаданные EXIF. Subject Distance Range рассчитывается автоматически.",
        "summary": "Это обновление добавляет поддержку дистанции фокусировки в приложение для Mac. Если вы записываете дистанцию фокусировки в Frames для iOS, эти данные теперь отображаются в боковой панели и записываются в метаданные EXIF при экспорте сканов. Обновление также улучшает обработку некоторых значений метаданных и включает визуальные улучшения для macOS Sequoia.",
        "alt": "Приложение Frames macOS показывает дистанцию фокусировки в боковой панели",
        "heading_1": "Дистанция фокусировки и Subject Distance Range",
        "paragraph_1": "Дистанция фокусировки теперь отображается в боковой панели вместе с другими данными съёмки. При экспорте в DNG, JPG или TIFF это значение записывается в поле Subject Distance метаданных EXIF. Приложение также рассчитывает Subject Distance Range, комбинируя дистанцию фокусировки с фокусным расстоянием, использованным для кадра, предоставляя просмотрщикам изображений и программам каталогизации больше информации о вашем снимке.",
        "paragraph_2": "Эта функция работает с данными дистанции фокусировки, записанными в Frames для iOS (версия 1.21.0 и выше). Если вы записывали дистанцию фокусировки на телефоне, эта информация теперь переносится в экспортированные файлы на Mac.",
        "improvements": [
            "Дистанция фокусировки отображается в боковой панели",
            "Subject Distance записывается в метаданные EXIF при экспорте в DNG, JPG и TIFF",
            "Subject Distance Range рассчитывается из дистанции фокусировки и фокусного расстояния",
            "Flash Off теперь записывается в метаданные вместо пропуска",
            "Экспокоррекция 0 EV теперь записывается в метаданные вместо пропуска",
            "Визуальные улучшения для macOS Sequoia, включая внешний вид боковой панели"
        ]
    },
    "sv": {
        "title": "Fokusavstånd i sidofält och EXIF",
        "meta_title": "Fokusavstånd i sidofält och EXIF - Frames",
        "meta_description": "Fokusavstånd visas nu i sidofältet och skrivs till EXIF-metadata. Subject Distance Range beräknas automatiskt.",
        "summary": "Denna uppdatering ger stöd för fokusavstånd i Mac-appen. Om du registrerar fokusavstånd i Frames för iOS visas dessa data nu i sidofältet och skrivs till EXIF-metadata när du exporterar dina skanningar. Uppdateringen förbättrar också hanteringen av vissa metadatavärden och inkluderar visuella förbättringar för macOS Sequoia.",
        "alt": "Frames macOS-app som visar fokusavstånd i sidofältet",
        "heading_1": "Fokusavstånd och Subject Distance Range",
        "paragraph_1": "Fokusavstånd syns nu i sidofältet tillsammans med dina andra fotograferingsdata. När du exporterar till DNG, JPG eller TIFF skrivs detta värde till Subject Distance-fältet i EXIF-metadata. Appen beräknar också ett Subject Distance Range genom att kombinera fokusavståndet med den brännvidd du använde för rutan, vilket ger bildvisare och katalogiseringsprogram mer sammanhang om din bild.",
        "paragraph_2": "Denna funktion fungerar med fokusavståndsdata som registrerats i Frames för iOS (version 1.21.0 och senare). Om du har loggat fokusavstånd på din telefon överförs den informationen nu till dina exporterade filer på Mac.",
        "improvements": [
            "Fokusavstånd visas i sidofältet",
            "Subject Distance skrivs till EXIF-metadata för DNG-, JPG- och TIFF-exporter",
            "Subject Distance Range beräknas från fokusavstånd och brännvidd",
            "Flash Off skrivs nu till metadata istället för att hoppas över",
            "0 EV exponeringskompensation skrivs nu till metadata istället för att hoppas över",
            "Visuella förbättringar för macOS Sequoia, inklusive sidofältets utseende"
        ]
    },
    "th": {
        "title": "ระยะโฟกัสในแถบด้านข้างและ EXIF",
        "meta_title": "ระยะโฟกัสในแถบด้านข้างและ EXIF - Frames",
        "meta_description": "ระยะโฟกัสแสดงในแถบด้านข้างและเขียนลงในเมตาดาต้า EXIF แล้ว Subject Distance Range คำนวณอัตโนมัติ",
        "summary": "การอัปเดตนี้นำการสนับสนุนระยะโฟกัสมาสู่แอป Mac หากคุณบันทึกระยะโฟกัสใน Frames สำหรับ iOS ข้อมูลนั้นจะแสดงในแถบด้านข้างและเขียนลงในเมตาดาต้า EXIF เมื่อคุณส่งออกไฟล์สแกน การอัปเดตยังปรับปรุงการจัดการค่าเมตาดาต้าบางอย่างและรวมถึงการปรับปรุงภาพสำหรับ macOS Sequoia",
        "alt": "แอป Frames macOS แสดงระยะโฟกัสในแถบด้านข้าง",
        "heading_1": "ระยะโฟกัสและ Subject Distance Range",
        "paragraph_1": "ระยะโฟกัสแสดงในแถบด้านข้างพร้อมกับข้อมูลการถ่ายภาพอื่นๆ ของคุณแล้ว เมื่อส่งออกเป็น DNG, JPG หรือ TIFF ค่านี้จะถูกเขียนลงในฟิลด์ Subject Distance ของเมตาดาต้า EXIF แอปยังคำนวณ Subject Distance Range โดยรวมระยะโฟกัสกับทางยาวโฟกัสที่คุณใช้สำหรับเฟรม ให้โปรแกรมดูภาพและซอฟต์แวร์จัดหมวดหมู่มีบริบทมากขึ้นเกี่ยวกับภาพของคุณ",
        "paragraph_2": "ฟีเจอร์นี้ทำงานกับข้อมูลระยะโฟกัสที่บันทึกใน Frames สำหรับ iOS (เวอร์ชัน 1.21.0 ขึ้นไป) หากคุณบันทึกระยะโฟกัสบนโทรศัพท์ ข้อมูลนั้นจะถูกส่งต่อไปยังไฟล์ที่ส่งออกบน Mac",
        "improvements": [
            "ระยะโฟกัสแสดงในแถบด้านข้าง",
            "Subject Distance เขียนลงในเมตาดาต้า EXIF สำหรับการส่งออก DNG, JPG และ TIFF",
            "Subject Distance Range คำนวณจากระยะโฟกัสและทางยาวโฟกัส",
            "Flash Off เขียนลงในเมตาดาต้าแทนที่จะถูกข้าม",
            "ค่าชดเชยแสง 0 EV เขียนลงในเมตาดาต้าแทนที่จะถูกข้าม",
            "การปรับปรุงภาพสำหรับ macOS Sequoia รวมถึงรูปลักษณ์แถบด้านข้าง"
        ]
    },
    "tr": {
        "title": "Kenar çubuğu ve EXIF'te odak mesafesi",
        "meta_title": "Kenar çubuğu ve EXIF'te odak mesafesi - Frames",
        "meta_description": "Odak mesafesi artık kenar çubuğunda görünüyor ve EXIF meta verilerine yazılıyor. Subject Distance Range otomatik hesaplanıyor.",
        "summary": "Bu güncelleme Mac uygulamasına odak mesafesi desteği getiriyor. iOS için Frames'te odak mesafesi kaydediyorsanız, bu veriler artık kenar çubuğunda görünüyor ve taramalarınızı dışa aktardığınızda EXIF meta verilerine yazılıyor. Güncelleme ayrıca belirli meta veri değerlerinin işlenmesini iyileştiriyor ve macOS Sequoia için görsel iyileştirmeler içeriyor.",
        "alt": "Frames macOS uygulaması kenar çubuğunda odak mesafesini gösteriyor",
        "heading_1": "Odak mesafesi ve Subject Distance Range",
        "paragraph_1": "Odak mesafesi artık diğer çekim verilerinizle birlikte kenar çubuğunda görünüyor. DNG, JPG veya TIFF'e dışa aktardığınızda, bu değer EXIF meta verilerinin Subject Distance alanına yazılıyor. Uygulama ayrıca odak mesafesini kare için kullandığınız odak uzaklığıyla birleştirerek Subject Distance Range hesaplıyor ve görüntü görüntüleyicilere ve kataloglama yazılımlarına çekiminiz hakkında daha fazla bağlam sağlıyor.",
        "paragraph_2": "Bu özellik iOS için Frames'te (sürüm 1.21.0 ve sonrası) kaydedilen odak mesafesi verileriyle çalışıyor. Telefonunuzda odak mesafesi kaydettiyseniz, bu bilgi artık Mac'teki dışa aktarılan dosyalarınıza aktarılıyor.",
        "improvements": [
            "Odak mesafesi kenar çubuğunda gösteriliyor",
            "Subject Distance, DNG, JPG ve TIFF dışa aktarımları için EXIF meta verilerine yazılıyor",
            "Subject Distance Range, odak mesafesi ve odak uzaklığından hesaplanıyor",
            "Flash Off artık atlanmak yerine meta verilere yazılıyor",
            "0 EV pozlama telafisi artık atlanmak yerine meta verilere yazılıyor",
            "Kenar çubuğu görünümü dahil macOS Sequoia için görsel iyileştirmeler"
        ]
    },
    "uk": {
        "title": "Дистанція фокусування в бічній панелі та EXIF",
        "meta_title": "Дистанція фокусування в бічній панелі та EXIF - Frames",
        "meta_description": "Дистанція фокусування тепер відображається в бічній панелі та записується в метадані EXIF. Subject Distance Range розраховується автоматично.",
        "summary": "Це оновлення додає підтримку дистанції фокусування в програму для Mac. Якщо ви записуєте дистанцію фокусування у Frames для iOS, ці дані тепер відображаються в бічній панелі та записуються в метадані EXIF під час експорту сканів. Оновлення також покращує обробку деяких значень метаданих та включає візуальні покращення для macOS Sequoia.",
        "alt": "Програма Frames macOS показує дистанцію фокусування в бічній панелі",
        "heading_1": "Дистанція фокусування та Subject Distance Range",
        "paragraph_1": "Дистанція фокусування тепер відображається в бічній панелі разом з іншими даними зйомки. При експорті в DNG, JPG або TIFF це значення записується в поле Subject Distance метаданих EXIF. Програма також розраховує Subject Distance Range, поєднуючи дистанцію фокусування з фокусною відстанню, використаною для кадру, надаючи переглядачам зображень та програмам каталогізації більше контексту про ваш знімок.",
        "paragraph_2": "Ця функція працює з даними дистанції фокусування, записаними у Frames для iOS (версія 1.21.0 і новіші). Якщо ви записували дистанцію фокусування на телефоні, ця інформація тепер переноситься в експортовані файли на Mac.",
        "improvements": [
            "Дистанція фокусування відображається в бічній панелі",
            "Subject Distance записується в метадані EXIF для експорту DNG, JPG і TIFF",
            "Subject Distance Range розраховується з дистанції фокусування та фокусної відстані",
            "Flash Off тепер записується в метадані замість пропуску",
            "Експокорекція 0 EV тепер записується в метадані замість пропуску",
            "Візуальні покращення для macOS Sequoia, включаючи вигляд бічної панелі"
        ]
    },
    "vi": {
        "title": "Khoảng cách lấy nét trong thanh bên và EXIF",
        "meta_title": "Khoảng cách lấy nét trong thanh bên và EXIF - Frames",
        "meta_description": "Khoảng cách lấy nét hiện hiển thị trong thanh bên và được ghi vào siêu dữ liệu EXIF. Subject Distance Range được tính tự động.",
        "summary": "Bản cập nhật này mang hỗ trợ khoảng cách lấy nét đến ứng dụng Mac. Nếu bạn ghi khoảng cách lấy nét trong Frames cho iOS, dữ liệu đó giờ hiển thị trong thanh bên và được ghi vào siêu dữ liệu EXIF khi bạn xuất các bản scan. Bản cập nhật cũng cải thiện cách xử lý một số giá trị siêu dữ liệu và bao gồm các cải tiến giao diện cho macOS Sequoia.",
        "alt": "Ứng dụng Frames macOS hiển thị khoảng cách lấy nét trong thanh bên",
        "heading_1": "Khoảng cách lấy nét và Subject Distance Range",
        "paragraph_1": "Khoảng cách lấy nét giờ hiển thị trong thanh bên cùng với các dữ liệu chụp khác của bạn. Khi xuất sang DNG, JPG hoặc TIFF, giá trị này được ghi vào trường Subject Distance trong siêu dữ liệu EXIF. Ứng dụng cũng tính Subject Distance Range bằng cách kết hợp khoảng cách lấy nét với tiêu cự bạn sử dụng cho khung hình, cung cấp cho trình xem ảnh và phần mềm danh mục thêm ngữ cảnh về bức ảnh của bạn.",
        "paragraph_2": "Tính năng này hoạt động với dữ liệu khoảng cách lấy nét được ghi trong Frames cho iOS (phiên bản 1.21.0 trở lên). Nếu bạn đã ghi khoảng cách lấy nét trên điện thoại, thông tin đó giờ được chuyển sang các tệp xuất trên Mac.",
        "improvements": [
            "Khoảng cách lấy nét hiển thị trong thanh bên",
            "Subject Distance được ghi vào siêu dữ liệu EXIF cho xuất DNG, JPG và TIFF",
            "Subject Distance Range được tính từ khoảng cách lấy nét và tiêu cự",
            "Flash Off giờ được ghi vào siêu dữ liệu thay vì bị bỏ qua",
            "Bù phơi sáng 0 EV giờ được ghi vào siêu dữ liệu thay vì bị bỏ qua",
            "Cải tiến giao diện cho macOS Sequoia, bao gồm giao diện thanh bên"
        ]
    },
    "zh": {
        "title": "侧边栏和 EXIF 中的对焦距离",
        "meta_title": "侧边栏和 EXIF 中的对焦距离 - Frames",
        "meta_description": "对焦距离现在显示在侧边栏中并写入 EXIF 元数据。Subject Distance Range 自动计算",
        "summary": "此更新为 Mac 应用带来了对焦距离支持。如果您在 Frames iOS 版中记录对焦距离,该数据现在会显示在侧边栏中,并在导出扫描文件时写入 EXIF 元数据。此更新还改进了某些元数据值的处理方式,并包含针对 macOS Sequoia 的视觉改进。",
        "alt": "Frames macOS 应用在侧边栏中显示对焦距离",
        "heading_1": "对焦距离和 Subject Distance Range",
        "paragraph_1": "对焦距离现在与其他拍摄数据一起显示在侧边栏中。导出为 DNG、JPG 或 TIFF 时,此值会写入 EXIF 元数据的 Subject Distance 字段。应用还会将对焦距离与帧所用的焦距相结合来计算 Subject Distance Range,为图像查看器和编目软件提供更多关于拍摄的信息。",
        "paragraph_2": "此功能与 Frames iOS 版(1.21.0 及更高版本)中记录的对焦距离数据配合使用。如果您在手机上记录了对焦距离,该信息现在会传递到 Mac 上导出的文件中。",
        "improvements": [
            "侧边栏中显示对焦距离",
            "Subject Distance 写入 DNG、JPG 和 TIFF 导出的 EXIF 元数据",
            "根据对焦距离和焦距计算 Subject Distance Range",
            "Flash Off 现在写入元数据而不是被跳过",
            "0 EV 曝光补偿现在写入元数据而不是被跳过",
            "针对 macOS Sequoia 的视觉改进,包括侧边栏外观"
        ]
    },
    "zh-hant": {
        "title": "側邊欄和 EXIF 中的對焦距離",
        "meta_title": "側邊欄和 EXIF 中的對焦距離 - Frames",
        "meta_description": "對焦距離現在顯示在側邊欄中並寫入 EXIF 中繼資料。Subject Distance Range 自動計算",
        "summary": "此更新為 Mac 應用程式帶來了對焦距離支援。如果您在 Frames iOS 版中記錄對焦距離,該資料現在會顯示在側邊欄中,並在輸出掃描檔案時寫入 EXIF 中繼資料。此更新還改進了某些中繼資料值的處理方式,並包含針對 macOS Sequoia 的視覺改進。",
        "alt": "Frames macOS 應用程式在側邊欄中顯示對焦距離",
        "heading_1": "對焦距離和 Subject Distance Range",
        "paragraph_1": "對焦距離現在與其他拍攝資料一起顯示在側邊欄中。輸出為 DNG、JPG 或 TIFF 時,此值會寫入 EXIF 中繼資料的 Subject Distance 欄位。應用程式還會將對焦距離與畫格所用的焦距相結合來計算 Subject Distance Range,為影像檢視器和編目軟體提供更多關於拍攝的資訊。",
        "paragraph_2": "此功能與 Frames iOS 版(1.21.0 及更高版本)中記錄的對焦距離資料配合使用。如果您在手機上記錄了對焦距離,該資訊現在會傳遞到 Mac 上輸出的檔案中。",
        "improvements": [
            "側邊欄中顯示對焦距離",
            "Subject Distance 寫入 DNG、JPG 和 TIFF 輸出的 EXIF 中繼資料",
            "根據對焦距離和焦距計算 Subject Distance Range",
            "Flash Off 現在寫入中繼資料而不是被跳過",
            "0 EV 曝光補償現在寫入中繼資料而不是被跳過",
            "針對 macOS Sequoia 的視覺改進,包括側邊欄外觀"
        ]
    }
}


def create_changelog_file(lang_code: str) -> bool:
    """Create a changelog file for the specified language."""

    if lang_code not in TRANSLATIONS:
        print(f"  No translations available for {lang_code}")
        return False

    trans = TRANSLATIONS[lang_code]

    # Build the full structure
    data = {
        **BASE_STRUCTURE,
        "title": trans["title"],
        "meta_title": trans["meta_title"],
        "meta_description": trans["meta_description"],
        "summary": trans["summary"],
        "sections": [
            get_media_section(trans["alt"]),
            {
                "type": "heading",
                "level": 3,
                "content": trans["heading_1"]
            },
            {
                "type": "paragraph",
                "content": trans["paragraph_1"]
            },
            {
                "type": "paragraph",
                "content": trans["paragraph_2"]
            }
        ],
        "improvements": trans["improvements"],
        "fixes": [],
        "patches": []
    }

    # Write the file
    file_path = BASE_PATH / lang_code / "1.13.0-macos.json"

    # Create directory if it doesn't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    return True


def main():
    """Main function to create all language files."""

    print("Creating 1.13.0-macos.json changelog files for all languages...\n")

    # Languages to process (excluding English which already exists)
    languages = [
        "da", "de", "el", "es", "fi", "fr", "hi", "id", "it", "ja", "ko",
        "nb", "nl", "pl", "pt", "ro", "ru", "sv", "th", "tr", "uk", "vi",
        "zh", "zh-hant"
    ]

    created = 0
    errors = 0

    for lang_code in languages:
        print(f"  {lang_code}: ", end="")

        if create_changelog_file(lang_code):
            print("Created")
            created += 1
        else:
            print("Error")
            errors += 1

    print(f"\nDone! Created: {created}, Errors: {errors}")


if __name__ == "__main__":
    main()
