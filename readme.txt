1.In prima faza am creat un excel in care am introdus un sumar a 10 teste manuale:
Avand trei calificative   ....  -> PASS
				-> FAILED
				-> 50/50

Am adaugat observatii la testele care aveau probleme!

2.In a doua faza am incercat sa automatizez testele de log-in cu datele reale si inexistente:
	Au fost ceva probleme cu ChromeDrive a trebuit de acceptat faptul ca nu merge bine testarea pe Windows si am continuat testele pe 
Ubuntu.
	Folosind biblioteca Selenium care am mai lucratin anterior o data si parca a mers atunci ok,de data asta mi-a dat mari batai de cap,eu nu fiind
un ultilizator de Chrome am incercat sa instalez un driver de Brave Browser sau Mozile FireFox la care nu a reusit nimic.
Codul python fiind gasit din diferite surse cum ar fi forumuri,avea un skelet destinat doar pentru un Browser Chrome.
In cele din urma am lasat idea de a rula pe un alt browser decat chrome,am optimizat codul pentru cele doua teste si in cele din urma a iesit ceva.

Sumar:Problema e ca la intrarea pe pagina de log-in a Facebook,apare pop-up cu obtiunea de acceptare a cookies (ce impedica la procesele mele de testare)
din cauza asta nu stiu cum sa automatizez acest proces! 