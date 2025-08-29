Lastenheft «Zeiterfassungssystem» 
Version 1.0 
Mykola Golubei 
Praktikant Produkt Manger 
Axilaris GmbH 
1. Hauptziel  
2. Benutzer und Rollen 
3. Zeiterfassung 
4. Berichte 
5. Funktionale Anforderungen und nicht funktionale Anforderungen 
6. Use Case (Mitarbeiter), Entwurf der Funktionalitäten und des Layouts der 
Webanwendung – Version 1.0   
1. Hauptziel 
Das Unternehmen hat mehrere Kunden (Supermärkte), und die Entwickler 
arbeiten an Projekten für jeden diser Kunden. 
Es soll ein System ein System eingeführt werden, das es den Enwicklern 
ermöglicht, den Beginn und das Ende ihrer Arbeit an einem bestimmen 
Kundenprojekt zu erfassen. Vor Arbeitsbeginn muss der Entwickler den Kunden 
aus einer Liste auswählen - erst danach wird die Schaltfläche "Arbeitbeginn" 
aktiviren. 
Nach Beendigung der Arbeit muss der Entwickler die Schaltfläche „Zeit 
stoppen“ betätigt. 
Am Ende eines jeden Monats soll automatisch ein Bericht generiert werden: 
Anzahl der Arbeitsstunden jedes Entwicklers, aufgeschlüsselt nach Kunden; 
Gesamtstunden je Kunde. 
Dieser Bericht wird an die Buchhaltung übermittelt, um Rechnungen an die 
Kunden zu erstellen. 
2. Benutzer und Rollen 
Die Rollen sind strikt voneinander getrennt. Jeder Benutzer hat nur Zugriff auf 
Funktionen und Daten, die seiner Rolle entsprechen. Das Prinzip der minimalen 
Rechtevergabe muss gewährleistet sein. 
Die Anwendung unterscheidet zwei Benutzerrollen mit klar definierten 
Rechten und Verantwortlichkeiten: 
Entwickler (Mitarbeiter) 
• Muss beim ersten Login das Initialpasswort (vom Teamleiter vergeben) 
ändern. 
• Kann die Zeiterfassung starten und stoppen. 
• Muss nach Beendigung einer Sitzung einen Kommentar über die erledigte 
Arbeit eintragen. 
• Muss vor Beginn einer Zeiterfassung einen Kunden aus der Kundenliste 
auswählen. 
• Kann ausschließlich die eigenen Zeiteinträge einsehen. 
• Kann bei Fehlern eigene Sitzungen korrigieren oder löschen. 
• Kann keine neue Sitzung starten, solange die vorherige nicht korrekt 
beendet wurde. Falls eine Sitzung nicht abgeschlossen wurde, muss der 
Entwickler das korrekte Enddatum eintragen und einen Kommentar 
hinzufügen. 
• Alle Korrekturen dürfen nur bis zum letzten Kalendertag des Monats 
vorgenommen werden. 
Teamleiter (Chef) 
• Verfügt über alle Rechte eines Entwicklers. 
• Hat Zugriff auf die Berichte aller Mitarbeiter. 
• Kann Monatsberichte pro Mitarbeiter sowie aggregierte Berichte pro 
Kunde einsehen. 
• Darf Zeiteinträge im Falle der Abwesenheit eines Mitarbeiters bearbeiten. 
• Kann Sitzungen auch nach Ablauf des Kalendermonats ändern. 
• Kann neue Benutzer anlegen, indem er eine geschäftliche E-Mail-Adresse 
und ein Initialpasswort vergibt. Beim ersten Login muss der Benutzer 
dieses Passwort ändern. 
Rechtevergleich der Rollen 
Funktion 
Teamleiter (Chef) 
Entwickler 
(Mitarbeiter) 
Passwortänderung beim ersten 
Login 
Zeiterfassung starten/stoppen 
Pflicht-Kommentar nach 
Sitzungsende 
Kundenauswahl vor 
Sitzungsbeginn 
Einsicht in Zeiteinträge 
Sitzungen korrigieren/löschen 
Keine neue Sitzung ohne 
Beendigung der vorherigen 
Korrektes Sitzungsende mit 
Kommentar 
Monatsberichte pro Mitarbeiter 
einsehen 
Aggregierte Berichte pro Kunde 
einsehen 
Bearbeitung von Zeiten bei 
Abwesenheit eines Mitarbeiters 
Neue Benutzer anlegen 

Die Auswahl eines Kunden ist verpflichtend, bevor die Zeiterfassung gestartet 
werden kann. 
Die Schaltfläche „Arbeitsbeginn“ ist inaktiv, solange kein Kunde ausgewählt 
wurde. 
Die Schaltfläche „Zeit stoppen“ beendet die aktuelle Zeiterfassungssitzung. 
Eine Aufgabenbeschreibung ist nicht erforderlich (Details werden in Jira 
dokumentiert). 
4. Berichte 
Monatlicher Bericht für jeden Mitarbeiter mit Aufschlüsselung der Stunden je 
Kunde 
Monatlicher Bericht für jeden Kunden mit Gesamtsumme der Stunden aller 
Entwickler 
5. Funktionale Anforderungen und nicht funktionale Anforderungen  
Es darf keine neue Sitzung gestartet werden, solange die vorherige Sitzung nicht 
beendet ist. 
Eine Sitzung gilt als beendet, wenn die Schaltfläche „Zeit stoppen“ betätigt 
wurde und das Feld „Kommentar“ ausgefüllt ist. 
Funktionale Anforderungen 
Anforderung Beschreibung Priorität 
Kundenauswahl vor 
Beginn 
Die Schaltfläche „Arbeitsbeginn“ ist 
deaktiviert, solange kein Kunde ausgewählt 
wurde. 
 
Zeiterfassung 
starten 
Entwickler können die Arbeitszeit nur 
starten, wenn ein Kunde aus einer festen 
Liste ausgewählt wurde. 
 
Zeiterfassung 
stoppen 
Entwickler können ihre Zeiterfassung 
beenden, indem sie auf „Arbeitsende“ 
klicken. 
 
Eigene Zeiteinträge 
einsehen 
Entwickler können nur ihre eigenen 
Zeiteinträge sehen.  
Eigene Zeiteinträge 
bearbeiten 
Entwickler können ihre eigenen 
Arbeitszeiten bis zum Ende des 
Kalendermonats bearbeiten. Der Teamleiter 
kann Sitzungen auch nach Ablauf des 
Kalendermonats bearbeiten. 
 
Eigene Zeiteinträge 
löschen 
Entwickler können ihre eigenen 
Arbeitssitzungen bis zum Ende des 
Kalendermonats löschen. Der Teamleiter 
kann Sitzungen auch nach Ablauf des 
Kalendermonats löschen. 
 
Berichte für 
Entwickler 
Monatlicher Bericht pro Entwickler mit 
Aufschlüsselung der Stunden je Kunde.  
Berichte für 
Kunden 
Monatlicher Bericht pro Kunde mit 
Gesamtsumme der geleisteten Stunden aller 
Entwickler. 
 
Zugriff für 
Teamleiter 
Der Teamleiter kann alle Berichte einsehen 
und Arbeitszeiteinträge der Mitarbeiter 
bearbeiten. 
 
Benutzerverwaltung 
Der Teamleiter kann neue Benutzer mit 
geschäftlicher E-Mail-Adresse und 
Initialpasswort anlegen. 
 
Passwortänderung 
beim ersten Login 
Benutzer müssen ihr Initialpasswort beim 
ersten Login ändern.  
 
Nicht funktionale Anforderungen 
Anforderung 
Rollentrennung          
Beschreibung 
Strikte Trennung der Benutzerrollen mit 
minimalen Zugriffsrechten 
Priorität 
Weboberfläche           
Die Anwendung soll über eine 
Weboberfläche bedienbar sein. 
Plattform               
Die Anwendung muss auf Windows
Systemen lauffähig sein. 
Browserunterstützung    Unterstützung für die Browser Google 
Chrome und Mozilla Firefox 
Zugriffsschutz 
Anmeldung erfolgt über 
unternehmenseigene E-Mail-Adresse 
Datenschutz 
Mitarbeiter dürfen nur ihre eigenen Daten 
einsehen 
Sprache der 
Oberfläche 
Die Benutzeroberfläche muss auf Deutsch 
verfügbar sein. 
 
  
6. Use Case (Mitarbeiter), Entwurf der Funktionalitäten und des Layouts der 
Webanwendung – Version 1.0 
Use Case (Mitarbeiter): 
1. Anmeldung und Abmeldung 
2. Buchung erfassen 
3. Buchung Nacherfassen 
4. Buchung korrigieren (nur bis Monatsende) 
5. Buchung lösen (nur bis Monatsende) 
6. Buchungsübersicht 