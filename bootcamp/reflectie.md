# Reflectie bootcamp - Jonathan Ricardo

Eerst ga ik vertellen wat ik per dag geleerd heb, en hoe ik daarop terug kijk. 
Daarna ga ik vertellen wat mijn kijk is naar AI als vakgebied.
En als laatst vertel ik mijn leaerdoelen voor de rest van de minor.

## Dag 1
Er valt niet heel veel te zeggen over dag 1. Hier leerde we vooral de basics van programmeren in python. Aangezien ik een Software Enigineer student ben, was dit niet heel lastig voor mij, omdat ik al ervaring heb met coderen.

## Dag 2
Tijdens de tweede dag kregen we een introductie over data en hoe een simpel model werkt. Hier heb ik geleerd wat voor soorten data er zijn, zoals categorisch of numeriek. En hoe ik deze data kan omzetten naar data die een model kan lezen, doormiddel van encoders zoals `LabelEncoder` voor ordinale data of `OneHotEncoder` voor nominale waarden. Ook heb ik geleerd hoe je met missende data om moet gaan, en hoe je dit vult. Deze data kan je nu opsplitsen in train en test data.

Daarna maakte wij 2 modellen, KNN en LR, en trainde we deze modellen met de train data. Daarna testte we deze modellen op te test data. Ook moesten wij ons model verbeteren en daarvoor heb je verschillende technieken. Zoals andere features te kiezen, of bij KNN het aantal neighbors omhoog of omlaag doen.

Tijdens deze dag heb ik ook een korte samenvatting gemaakt van de theorie, om mij een geheugen steuntje te geven.

## Dag 3
#### Ochtend
Deze dag was best wel zwaar. We kregen heel erg veel theorie over statestiek en alles daar omheen. Daarna moesten wij werken aan een notebook over airline satisfaction. Hier maakte we gebruik van een steekproef om daarvan de statestiek te krijgen. Ook leerde je welke features geen impact hadden zoals id. Hierna gingen we kijken naar wat statestieken zoals de standard diviation, dit betekend hoe groot de variatie of verspreiding is in een set van waarden. Om een duidelijker beeld te krijgen van je data, gingen we onze data plotten in grafieken. Nu kan je snel zien hoe je data ervoor staat.

Daarna zette we alle categorische data om in numerieke waarden. Dit is noodzakelijk als je de data wilt normaliseren. Daarna testte we de data met een ktest (Kolmogorov-Smirnov test), deze data testen we tegen een normale verdeling. Hiermee zien we of de data normaal verdeeld is of niet. Dit is handig om te weten, want veel statistische technieken gaan er vanuit dat de data normaal verdeeld is.

Ook heb ik geleerd over de correlatie tussen verschillende features. Dit betekend dat als 1 feature omhoog gaat, dat de andere ook omhoog gaat, die is een positieve correlatie. Maar hiermee moet je wel uitkijken, want correlatie is niet causaliteit.

Daarna leerde we hoe we linear regressie toe kunnen passen op de data. Hier komen heel veel verschillende waarden uit waaronder p-values. Als deze p-value onder 0.05 is, betekend dat er significantie is, en dan verwerp je de nulhypothese.

#### Middag
Hier kregen we een data set over diabetes, je moest daarom ook weten hoe diabetes werkt. Dit is namelijk handig als je weet welke features wel of niet belangrijk zijn. Weer moesten we hier veel missende data vullen voordat we aan de slag konden gaan met een model. Daarna gingen we de data analyseren. Dit deden we daar alle data te plotten in grafieken voor een duideljk overzicht. Hier leerde je wat `bins` zijn en hoe dat invloed kan hebben over hoe je data gevisualiseerd is. Om verder de data te analyseren gebruikte we een scatter plot, hier kan je in een notendop zien van de relaties zijn tussen verschillende variablen. Weer berekende we hier de correlatie tussen verschillende features, dit is dus handig voor feature selectie.

Uiteindelijk gingen we voorspellingen maken met modelen met deze data. Weer splitste we de data om in train en test data. Hier leerde je wat een SVM en LR model is. Hiermee konden we voorspellen welke vrouwen wel of niet diabetes hebben. We leerde ook wat ensembling is, dat is een techniek waarmee meerdere modellen worden getraint en hun voorspellingen worden gecobineerd.

Daarna moesten we onze resultaten verbeteren met feature extraction, dit doe je opbasis van de resulataten uit de raindomforestcassifier. Hieruit krijg je de data die het meest met elkaar ondelinge correlatie hebben. We hebben daarna de features met de laagste score eruit gehaald.

## Dag 4
Op dag 4 gingen we werken computer vision. Eerste gingen we aan de slag met een oud algoritme, namelijk Haar Cascade om gezichten te herkennen. Maar eerst leerde we verschillende technieken om edges te vinden in een plaatje. Dit deden we met het canny algoritme, en deze konden we beter maken door de kleuren van het plaatje te veranderen. Door het contrast omhoog te zetten tussen de kleuren, is het makkelijker voor canny om randen te vinden in een figuur.

Nu gingen we gezichten zoeken met Haar Cascade. Eerst moest je de foto omzetten naar zwartwit. Dit algoritme geef de coördinaten terug van een gevonden gezicht. Met deze data kan je een rechthoek tekenen op de originele foto met deze coördinaten. Omdat dit algoritme al oud is, presteerde het niet heel goed om mijn foto. Je zou de neigbhors parameter kunnen aanpassen, maar dat kan je meer of minder valse herkenningen geven in de foto. Dit zelfde geldt voor de minSize parameter. We deden dit ook om de mond en ogen te detecteren.

Nu gingen we werken met CNN, een neural network. Hier gaven we de zelfde foto aan de deze herkende wel alle gezichten, wat cascade niet deed. Maar ook hier had ik een nep gezicht gevonden. Juist omdat dit neural network zo krachtig is, kan het patronen zien in de foto wat precies lijkt op een gezicht, maar wat eigenlijk een stukje kleding is.

Daarna gingen we aan de slag met numpy arrays voor fotos. Hier zette we de zelfde foto om in een numpy 2d array. Nu dat de foto in een 2d array zit, kan je precies zien wat de RBG values zijn per pixels, en dus ook aanpassen met coördinaten van de 2d array.

We leerde hier ook dat je fotos kan aanpassen. Dit zorgt ervoor dat je dataset veel groter wordt, je kan hier 10 plaatjes omzetten in 40 plaatjes. Dit is nartuurlijk fijn voor AI, je hebt dus meer data om mee te trainen.

## Dag 5
Hier gingen we verder met statestiek. Weer kregen we heel er veel theorie over de statestiek. Het ging vooral over de standaard diviation, en hoe je die kan berekenen. En over verschillende testen zoals de t-test en ANOVA.

Eerst moesten we de t-testen uitoefenen op onze data. Hieruit kwamen de p-values van onze data. Zoals ik eerder zei, als dit getal lager is dan 0.05 dan is er spraken van significantie. Dat betekend dus dat deze features belangrijk zijn. Maar volgensmij is er bij mij iets niet helemaal goed gegaan, want al mijn waarden zijn extreem lage getallen.

Daarna moesten we ANOVA uitvoeren om daarme uit te zoeken of er significantie is tussen 2 features. Deze test werke echter wel fatsoenlijk volgens mijn data.

Daarna moest je de features selecteren op basis van correlatie met elkaar, en daarna trainde we 5 modellen met deze data, en bekeken we de daaruit gekregen accuracies.

Nu moesten we hetzelfde doen, maar dan met alle features inplaats van features met een hoge correlatie, om dus te kijken of dat impact heeft op de accuracy van onze modellen. En zoals verwacht heeft het dus dergelijk effect op de accuracy. De modellen met de belangrijke features presteerde beter dan de modellen met alle features. Wat logisch is, omdat de andere modelle leren op nutteloze informatie.

## Dag 6
Op dag 6 leerde we meer over neurale netwerken en hou ze in elkaar zitten. Een neural netwerk heeft dus een input laag, hidden layers en een output laag. De inputlayer inputshape parameter moet overeenkomen met de data die je het nn geeft. Ook moet de laaste layer ook de hoeveilheid neuronen hebben als de uitkomst die je wilt hebben, dus als er 3 mogelijke antwoorden zijn, heb je 3 neuronen in de laaste laag.

Daarna trainde we de modellen, en daarmee geef je mee hoeveel epochs er zijn, dat zijn dus hoe vaak het model door de complete data set heen gaat, en dus leert van de train data. Daarna kan je het model weer testen op accuracy. De invloed van mer of minder lagen, en meer of minder neuronen kan een grote invloed hebben op de resultaten. Dus daar moet je goed naar kijken.

Dit deden we dus op de IMDB data set, om dus te voorspellen of een achter gelaten review positief of negatief is. Eerst zette we de data om in getallen, zodat ons model het kan lezen. Daarna trainen we het model met 50 epochs. Dit deed ik om te zien wat de impact is van de hoeveelheid epcohs. Als je dus te veel epochs hebt, leert het model te goed aan de training data en is er spraken van overfitting. En in mijn model is er dus ook spraken daarvan. Er zijn dus verschillende manieren om dit op te losen, maar mij is het niet gelukt. Ik heb wel dropout layers toegepast, dit zorgt ervoor daat sommige neuronen uitgeschakeld worden, waardoor andere neuronen moeten werken, en het model niet te gewent raakt aan de train data.

## Dag 7
Hier moesten we een model maken die de lyrics van abba gebruikt als trainings data, en om daarna voorspellingen te maken met een gegeven stuk lyrics. Dus dit model kan dus een liedje schrijven door het volgende karakter te voorspellen.

Eerst moesten we encoders en decoders maken die de worden omzet in nummers voor een model. Nu dat de data klaar was konden we ons model trainen. Dit deden we met LSTM layers. Deze layers hebben geheugencellen die informatie kunnen opslaan en ophalen. Deze cellen hebben ook een inputpoort, forgetpoort en outputpoort. Het duurde wel heel erg lang om het model te trainen, zo'n 50 minuten.

Dit model maakt ook gebruik van callbacks, dit zorgt ervoor dat per elke epoch het huidige model wordt opgeslagen. We slaan het model elke keer op als json, om het op een ander moment opnieuw te gebruiken

Daarna opende we het laatst opgeslagen model. en dankzij de `sample`, `generate` en `make_seed` funcites kunnen we nu liedjes genereren. De generate functie voorsplelt de tekst die moet komen na de gegeven seed. de generate functie gebruikt de sample functie, die kiest een index uit de voorspelling van het model. Dit allemaal samen creërt een nieuw Abba liedje! Maar de tekst klopt niet helemaal.

## Dag 8
In de laatste dag gingen we verder met computer vision. Hier leerde we hoe verschillende modellen werkte om handgeschreven nummers te herkennen. Waaronder een KNN, NN en CNN model. Vorige week hadden we al gewerkt met een kant en klaar CNN model, maar nu gingen we meer diep erop in hoe het precies werkt. Een CNN model maakt gebruik van conv2 en pooliong om features in de figuren te onderscheiden, bijvoorbeeld, een handgeschreven 8, zijn twee circles, eentje hoog en eentje laag. Dus als het model deze features herkent in een model, weet het precies welk getal het is.

Ook keken we naar wat de modellen fout deden. Bijvoorbeeld, het KNN model maakte simpele fouten zoals een 1 en 7, terwijl het CNN model vaak fouten maakte teussen 4 en 9. Omdat die dezelfde onderliggende features hebben.

## Terug blik
Ik heb heel erg veel geleerd over AI in deze afgelopen dagen. Persoonlijk vind ik dat mijn aanpak goed was. Ik probeerde eerste de theorie van de dag op te schrijven, maar na dag 3 werd dat te veel. 

Na elke opdracht probeerde ik een conclusie te trekken over wat ik nou gedaan heb, en wat alles getekend. Dit was heel erg leerzaam voor mij, juist omdat we soms werkte uit klaargemaakte notebooks.

## AI als vakgebied
Met alles wat ik nu geleerd heb over AI, is mijn beeld zeer verbreed over hoe AI nu eigenlijk precies werkt achter de schermen. Nu dat ik eindelijk een beetje weet hoe het werkt, kan ik niet wachten om nog dieper in de stof de gaan, om steeds meer kennis op te doen over AI. Ook hebben we ethiek gehad over AI, wat ook zeer belangrijk is. Zelf heb ik al een verslag geschreven over deepfakes en daar gaat het ook veel over ethiek. Wat ik hier dus uithaal, is dat AI heel erg veel kracht heeft. En veel dingen kan doen, en je dus ook uit moet kijken met wat het *wel* en wat het *niet* kan doen. Al met al, kan ik niet wachter om verder te gaan met de minor.

## Leerdoelen

- Aan het einde van mijn minor wil ik weten wat voor machine learning technieken erzijn en hoe deze in elkaar zitten. Dit ga ik doen doormiddel van altijd mijn opdrachten te maken en samenvatting van de theorie te maken.

- Aan het eind van mijn minor moet ik weten wanneer ik wel en niet AI kan gebruiken, op basis van ethische redenen. Dit wil ik doen doormiddel van het ethiek onderdeel van de minor met een voldoende af te ronden.

- Aan het einde van mijn minor wil ik verschillende machine learning technieken kunnen toepassen op bepaalde problemen. Dit wil ik doen doormiddel om al mijn vakken/project succesvol af te ronden.

Dit zijn al mijn leerdoelen voor de rest van deze minor. Al deze leerdoelen zijn behaald als ik de minor succesvol heb afgerond en al mijn studiepunten binnen heb.