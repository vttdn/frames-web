#!/usr/bin/env python3
"""
Script to create 1.21.0-ios.json changelog files for all supported languages.
Professional translations adapted for film photography terminology.
"""

import json
from pathlib import Path

# Base path for changelog locales
BASE_PATH = Path(__file__).parent.parent / "sources" / "locales" / "changelog"

# Base structure that's the same for all languages
BASE_STRUCTURE = {
    "version": "1.21.0",
    "version_short": "1.21",
    "url_slug": "1-21-ios",
    "platform": "ios",
    "release_date": "2026-01-26T10:00:00.000Z",
}

# Media section (same for all languages except alt text)
def get_media_section(alt_text):
    return {
        "type": "media",
        "image": "/lib/img/shared/changelog/frames-1.21.0-1.png",
        "image_2x": "/lib/img/shared/changelog/frames-1.21.0-1@2x.png",
        "alt": alt_text,
        "width": "400",
        "height": "300"
    }

# All translations
TRANSLATIONS = {
    "da": {
        "title": "Registrering af fokusafstand",
        "meta_title": "Registrering af fokusafstand - Frames",
        "meta_description": "Registrer fokusafstanden for hver ramme i meter eller fod. Data kan bruges med Mac-appen til EXIF-metadata i dine eksporterede scanninger.",
        "summary": "Denne opdatering tilføjer fokusafstand til de data, du kan registrere for hver ramme, så du får et mere komplet billede af dine optageindstillinger. Opdateringen indeholder også flere forbedringer af brugerfladen, der gør det nemmere at indtaste og gennemgå dine rammedata.",
        "alt": "Frames-appen viser registrering af fokusafstand for en ramme",
        "heading_1": "Registrer din fokusafstand",
        "paragraph_1": "Når du logger en ramme, kan du nu registrere fokusafstanden sammen med dine andre optagedata. Uanset om du fokuserede på 1,2 meter til et portræt eller stillede på uendelig til et landskab, gemmes denne information med hvert billede. Appen læser dine iOS-regionindstillinger og viser afstande i meter eller fod efter behov.",
        "paragraph_2": "Hvis du bruger Frames på Mac, kan disse fokusafstandsdata skrives ind i felterne Subject Distance og Subject Distance Range i dine EXIF-metadata ved eksport til DNG, JPG eller TIFF. Dine fokusindstillinger følger med dine scanninger, ligesom blænde og lukkertid.",
        "heading_2": "Forbedringer af brugerfladen",
        "paragraph_3": "Det er nu nemmere at vælge brændviddeværdier, og eksponeringskompensationsvælgeren viser 0 EV i stedet for Ikke indstillet, når der ikke er registreret nogen justering. Parametre vises også i en ensartet rækkefølge på tværs af rammelisten og indstillingerne, så appen er mere forudsigelig at bruge.",
        "improvements": [
            "Registrer fokusafstand for hver ramme med automatisk enhedsvalg baseret på iOS-indstillinger",
            "Nemmere valg ved indtastning af brændviddeværdier",
            "Eksponeringskompensationsvælgeren viser nu 0 EV i stedet for Ikke indstillet",
            "Ensartet parameterrækkefølge i rammelisten og indstillingerne",
            "Diverse forbedringer af brugerfladen"
        ]
    },
    "de": {
        "title": "Aufnahmeentfernung erfassen",
        "meta_title": "Aufnahmeentfernung erfassen - Frames",
        "meta_description": "Erfasse die Aufnahmeentfernung für jedes Einzelbild in Metern oder Fuß. Die Daten können mit der Mac-App in die EXIF-Metadaten geschrieben werden.",
        "summary": "Mit diesem Update kannst du die Aufnahmeentfernung für jedes Einzelbild erfassen und erhältst so ein vollständigeres Bild deiner Aufnahmeeinstellungen. Das Update enthält außerdem mehrere Verbesserungen der Benutzeroberfläche, die das Eingeben und Überprüfen deiner Einzelbilddaten komfortabler machen.",
        "alt": "Frames-App zeigt die Erfassung der Aufnahmeentfernung für ein Einzelbild",
        "heading_1": "Erfasse deine Aufnahmeentfernung",
        "paragraph_1": "Beim Erfassen eines Einzelbilds kannst du jetzt die Aufnahmeentfernung zusammen mit deinen anderen Aufnahmedaten speichern. Ob du auf 1,2 Meter für ein Porträt fokussiert hast oder auf Unendlich für eine Landschaft – diese Information wird mit jeder Aufnahme gespeichert. Die App liest deine iOS-Regionseinstellungen und zeigt Entfernungen entsprechend in Metern oder Fuß an.",
        "paragraph_2": "Wenn du Frames auf dem Mac verwendest, können diese Entfernungsdaten beim Export in DNG, JPG oder TIFF in die EXIF-Felder «Aufnahmeentfernung» und «Aufnahmeentfernungsbereich» geschrieben werden. Deine Fokuseinstellungen bleiben so bei deinen Scans erhalten, genau wie Blende und Verschlusszeit.",
        "heading_2": "Verbesserungen der Benutzeroberfläche",
        "paragraph_3": "Die Auswahl von Brennweitenwerten ist jetzt einfacher, und die Belichtungskorrekturauswahl zeigt 0 EV anstelle von Nicht festgelegt an, wenn keine Anpassung erfasst wurde. Parameter werden außerdem in einer einheitlichen Reihenfolge in der Einzelbildliste und den Einstellungen angezeigt, was die App vorhersehbarer macht.",
        "improvements": [
            "Aufnahmeentfernung für jedes Einzelbild erfassen mit automatischer Einheitenauswahl basierend auf iOS-Einstellungen",
            "Einfachere Auswahl bei der Eingabe von Brennweitenwerten",
            "Belichtungskorrekturauswahl zeigt jetzt 0 EV statt Nicht festgelegt",
            "Einheitliche Parameterreihenfolge in der Einzelbildliste und den Einstellungen",
            "Diverse Verbesserungen der Benutzeroberfläche"
        ]
    },
    "el": {
        "title": "Καταγραφή απόστασης εστίασης",
        "meta_title": "Καταγραφή απόστασης εστίασης - Frames",
        "meta_description": "Καταγράψτε την απόσταση εστίασης για κάθε καρέ σε μέτρα ή πόδια. Τα δεδομένα ενσωματώνονται με την εφαρμογή Mac για μεταδεδομένα EXIF.",
        "summary": "Αυτή η ενημέρωση προσθέτει την απόσταση εστίασης στα δεδομένα που μπορείτε να καταγράψετε για κάθε καρέ, δίνοντάς σας μια πιο ολοκληρωμένη εικόνα των ρυθμίσεων λήψης. Η ενημέρωση περιλαμβάνει επίσης αρκετές βελτιώσεις διεπαφής που κάνουν την εισαγωγή και την ανασκόπηση των δεδομένων καρέ πιο βολική.",
        "alt": "Η εφαρμογή Frames δείχνει την καταγραφή απόστασης εστίασης για ένα καρέ",
        "heading_1": "Καταγράψτε την απόσταση εστίασης",
        "paragraph_1": "Κατά την καταγραφή ενός καρέ, μπορείτε τώρα να αποθηκεύσετε την απόσταση εστίασης μαζί με τα υπόλοιπα δεδομένα λήψης. Είτε εστιάσατε στα 1,2 μέτρα για ένα πορτρέτο είτε στο άπειρο για ένα τοπίο, αυτή η πληροφορία αποθηκεύεται με κάθε λήψη. Η εφαρμογή διαβάζει τις περιφερειακές ρυθμίσεις του iOS και εμφανίζει τις αποστάσεις σε μέτρα ή πόδια ανάλογα.",
        "paragraph_2": "Αν χρησιμοποιείτε το Frames σε Mac, αυτά τα δεδομένα απόστασης εστίασης μπορούν να εγγραφούν στα πεδία Subject Distance και Subject Distance Range των μεταδεδομένων EXIF κατά την εξαγωγή σε DNG, JPG ή TIFF. Οι ρυθμίσεις εστίασης παραμένουν με τις σαρώσεις σας, όπως το διάφραγμα και η ταχύτητα κλείστρου.",
        "heading_2": "Βελτιώσεις διεπαφής",
        "paragraph_3": "Η επιλογή τιμών εστιακής απόστασης είναι τώρα ευκολότερη και ο επιλογέας αντιστάθμισης έκθεσης εμφανίζει 0 EV αντί για Δεν ορίστηκε όταν δεν έχει καταγραφεί προσαρμογή. Οι παράμετροι εμφανίζονται επίσης με συνεπή σειρά στη λίστα καρέ και στις ρυθμίσεις, κάνοντας την εφαρμογή πιο προβλέψιμη στη χρήση.",
        "improvements": [
            "Καταγραφή απόστασης εστίασης για κάθε καρέ με αυτόματη επιλογή μονάδας βάσει ρυθμίσεων iOS",
            "Ευκολότερη επιλογή κατά την εισαγωγή τιμών εστιακής απόστασης",
            "Ο επιλογέας αντιστάθμισης έκθεσης εμφανίζει τώρα 0 EV αντί για Δεν ορίστηκε",
            "Συνεπής σειρά παραμέτρων στη λίστα καρέ και τις ρυθμίσεις",
            "Διάφορες βελτιώσεις διεπαφής"
        ]
    },
    "es": {
        "title": "Registro de distancia de enfoque",
        "meta_title": "Registro de distancia de enfoque - Frames",
        "meta_description": "Registra la distancia de enfoque de cada fotograma en metros o pies. Los datos se integran con la app de Mac para metadatos EXIF en tus escaneos.",
        "summary": "Esta actualización añade la distancia de enfoque a los datos que puedes registrar para cada fotograma, ofreciéndote una imagen más completa de tus ajustes de disparo. La actualización también incluye varias mejoras de interfaz que hacen más cómodo introducir y revisar los datos de tus fotogramas.",
        "alt": "La app Frames mostrando el registro de distancia de enfoque para un fotograma",
        "heading_1": "Registra tu distancia de enfoque",
        "paragraph_1": "Al registrar un fotograma, ahora puedes guardar la distancia de enfoque junto con el resto de datos de disparo. Ya sea que hayas enfocado a 1,2 metros para un retrato o a infinito para un paisaje, esta información se guarda con cada toma. La app lee tus ajustes regionales de iOS y muestra las distancias en metros o pies según corresponda.",
        "paragraph_2": "Si usas Frames en Mac, estos datos de distancia de enfoque pueden escribirse en los campos Subject Distance y Subject Distance Range de los metadatos EXIF al exportar a DNG, JPG o TIFF. Tus ajustes de enfoque permanecen con tus escaneos, igual que la apertura y la velocidad de obturación.",
        "heading_2": "Mejoras de interfaz",
        "paragraph_3": "Seleccionar valores de distancia focal ahora es más fácil, y el selector de compensación de exposición muestra 0 EV en lugar de No establecido cuando no se ha registrado ningún ajuste. Los parámetros también aparecen en un orden consistente en la lista de fotogramas y en los ajustes, haciendo la app más predecible de usar.",
        "improvements": [
            "Registra la distancia de enfoque para cada fotograma con selección automática de unidad según los ajustes de iOS",
            "Selección más fácil al introducir valores de distancia focal",
            "El selector de compensación de exposición ahora muestra 0 EV en lugar de No establecido",
            "Orden de parámetros consistente en la lista de fotogramas y los ajustes",
            "Varias mejoras de interfaz"
        ]
    },
    "fi": {
        "title": "Tarkennusetäisyyden tallennus",
        "meta_title": "Tarkennusetäisyyden tallennus - Frames",
        "meta_description": "Tallenna tarkennusetäisyys jokaiselle kehykselle metreinä tai jalkoina. Tiedot voidaan kirjoittaa EXIF-metatietoihin Mac-sovelluksella.",
        "summary": "Tämä päivitys lisää tarkennusetäisyyden tietoihin, joita voit tallentaa jokaiselle kehykselle, antaen sinulle kattavamman kuvan kuvausasetuksistasi. Päivitys sisältää myös useita käyttöliittymäparannuksia, jotka tekevät kehystietojen syöttämisestä ja tarkistamisesta kätevämpää.",
        "alt": "Frames-sovellus näyttää tarkennusetäisyyden tallennuksen kehykselle",
        "heading_1": "Tallenna tarkennusetäisyys",
        "paragraph_1": "Kehystä kirjatessasi voit nyt tallentaa tarkennusetäisyyden muiden kuvaustietojen ohella. Olitpa tarkentanut 1,2 metriin muotokuvaa varten tai äärettömään maisemaa varten, tämä tieto tallennetaan jokaisen kuvan mukana. Sovellus lukee iOS-alueasetuksesi ja näyttää etäisyydet metreinä tai jalkoina sen mukaisesti.",
        "paragraph_2": "Jos käytät Framesia Macilla, nämä tarkennusetäisyystiedot voidaan kirjoittaa EXIF-metatietojen Subject Distance- ja Subject Distance Range -kenttiin vietäessä DNG-, JPG- tai TIFF-muotoon. Tarkennusasetuksesi säilyvät skannauksissasi, aivan kuten aukko ja suljinaika.",
        "heading_2": "Käyttöliittymäparannukset",
        "paragraph_3": "Polttovälin arvojen valitseminen on nyt helpompaa, ja valotuksen korjauksen valitsin näyttää 0 EV Ei asetettu -tekstin sijaan, kun säätöä ei ole tallennettu. Parametrit näkyvät myös yhtenäisessä järjestyksessä kehysluettelossa ja asetuksissa, mikä tekee sovelluksesta ennakoitavamman.",
        "improvements": [
            "Tallenna tarkennusetäisyys jokaiselle kehykselle automaattisella yksikön valinnalla iOS-asetusten perusteella",
            "Helpompi valinta polttovälin arvoja syötettäessä",
            "Valotuksen korjauksen valitsin näyttää nyt 0 EV Ei asetettu -tekstin sijaan",
            "Yhtenäinen parametrien järjestys kehysluettelossa ja asetuksissa",
            "Useita käyttöliittymäparannuksia"
        ]
    },
    "fr": {
        "title": "Enregistrement de la distance de mise au point",
        "meta_title": "Enregistrement de la distance de mise au point - Frames",
        "meta_description": "Enregistrez la distance de mise au point pour chaque frame en mètres ou en pieds. Intégration avec l'app Mac pour les métadonnées EXIF.",
        "summary": "Cette mise à jour ajoute la distance de mise au point aux données que vous pouvez enregistrer pour chaque frame, vous donnant une image plus complète de vos réglages de prise de vue. Elle comprend également plusieurs améliorations d'interface qui rendent la saisie et la consultation des données de vos frames plus pratiques.",
        "alt": "L'app Frames affichant l'enregistrement de la distance de mise au point pour une frame",
        "heading_1": "Enregistrez votre distance de mise au point",
        "paragraph_1": "Lors de l'enregistrement d'une frame, vous pouvez maintenant sauvegarder la distance de mise au point avec vos autres données de prise de vue. Que vous ayez fait la mise au point à 1,2 mètre pour un portrait ou à l'infini pour un paysage, cette information est conservée avec chaque photo. L'app lit vos réglages régionaux iOS et affiche les distances en mètres ou en pieds en conséquence.",
        "paragraph_2": "Si vous utilisez Frames sur Mac, ces données de distance peuvent être inscrites dans les champs Subject Distance et Subject Distance Range des métadonnées EXIF lors de l'exportation en DNG, JPG ou TIFF. Vos réglages de mise au point accompagnent vos scans, tout comme l'ouverture et la vitesse d'obturation.",
        "heading_2": "Améliorations de l'interface",
        "paragraph_3": "La sélection des valeurs de focale est maintenant plus facile, et le sélecteur de correction d'exposition affiche 0 EV au lieu de Non défini lorsqu'aucun ajustement n'a été enregistré. Les paramètres apparaissent également dans un ordre cohérent dans la liste des frames et les réglages, rendant l'app plus prévisible à utiliser.",
        "improvements": [
            "Enregistrez la distance de mise au point pour chaque frame avec sélection automatique de l'unité selon les réglages iOS",
            "Sélection plus facile lors de la saisie des valeurs de focale",
            "Le sélecteur de correction d'exposition affiche maintenant 0 EV au lieu de Non défini",
            "Ordre des paramètres cohérent dans la liste des frames et les réglages",
            "Diverses améliorations de l'interface"
        ]
    },
    "hi": {
        "title": "फोकस दूरी रिकॉर्डिंग",
        "meta_title": "फोकस दूरी रिकॉर्डिंग - Frames",
        "meta_description": "प्रत्येक फ्रेम के लिए मीटर या फीट में फोकस दूरी रिकॉर्ड करें। Mac ऐप के साथ EXIF मेटाडेटा के लिए डेटा एकीकृत होता है।",
        "summary": "यह अपडेट फोकस दूरी को उन डेटा में जोड़ता है जो आप प्रत्येक फ्रेम के लिए रिकॉर्ड कर सकते हैं, जिससे आपको अपनी शूटिंग सेटिंग्स की अधिक संपूर्ण तस्वीर मिलती है। इस अपडेट में कई इंटरफ़ेस सुधार भी शामिल हैं जो आपके फ्रेम डेटा को दर्ज करना और समीक्षा करना अधिक सुविधाजनक बनाते हैं।",
        "alt": "Frames ऐप एक फ्रेम के लिए फोकस दूरी रिकॉर्डिंग दिखा रहा है",
        "heading_1": "अपनी फोकस दूरी ट्रैक करें",
        "paragraph_1": "फ्रेम लॉग करते समय, अब आप अपने अन्य शूटिंग डेटा के साथ फोकस दूरी भी रिकॉर्ड कर सकते हैं। चाहे आपने पोर्ट्रेट के लिए 1.2 मीटर पर फोकस किया हो या लैंडस्केप के लिए इन्फिनिटी पर सेट किया हो, यह जानकारी प्रत्येक शॉट के साथ सहेजी जाती है। ऐप आपकी iOS क्षेत्रीय सेटिंग्स पढ़ता है और तदनुसार मीटर या फीट में दूरियां दिखाता है।",
        "paragraph_2": "यदि आप Mac पर Frames का उपयोग करते हैं, तो DNG, JPG या TIFF में निर्यात करते समय यह फोकस दूरी डेटा EXIF मेटाडेटा के Subject Distance और Subject Distance Range फ़ील्ड में लिखा जा सकता है। आपकी फोकस सेटिंग्स आपके स्कैन के साथ रहती हैं, जैसे एपर्चर और शटर स्पीड।",
        "heading_2": "इंटरफ़ेस सुधार",
        "paragraph_3": "फोकल लेंथ वैल्यू चुनना अब आसान है, और एक्सपोज़र कंपेंसेशन पिकर जब कोई एडजस्टमेंट रिकॉर्ड नहीं होता तो सेट नहीं के बजाय 0 EV दिखाता है। फ्रेम लिस्ट और सेटिंग्स में पैरामीटर एक सुसंगत क्रम में भी दिखाई देते हैं, जिससे ऐप का उपयोग अधिक अनुमानित हो जाता है।",
        "improvements": [
            "iOS सेटिंग्स के आधार पर स्वचालित यूनिट चयन के साथ प्रत्येक फ्रेम के लिए फोकस दूरी रिकॉर्ड करें",
            "फोकल लेंथ वैल्यू दर्ज करते समय आसान चयन",
            "एक्सपोज़र कंपेंसेशन पिकर अब सेट नहीं के बजाय 0 EV दिखाता है",
            "फ्रेम लिस्ट और सेटिंग्स में सुसंगत पैरामीटर क्रम",
            "विभिन्न इंटरफ़ेस सुधार"
        ]
    },
    "id": {
        "title": "Perekaman jarak fokus",
        "meta_title": "Perekaman jarak fokus - Frames",
        "meta_description": "Rekam jarak fokus untuk setiap frame dalam meter atau kaki. Data terintegrasi dengan app Mac untuk metadata EXIF pada hasil scan.",
        "summary": "Pembaruan ini menambahkan jarak fokus ke data yang dapat Anda rekam untuk setiap frame, memberikan gambaran lebih lengkap tentang pengaturan pemotretan Anda. Pembaruan ini juga mencakup beberapa perbaikan antarmuka yang membuat memasukkan dan meninjau data frame Anda lebih nyaman.",
        "alt": "Aplikasi Frames menampilkan perekaman jarak fokus untuk sebuah frame",
        "heading_1": "Lacak jarak fokus Anda",
        "paragraph_1": "Saat mencatat frame, Anda sekarang dapat merekam jarak fokus bersama data pemotretan lainnya. Baik Anda fokus pada 1,2 meter untuk potret atau diatur ke tak terhingga untuk lanskap, informasi ini disimpan dengan setiap jepretan. Aplikasi membaca pengaturan regional iOS Anda dan menampilkan jarak dalam meter atau kaki sesuai preferensi.",
        "paragraph_2": "Jika Anda menggunakan Frames di Mac, data jarak fokus ini dapat ditulis ke bidang Subject Distance dan Subject Distance Range pada metadata EXIF saat mengekspor ke DNG, JPG, atau TIFF. Pengaturan fokus Anda tetap menyertai hasil scan, seperti halnya apertur dan kecepatan rana.",
        "heading_2": "Perbaikan antarmuka",
        "paragraph_3": "Memilih nilai panjang fokus sekarang lebih mudah, dan pemilih kompensasi eksposur menampilkan 0 EV alih-alih Tidak Diatur saat tidak ada penyesuaian yang direkam. Parameter juga muncul dalam urutan yang konsisten di seluruh daftar frame dan pengaturan, membuat aplikasi lebih mudah diprediksi.",
        "improvements": [
            "Rekam jarak fokus untuk setiap frame dengan pemilihan unit otomatis berdasarkan pengaturan iOS",
            "Pemilihan lebih mudah saat memasukkan nilai panjang fokus",
            "Pemilih kompensasi eksposur sekarang menampilkan 0 EV alih-alih Tidak Diatur",
            "Urutan parameter konsisten di daftar frame dan pengaturan",
            "Berbagai perbaikan antarmuka"
        ]
    },
    "it": {
        "title": "Registrazione della distanza di messa a fuoco",
        "meta_title": "Registrazione della distanza di messa a fuoco - Frames",
        "meta_description": "Registra la distanza di messa a fuoco per ogni fotogramma in metri o piedi. I dati si integrano con l'app Mac per i metadati EXIF.",
        "summary": "Questo aggiornamento aggiunge la distanza di messa a fuoco ai dati che puoi registrare per ogni fotogramma, offrendoti un quadro più completo delle tue impostazioni di scatto. L'aggiornamento include anche diversi miglioramenti dell'interfaccia che rendono più comodo inserire e consultare i dati dei tuoi fotogrammi.",
        "alt": "L'app Frames che mostra la registrazione della distanza di messa a fuoco per un fotogramma",
        "heading_1": "Registra la tua distanza di messa a fuoco",
        "paragraph_1": "Quando registri un fotogramma, ora puoi salvare la distanza di messa a fuoco insieme agli altri dati di scatto. Che tu abbia messo a fuoco a 1,2 metri per un ritratto o all'infinito per un paesaggio, questa informazione viene salvata con ogni scatto. L'app legge le tue impostazioni regionali iOS e mostra le distanze in metri o piedi di conseguenza.",
        "paragraph_2": "Se usi Frames su Mac, questi dati sulla distanza di messa a fuoco possono essere scritti nei campi Subject Distance e Subject Distance Range dei metadati EXIF durante l'esportazione in DNG, JPG o TIFF. Le tue impostazioni di messa a fuoco restano con le tue scansioni, proprio come diaframma e tempo di scatto.",
        "heading_2": "Miglioramenti dell'interfaccia",
        "paragraph_3": "Selezionare i valori della lunghezza focale è ora più facile, e il selettore della compensazione dell'esposizione mostra 0 EV invece di Non impostato quando non è stata registrata alcuna regolazione. I parametri appaiono anche in un ordine coerente nell'elenco dei fotogrammi e nelle impostazioni, rendendo l'app più prevedibile nell'uso.",
        "improvements": [
            "Registra la distanza di messa a fuoco per ogni fotogramma con selezione automatica dell'unità in base alle impostazioni iOS",
            "Selezione più facile nell'inserimento dei valori di lunghezza focale",
            "Il selettore della compensazione dell'esposizione ora mostra 0 EV invece di Non impostato",
            "Ordine dei parametri coerente nell'elenco dei fotogrammi e nelle impostazioni",
            "Vari miglioramenti dell'interfaccia"
        ]
    },
    "ja": {
        "title": "撮影距離の記録",
        "meta_title": "撮影距離の記録 - Frames",
        "meta_description": "各コマの撮影距離をメートルまたはフィートで記録。Macアプリと連携してEXIFメタデータに書き込み可能",
        "summary": "このアップデートでは、各コマに記録できるデータに撮影距離が追加され、撮影設定をより完全に把握できるようになりました。また、コマデータの入力と確認をより便利にするインターフェースの改善も含まれています。",
        "alt": "Framesアプリでコマの撮影距離を記録する画面",
        "heading_1": "撮影距離を記録",
        "paragraph_1": "コマを記録する際、他の撮影データと一緒に撮影距離を保存できるようになりました。ポートレートで1.2メートルにフォーカスした場合も、風景で無限遠に設定した場合も、この情報は各ショットと共に保存されます。アプリはiOSの地域設定を読み取り、それに応じてメートルまたはフィートで距離を表示します。",
        "paragraph_2": "MacでFramesを使用している場合、DNG、JPG、TIFFへのエクスポート時に、この撮影距離データをEXIFメタデータのSubject DistanceおよびSubject Distance Rangeフィールドに書き込むことができます。絞りやシャッタースピードと同様に、フォーカス設定もスキャンデータと一緒に保存されます。",
        "heading_2": "インターフェースの改善",
        "paragraph_3": "焦点距離の値の選択がより簡単になり、露出補正ピッカーは調整が記録されていない場合に未設定ではなく0 EVを表示するようになりました。また、コマリストと設定でパラメータが一貫した順序で表示されるようになり、アプリがより予測しやすくなりました。",
        "improvements": [
            "iOS設定に基づく自動単位選択で各コマの撮影距離を記録",
            "焦点距離の値を入力する際の選択がより簡単に",
            "露出補正ピッカーが未設定ではなく0 EVを表示",
            "コマリストと設定で一貫したパラメータ順序",
            "各種インターフェースの改善"
        ]
    },
    "ko": {
        "title": "초점 거리 기록",
        "meta_title": "초점 거리 기록 - Frames",
        "meta_description": "각 프레임의 초점 거리를 미터 또는 피트로 기록하세요. Mac 앱과 연동하여 EXIF 메타데이터에 저장됩니다.",
        "summary": "이번 업데이트는 각 프레임에 기록할 수 있는 데이터에 초점 거리를 추가하여 촬영 설정을 더 완벽하게 파악할 수 있게 해줍니다. 또한 프레임 데이터를 입력하고 검토하는 것을 더 편리하게 만드는 여러 인터페이스 개선 사항이 포함되어 있습니다.",
        "alt": "Frames 앱에서 프레임의 초점 거리 기록 화면",
        "heading_1": "초점 거리 추적",
        "paragraph_1": "프레임을 기록할 때 이제 다른 촬영 데이터와 함께 초점 거리를 저장할 수 있습니다. 인물 사진을 위해 1.2미터에 초점을 맞췄든 풍경을 위해 무한대로 설정했든, 이 정보는 각 촬영과 함께 저장됩니다. 앱은 iOS 지역 설정을 읽고 그에 따라 미터 또는 피트로 거리를 표시합니다.",
        "paragraph_2": "Mac에서 Frames를 사용하는 경우, DNG, JPG 또는 TIFF로 내보낼 때 이 초점 거리 데이터를 EXIF 메타데이터의 Subject Distance 및 Subject Distance Range 필드에 기록할 수 있습니다. 조리개와 셔터 속도처럼 초점 설정도 스캔과 함께 유지됩니다.",
        "heading_2": "인터페이스 개선",
        "paragraph_3": "초점 거리 값 선택이 더 쉬워졌고, 노출 보정 선택기는 조정이 기록되지 않았을 때 설정되지 않음 대신 0 EV를 표시합니다. 또한 프레임 목록과 설정에서 매개변수가 일관된 순서로 표시되어 앱 사용이 더 예측 가능해졌습니다.",
        "improvements": [
            "iOS 설정에 따른 자동 단위 선택으로 각 프레임의 초점 거리 기록",
            "초점 거리 값 입력 시 더 쉬운 선택",
            "노출 보정 선택기가 설정되지 않음 대신 0 EV 표시",
            "프레임 목록과 설정에서 일관된 매개변수 순서",
            "다양한 인터페이스 개선"
        ]
    },
    "nb": {
        "title": "Registrering av fokusavstand",
        "meta_title": "Registrering av fokusavstand - Frames",
        "meta_description": "Registrer fokusavstanden for hver ramme i meter eller fot. Data integreres med Mac-appen for EXIF-metadata i eksporterte skanninger.",
        "summary": "Denne oppdateringen legger til fokusavstand i dataene du kan registrere for hver ramme, slik at du får et mer komplett bilde av opptaksinnstillingene dine. Oppdateringen inkluderer også flere grensesnittforbedringer som gjør det enklere å legge inn og se gjennom rammedataene dine.",
        "alt": "Frames-appen viser registrering av fokusavstand for en ramme",
        "heading_1": "Registrer fokusavstanden din",
        "paragraph_1": "Når du logger en ramme, kan du nå registrere fokusavstanden sammen med de andre opptaksdataene dine. Enten du fokuserte på 1,2 meter for et portrett eller stilte inn på uendelig for et landskap, lagres denne informasjonen med hvert bilde. Appen leser iOS-regioninnstillingene dine og viser avstander i meter eller fot tilsvarende.",
        "paragraph_2": "Hvis du bruker Frames på Mac, kan disse fokusavstandsdataene skrives inn i feltene Subject Distance og Subject Distance Range i EXIF-metadataene ved eksport til DNG, JPG eller TIFF. Fokusinnstillingene dine følger med skanningene dine, akkurat som blender og lukkertid.",
        "heading_2": "Grensesnittforbedringer",
        "paragraph_3": "Det er nå enklere å velge brennviddeverdier, og eksponeringskompensasjonsvelgeren viser 0 EV i stedet for Ikke angitt når ingen justering er registrert. Parametere vises også i en konsistent rekkefølge i rammelisten og innstillingene, noe som gjør appen mer forutsigbar å bruke.",
        "improvements": [
            "Registrer fokusavstand for hver ramme med automatisk enhetsvalg basert på iOS-innstillinger",
            "Enklere valg ved inntasting av brennviddeverdier",
            "Eksponeringskompensasjonsvelgeren viser nå 0 EV i stedet for Ikke angitt",
            "Konsistent parameterrekkefølge i rammelisten og innstillingene",
            "Diverse grensesnittforbedringer"
        ]
    },
    "nl": {
        "title": "Scherpstelafstand vastleggen",
        "meta_title": "Scherpstelafstand vastleggen - Frames",
        "meta_description": "Leg de scherpstelafstand vast voor elke filmframe in meters of voet. Integratie met de Mac-app voor EXIF-metadata in je scans.",
        "summary": "Deze update voegt scherpstelafstand toe aan de gegevens die je kunt vastleggen voor elke filmframe, zodat je een completer beeld krijgt van je opname-instellingen. De update bevat ook verschillende interfaceverbeteringen die het invoeren en bekijken van je filmframegegevens handiger maken.",
        "alt": "Frames-app toont het vastleggen van scherpstelafstand voor een filmframe",
        "heading_1": "Leg je scherpstelafstand vast",
        "paragraph_1": "Bij het vastleggen van een filmframe kun je nu de scherpstelafstand opslaan samen met je andere opnamegegevens. Of je nu scherpstelde op 1,2 meter voor een portret of op oneindig voor een landschap, deze informatie wordt bij elke opname bewaard. De app leest je iOS-regioinstellingen en toont afstanden in meters of voet.",
        "paragraph_2": "Als je Frames op Mac gebruikt, kunnen deze scherpstelafstandgegevens worden geschreven naar de velden Subject Distance en Subject Distance Range in de EXIF-metadata bij het exporteren naar DNG, JPG of TIFF. Je scherpstelinstellingen blijven bij je scans, net als diafragma en sluitertijd.",
        "heading_2": "Interfaceverbeteringen",
        "paragraph_3": "Het selecteren van brandpuntafstandwaarden is nu eenvoudiger en de belichtingscompensatiekiezer toont 0 EV in plaats van Niet ingesteld wanneer geen aanpassing is vastgelegd. Parameters verschijnen ook in een consistente volgorde in de filmframelijst en instellingen, waardoor de app voorspelbaarder wordt.",
        "improvements": [
            "Leg scherpstelafstand vast voor elke filmframe met automatische eenheidsselectie op basis van iOS-instellingen",
            "Eenvoudigere selectie bij het invoeren van brandpuntafstandwaarden",
            "Belichtingscompensatiekiezer toont nu 0 EV in plaats van Niet ingesteld",
            "Consistente parametervolgorde in de filmframelijst en instellingen",
            "Diverse interfaceverbeteringen"
        ]
    },
    "pl": {
        "title": "Rejestrowanie odległości ostrości",
        "meta_title": "Rejestrowanie odległości ostrości - Frames",
        "meta_description": "Rejestruj odległość ostrości dla każdej klatki w metrach lub stopach. Dane integrują się z aplikacją Mac dla metadanych EXIF.",
        "summary": "Ta aktualizacja dodaje odległość ostrości do danych, które możesz rejestrować dla każdej klatki, dając pełniejszy obraz ustawień fotografowania. Aktualizacja zawiera również kilka ulepszeń interfejsu, które czynią wprowadzanie i przeglądanie danych klatek wygodniejszym.",
        "alt": "Aplikacja Frames pokazująca rejestrowanie odległości ostrości dla klatki",
        "heading_1": "Śledź swoją odległość ostrości",
        "paragraph_1": "Podczas rejestrowania klatki możesz teraz zapisać odległość ostrości wraz z innymi danymi fotografowania. Niezależnie od tego, czy ustawiłeś ostrość na 1,2 metra do portretu, czy na nieskończoność do krajobrazu, ta informacja jest zapisywana z każdym zdjęciem. Aplikacja odczytuje regionalne ustawienia iOS i wyświetla odległości w metrach lub stopach odpowiednio.",
        "paragraph_2": "Jeśli używasz Frames na Macu, te dane odległości ostrości mogą być zapisane w polach Subject Distance i Subject Distance Range metadanych EXIF podczas eksportu do DNG, JPG lub TIFF. Twoje ustawienia ostrości pozostają ze skanami, tak jak przysłona i czas otwarcia migawki.",
        "heading_2": "Ulepszenia interfejsu",
        "paragraph_3": "Wybieranie wartości ogniskowej jest teraz łatwiejsze, a selektor kompensacji ekspozycji pokazuje 0 EV zamiast Nie ustawiono, gdy nie zarejestrowano żadnej korekty. Parametry pojawiają się również w spójnej kolejności na liście klatek i w ustawieniach, czyniąc aplikację bardziej przewidywalną.",
        "improvements": [
            "Rejestruj odległość ostrości dla każdej klatki z automatycznym wyborem jednostki na podstawie ustawień iOS",
            "Łatwiejszy wybór przy wprowadzaniu wartości ogniskowej",
            "Selektor kompensacji ekspozycji pokazuje teraz 0 EV zamiast Nie ustawiono",
            "Spójna kolejność parametrów na liście klatek i w ustawieniach",
            "Różne ulepszenia interfejsu"
        ]
    },
    "pt": {
        "title": "Registo da distância de focagem",
        "meta_title": "Registo da distância de focagem - Frames",
        "meta_description": "Registe a distância de focagem para cada fotograma em metros ou pés. Os dados integram-se com a app Mac para metadados EXIF.",
        "summary": "Esta atualização adiciona a distância de focagem aos dados que pode registar para cada fotograma, proporcionando uma imagem mais completa das suas definições de disparo. A atualização também inclui várias melhorias de interface que tornam a introdução e revisão dos dados dos seus fotogramas mais conveniente.",
        "alt": "App Frames a mostrar o registo da distância de focagem para um fotograma",
        "heading_1": "Registe a sua distância de focagem",
        "paragraph_1": "Ao registar um fotograma, pode agora guardar a distância de focagem juntamente com os outros dados de disparo. Quer tenha focado a 1,2 metros para um retrato ou definido para infinito para uma paisagem, esta informação é guardada com cada disparo. A app lê as definições regionais do iOS e apresenta as distâncias em metros ou pés em conformidade.",
        "paragraph_2": "Se utiliza o Frames no Mac, estes dados de distância de focagem podem ser escritos nos campos Subject Distance e Subject Distance Range dos metadados EXIF ao exportar para DNG, JPG ou TIFF. As suas definições de focagem permanecem com as suas digitalizações, tal como a abertura e a velocidade do obturador.",
        "heading_2": "Melhorias de interface",
        "paragraph_3": "Selecionar valores de distância focal é agora mais fácil, e o seletor de compensação de exposição mostra 0 EV em vez de Não ajustado quando nenhum ajuste foi registado. Os parâmetros também aparecem numa ordem consistente na lista de fotogramas e nas definições, tornando a app mais previsível de usar.",
        "improvements": [
            "Registe a distância de focagem para cada fotograma com seleção automática de unidade com base nas definições do iOS",
            "Seleção mais fácil ao introduzir valores de distância focal",
            "O seletor de compensação de exposição agora mostra 0 EV em vez de Não ajustado",
            "Ordem de parâmetros consistente na lista de fotogramas e nas definições",
            "Várias melhorias de interface"
        ]
    },
    "ro": {
        "title": "Înregistrarea distanței de focalizare",
        "meta_title": "Înregistrarea distanței de focalizare - Frames",
        "meta_description": "Înregistrează distanța de focalizare pentru fiecare cadru în metri sau picioare. Datele se integrează cu aplicația Mac pentru metadate EXIF.",
        "summary": "Această actualizare adaugă distanța de focalizare la datele pe care le poți înregistra pentru fiecare cadru, oferindu-ți o imagine mai completă a setărilor de fotografiere. Actualizarea include și câteva îmbunătățiri ale interfeței care fac introducerea și revizuirea datelor cadrelor mai convenabilă.",
        "alt": "Aplicația Frames afișând înregistrarea distanței de focalizare pentru un cadru",
        "heading_1": "Înregistrează distanța de focalizare",
        "paragraph_1": "Când înregistrezi un cadru, acum poți salva distanța de focalizare împreună cu celelalte date de fotografiere. Fie că ai focalizat la 1,2 metri pentru un portret sau ai setat pe infinit pentru un peisaj, această informație este salvată cu fiecare fotografie. Aplicația citește setările regionale iOS și afișează distanțele în metri sau picioare în consecință.",
        "paragraph_2": "Dacă folosești Frames pe Mac, aceste date despre distanța de focalizare pot fi scrise în câmpurile Subject Distance și Subject Distance Range din metadatele EXIF la exportul în DNG, JPG sau TIFF. Setările tale de focalizare rămân cu scanările tale, la fel ca diafragma și viteza obturatorului.",
        "heading_2": "Îmbunătățiri ale interfeței",
        "paragraph_3": "Selectarea valorilor distanței focale este acum mai ușoară, iar selectorul de compensare a expunerii afișează 0 EV în loc de Neconfigurat când nu a fost înregistrată nicio ajustare. Parametrii apar și într-o ordine consistentă în lista de cadre și setări, făcând aplicația mai previzibilă în utilizare.",
        "improvements": [
            "Înregistrează distanța de focalizare pentru fiecare cadru cu selecție automată a unității bazată pe setările iOS",
            "Selecție mai ușoară la introducerea valorilor distanței focale",
            "Selectorul de compensare a expunerii afișează acum 0 EV în loc de Neconfigurat",
            "Ordine consistentă a parametrilor în lista de cadre și setări",
            "Diverse îmbunătățiri ale interfeței"
        ]
    },
    "ru": {
        "title": "Запись дистанции фокусировки",
        "meta_title": "Запись дистанции фокусировки - Frames",
        "meta_description": "Записывайте дистанцию фокусировки для каждого кадра в метрах или футах. Данные интегрируются с приложением Mac для метаданных EXIF.",
        "summary": "Это обновление добавляет дистанцию фокусировки к данным, которые вы можете записывать для каждого кадра, давая более полную картину настроек съёмки. Обновление также включает несколько улучшений интерфейса, которые делают ввод и просмотр данных кадров удобнее.",
        "alt": "Приложение Frames показывает запись дистанции фокусировки для кадра",
        "heading_1": "Записывайте дистанцию фокусировки",
        "paragraph_1": "При записи кадра теперь можно сохранять дистанцию фокусировки вместе с другими данными съёмки. Независимо от того, фокусировались ли вы на 1,2 метра для портрета или установили бесконечность для пейзажа, эта информация сохраняется с каждым снимком. Приложение считывает региональные настройки iOS и отображает расстояния в метрах или футах соответственно.",
        "paragraph_2": "Если вы используете Frames на Mac, эти данные о дистанции фокусировки могут быть записаны в поля Subject Distance и Subject Distance Range метаданных EXIF при экспорте в DNG, JPG или TIFF. Ваши настройки фокусировки сохраняются со сканами, как диафрагма и выдержка.",
        "heading_2": "Улучшения интерфейса",
        "paragraph_3": "Выбор значений фокусного расстояния стал проще, а селектор экспокоррекции показывает 0 EV вместо Не задано, когда корректировка не записана. Параметры также отображаются в единообразном порядке в списке кадров и настройках, что делает приложение более предсказуемым.",
        "improvements": [
            "Запись дистанции фокусировки для каждого кадра с автоматическим выбором единиц на основе настроек iOS",
            "Упрощённый выбор при вводе значений фокусного расстояния",
            "Селектор экспокоррекции теперь показывает 0 EV вместо Не задано",
            "Единообразный порядок параметров в списке кадров и настройках",
            "Различные улучшения интерфейса"
        ]
    },
    "sv": {
        "title": "Registrering av fokusavstånd",
        "meta_title": "Registrering av fokusavstånd - Frames",
        "meta_description": "Registrera fokusavståndet för varje ruta i meter eller fot. Data integreras med Mac-appen för EXIF-metadata i dina skanningar.",
        "summary": "Den här uppdateringen lägger till fokusavstånd till de data du kan registrera för varje ruta, vilket ger dig en mer komplett bild av dina fotograferingsinställningar. Uppdateringen innehåller också flera gränssnittsförbättringar som gör det smidigare att mata in och granska dina rutdata.",
        "alt": "Frames-appen visar registrering av fokusavstånd för en ruta",
        "heading_1": "Registrera ditt fokusavstånd",
        "paragraph_1": "När du loggar en ruta kan du nu registrera fokusavståndet tillsammans med dina andra fotograferingsdata. Oavsett om du fokuserade på 1,2 meter för ett porträtt eller ställde in på oändligt för ett landskap, sparas denna information med varje bild. Appen läser dina iOS-regioninställningar och visar avstånd i meter eller fot därefter.",
        "paragraph_2": "Om du använder Frames på Mac kan dessa fokusavståndsdata skrivas in i fälten Subject Distance och Subject Distance Range i EXIF-metadata vid export till DNG, JPG eller TIFF. Dina fokusinställningar följer med dina skanningar, precis som bländare och slutartid.",
        "heading_2": "Gränssnittsförbättringar",
        "paragraph_3": "Att välja brännviddsvärden är nu enklare, och exponeringskompensationsväljaren visar 0 EV istället för Inte inställd när ingen justering har registrerats. Parametrar visas också i en konsekvent ordning i rutlistan och inställningarna, vilket gör appen mer förutsägbar att använda.",
        "improvements": [
            "Registrera fokusavstånd för varje ruta med automatiskt enhetsval baserat på iOS-inställningar",
            "Enklare val vid inmatning av brännviddsvärden",
            "Exponeringskompensationsväljaren visar nu 0 EV istället för Inte inställd",
            "Konsekvent parameterordning i rutlistan och inställningarna",
            "Diverse gränssnittsförbättringar"
        ]
    },
    "th": {
        "title": "บันทึกระยะโฟกัส",
        "meta_title": "บันทึกระยะโฟกัส - Frames",
        "meta_description": "บันทึกระยะโฟกัสสำหรับแต่ละเฟรมเป็นเมตรหรือฟุต ข้อมูลเชื่อมต่อกับแอป Mac สำหรับเมตาดาต้า EXIF",
        "summary": "การอัปเดตนี้เพิ่มระยะโฟกัสในข้อมูลที่คุณสามารถบันทึกสำหรับแต่ละเฟรม ทำให้คุณเห็นภาพการตั้งค่าการถ่ายภาพได้สมบูรณ์ยิ่งขึ้น การอัปเดตยังรวมถึงการปรับปรุงอินเทอร์เฟซหลายอย่างที่ทำให้การป้อนและตรวจสอบข้อมูลเฟรมสะดวกยิ่งขึ้น",
        "alt": "แอป Frames แสดงการบันทึกระยะโฟกัสสำหรับเฟรม",
        "heading_1": "ติดตามระยะโฟกัสของคุณ",
        "paragraph_1": "เมื่อบันทึกเฟรม คุณสามารถบันทึกระยะโฟกัสพร้อมกับข้อมูลการถ่ายภาพอื่นๆ ได้แล้ว ไม่ว่าคุณจะโฟกัสที่ 1.2 เมตรสำหรับภาพบุคคลหรือตั้งค่าเป็นอินฟินิตี้สำหรับภาพทิวทัศน์ ข้อมูลนี้จะถูกบันทึกไว้กับทุกภาพ แอปจะอ่านการตั้งค่าภูมิภาค iOS ของคุณและแสดงระยะทางเป็นเมตรหรือฟุตตามนั้น",
        "paragraph_2": "หากคุณใช้ Frames บน Mac ข้อมูลระยะโฟกัสนี้สามารถเขียนลงในฟิลด์ Subject Distance และ Subject Distance Range ของเมตาดาต้า EXIF เมื่อส่งออกเป็น DNG, JPG หรือ TIFF การตั้งค่าโฟกัสของคุณจะอยู่กับไฟล์สแกน เช่นเดียวกับรูรับแสงและความเร็วชัตเตอร์",
        "heading_2": "การปรับปรุงอินเทอร์เฟซ",
        "paragraph_3": "การเลือกค่าทางยาวโฟกัสง่ายขึ้น และตัวเลือกชดเชยแสงจะแสดง 0 EV แทนที่จะเป็น ยังไม่กำหนด เมื่อไม่มีการบันทึกการปรับค่า พารามิเตอร์ยังแสดงในลำดับที่สอดคล้องกันในรายการเฟรมและการตั้งค่า ทำให้แอปใช้งานได้คาดเดาได้มากขึ้น",
        "improvements": [
            "บันทึกระยะโฟกัสสำหรับแต่ละเฟรมพร้อมการเลือกหน่วยอัตโนมัติตามการตั้งค่า iOS",
            "เลือกได้ง่ายขึ้นเมื่อป้อนค่าทางยาวโฟกัส",
            "ตัวเลือกชดเชยแสงแสดง 0 EV แทน ยังไม่กำหนด",
            "ลำดับพารามิเตอร์สอดคล้องกันในรายการเฟรมและการตั้งค่า",
            "การปรับปรุงอินเทอร์เฟซต่างๆ"
        ]
    },
    "tr": {
        "title": "Odak mesafesi kaydı",
        "meta_title": "Odak mesafesi kaydı - Frames",
        "meta_description": "Her kare için odak mesafesini metre veya fit olarak kaydedin. Veriler Mac uygulamasıyla EXIF meta verileri için entegre olur.",
        "summary": "Bu güncelleme, her kare için kaydedebileceğiniz verilere odak mesafesini ekleyerek çekim ayarlarınızın daha eksiksiz bir resmini sunar. Güncelleme ayrıca kare verilerinizi girmeyi ve incelemeyi daha rahat hale getiren çeşitli arayüz iyileştirmeleri içerir.",
        "alt": "Frames uygulaması bir kare için odak mesafesi kaydını gösteriyor",
        "heading_1": "Odak mesafenizi kaydedin",
        "paragraph_1": "Bir kare kaydederken artık diğer çekim verilerinizle birlikte odak mesafesini de kaydedebilirsiniz. İster bir portre için 1,2 metreye odaklanmış olun, ister bir manzara için sonsuza ayarlamış olun, bu bilgi her çekimle birlikte kaydedilir. Uygulama iOS bölge ayarlarınızı okur ve mesafeleri buna göre metre veya fit olarak gösterir.",
        "paragraph_2": "Mac'te Frames kullanıyorsanız, bu odak mesafesi verileri DNG, JPG veya TIFF'e aktarırken EXIF meta verilerinin Subject Distance ve Subject Distance Range alanlarına yazılabilir. Odak ayarlarınız, diyafram ve enstantane gibi taramalarınızla birlikte kalır.",
        "heading_2": "Arayüz iyileştirmeleri",
        "paragraph_3": "Odak uzaklığı değerlerini seçmek artık daha kolay ve pozlama telafisi seçici, hiçbir ayarlama kaydedilmediğinde Ayarlanmamış yerine 0 EV gösteriyor. Parametreler ayrıca kare listesi ve ayarlarda tutarlı bir sırada görüntülenerek uygulamayı daha öngörülebilir hale getiriyor.",
        "improvements": [
            "iOS ayarlarına göre otomatik birim seçimiyle her kare için odak mesafesini kaydedin",
            "Odak uzaklığı değerlerini girerken daha kolay seçim",
            "Pozlama telafisi seçici artık Ayarlanmamış yerine 0 EV gösteriyor",
            "Kare listesi ve ayarlarda tutarlı parametre sırası",
            "Çeşitli arayüz iyileştirmeleri"
        ]
    },
    "uk": {
        "title": "Запис дистанції фокусування",
        "meta_title": "Запис дистанції фокусування - Frames",
        "meta_description": "Записуйте дистанцію фокусування для кожного кадру в метрах або футах. Дані інтегруються з програмою Mac для метаданих EXIF.",
        "summary": "Це оновлення додає дистанцію фокусування до даних, які ви можете записувати для кожного кадру, даючи повнішу картину налаштувань зйомки. Оновлення також включає кілька покращень інтерфейсу, які роблять введення та перегляд даних кадрів зручнішим.",
        "alt": "Програма Frames показує запис дистанції фокусування для кадру",
        "heading_1": "Записуйте дистанцію фокусування",
        "paragraph_1": "При записі кадру тепер можна зберігати дистанцію фокусування разом з іншими даними зйомки. Незалежно від того, чи ви фокусувалися на 1,2 метра для портрета, чи встановили нескінченність для пейзажу, ця інформація зберігається з кожним знімком. Програма зчитує регіональні налаштування iOS і відображає відстані в метрах або футах відповідно.",
        "paragraph_2": "Якщо ви використовуєте Frames на Mac, ці дані про дистанцію фокусування можуть бути записані в поля Subject Distance та Subject Distance Range метаданих EXIF при експорті в DNG, JPG або TIFF. Ваші налаштування фокусування зберігаються зі сканами, як діафрагма та витримка.",
        "heading_2": "Покращення інтерфейсу",
        "paragraph_3": "Вибір значень фокусної відстані тепер простіший, а селектор експокорекції показує 0 EV замість Не встановлено, коли корекція не записана. Параметри також відображаються в однаковому порядку в списку кадрів і налаштуваннях, що робить програму більш передбачуваною.",
        "improvements": [
            "Запис дистанції фокусування для кожного кадру з автоматичним вибором одиниць на основі налаштувань iOS",
            "Спрощений вибір при введенні значень фокусної відстані",
            "Селектор експокорекції тепер показує 0 EV замість Не встановлено",
            "Однаковий порядок параметрів у списку кадрів і налаштуваннях",
            "Різні покращення інтерфейсу"
        ]
    },
    "vi": {
        "title": "Ghi nhận khoảng cách lấy nét",
        "meta_title": "Ghi nhận khoảng cách lấy nét - Frames",
        "meta_description": "Ghi khoảng cách lấy nét cho mỗi khung hình bằng mét hoặc feet. Dữ liệu tích hợp với ứng dụng Mac cho siêu dữ liệu EXIF.",
        "summary": "Bản cập nhật này thêm khoảng cách lấy nét vào dữ liệu bạn có thể ghi cho mỗi khung hình, giúp bạn có cái nhìn đầy đủ hơn về cài đặt chụp ảnh. Bản cập nhật cũng bao gồm một số cải tiến giao diện giúp việc nhập và xem lại dữ liệu khung hình thuận tiện hơn.",
        "alt": "Ứng dụng Frames hiển thị ghi nhận khoảng cách lấy nét cho một khung hình",
        "heading_1": "Theo dõi khoảng cách lấy nét",
        "paragraph_1": "Khi ghi nhận một khung hình, bạn có thể lưu khoảng cách lấy nét cùng với các dữ liệu chụp khác. Dù bạn lấy nét ở 1,2 mét cho ảnh chân dung hay đặt vô cực cho phong cảnh, thông tin này được lưu với mỗi bức ảnh. Ứng dụng đọc cài đặt vùng iOS của bạn và hiển thị khoảng cách bằng mét hoặc feet tương ứng.",
        "paragraph_2": "Nếu bạn sử dụng Frames trên Mac, dữ liệu khoảng cách lấy nét này có thể được ghi vào các trường Subject Distance và Subject Distance Range của siêu dữ liệu EXIF khi xuất sang DNG, JPG hoặc TIFF. Cài đặt lấy nét của bạn đi kèm với các bản scan, giống như khẩu độ và tốc độ màn trập.",
        "heading_2": "Cải tiến giao diện",
        "paragraph_3": "Việc chọn giá trị tiêu cự giờ dễ dàng hơn, và bộ chọn bù phơi sáng hiển thị 0 EV thay vì Chưa Đặt khi không có điều chỉnh nào được ghi. Các thông số cũng xuất hiện theo thứ tự nhất quán trong danh sách khung hình và cài đặt, giúp ứng dụng dễ đoán hơn khi sử dụng.",
        "improvements": [
            "Ghi khoảng cách lấy nét cho mỗi khung hình với tự động chọn đơn vị dựa trên cài đặt iOS",
            "Chọn dễ dàng hơn khi nhập giá trị tiêu cự",
            "Bộ chọn bù phơi sáng hiển thị 0 EV thay vì Chưa Đặt",
            "Thứ tự thông số nhất quán trong danh sách khung hình và cài đặt",
            "Các cải tiến giao diện khác"
        ]
    },
    "zh": {
        "title": "记录对焦距离",
        "meta_title": "记录对焦距离 - Frames",
        "meta_description": "以米或英尺为单位记录每帧的对焦距离。数据可通过 Mac 应用写入 EXIF 元数据",
        "summary": "此更新为每帧可记录的数据新增了对焦距离,让您更全面地了解拍摄设置。更新还包含多项界面改进,使输入和查看帧数据更加便捷。",
        "alt": "Frames 应用显示帧的对焦距离记录",
        "heading_1": "记录对焦距离",
        "paragraph_1": "记录帧时,您现在可以将对焦距离与其他拍摄数据一起保存。无论是为人像对焦在 1.2 米处,还是为风景设置为无穷远,这些信息都会随每张照片保存。应用会读取您的 iOS 地区设置,并相应地以米或英尺显示距离。",
        "paragraph_2": "如果您在 Mac 上使用 Frames,这些对焦距离数据可以在导出为 DNG、JPG 或 TIFF 时写入 EXIF 元数据的 Subject Distance 和 Subject Distance Range 字段。您的对焦设置会与扫描文件一起保留,就像光圈和快门速度一样。",
        "heading_2": "界面改进",
        "paragraph_3": "选择焦距值现在更加容易,曝光补偿选择器在未记录调整时显示 0 EV 而非「未设置」。参数在帧列表和设置中也以一致的顺序显示,使应用更易于预测。",
        "improvements": [
            "根据 iOS 设置自动选择单位,为每帧记录对焦距离",
            "输入焦距值时选择更轻松",
            "曝光补偿选择器现显示 0 EV 而非「未设置」",
            "帧列表和设置中参数顺序一致",
            "多项界面改进"
        ]
    },
    "zh-hant": {
        "title": "記錄對焦距離",
        "meta_title": "記錄對焦距離 - Frames",
        "meta_description": "以公尺或英尺為單位記錄每個畫格的對焦距離。資料可透過 Mac 應用程式寫入 EXIF 中繼資料",
        "summary": "此更新為每個畫格可記錄的資料新增了對焦距離,讓您更全面地了解拍攝設定。更新還包含多項介面改進,使輸入和檢視畫格資料更加便利。",
        "alt": "Frames 應用程式顯示畫格的對焦距離記錄",
        "heading_1": "記錄對焦距離",
        "paragraph_1": "記錄畫格時,您現在可以將對焦距離與其他拍攝資料一起儲存。無論是為人像對焦在 1.2 公尺處,還是為風景設定為無限遠,這些資訊都會隨每張照片儲存。應用程式會讀取您的 iOS 地區設定,並相應地以公尺或英尺顯示距離。",
        "paragraph_2": "如果您在 Mac 上使用 Frames,這些對焦距離資料可以在輸出為 DNG、JPG 或 TIFF 時寫入 EXIF 中繼資料的 Subject Distance 和 Subject Distance Range 欄位。您的對焦設定會與掃描檔案一起保留,就像光圈和快門速度一樣。",
        "heading_2": "介面改進",
        "paragraph_3": "選擇焦距值現在更加容易,曝光補償選擇器在未記錄調整時顯示 0 EV 而非「未設定」。參數在畫格列表和設定中也以一致的順序顯示,使應用程式更易於預測。",
        "improvements": [
            "根據 iOS 設定自動選擇單位,為每個畫格記錄對焦距離",
            "輸入焦距值時選擇更輕鬆",
            "曝光補償選擇器現顯示 0 EV 而非「未設定」",
            "畫格列表和設定中參數順序一致",
            "多項介面改進"
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
            },
            {
                "type": "heading",
                "level": 3,
                "content": trans["heading_2"]
            },
            {
                "type": "paragraph",
                "content": trans["paragraph_3"]
            }
        ],
        "improvements": trans["improvements"],
        "fixes": [],
        "patches": []
    }

    # Write the file
    file_path = BASE_PATH / lang_code / "1.21.0-ios.json"

    # Create directory if it doesn't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    return True


def main():
    """Main function to create all language files."""

    print("Creating 1.21.0-ios.json changelog files for all languages...\n")

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
