## Rules
1. Use branches (NOT) https://guides.github.com/introduction/flow/

## DOTO
    * Update Blog
    * Wireframe
    * UX Design
    * System Model (Visual Paradigm Community Edition)
    * Framework

## Software
1. Visual Paradigm Community Edition https://www.visual-paradigm.com/download/community.jsp

## Backen-end arendaja õpi
- ES6
- Node.js
  - Handlebars (hbs) templates
  - Node.js express
  - Jason web tokens
  - Passport + passport-jwt

## Kaustad
- /bin
  - www fail ütleb kuidas server tööle läheb
- /config
  - Vahekihtide config failid
- /controllers
  - Funktsioonid sisuliselt ja kuidas mis lehele suunata
- /middleware
  - Vahekihtide seaded
- /models
  - suhtleb veel andmebaasiga kuidagi :)
- /public
  - Staatilised failid
- /routes
  - Sisuliselt sama, mis controllers... peaks tulevikus kaustad kokku viima
- /views
  - On dünaamilised template failid ehk vaated
- app.js on see fail mis tõmmatakse www faili järel käima, võiks äkki õelda et main() ;) vist lolz

## Keskkonna käivitamine
- Klooni või tiri kaust arvutisse
- Paigalda arvutisse uusim node.js
- Käivita `npm install` mis paigaldab vajalikud moodulid package.json failist.
- Googelda ja paigalda nodemon (`npm install nodemon` vist)
- Liigu projekti kausta ja kirjuta `nodemon bin/www`
  - See võimaldab arendada samal ajal kui server jookseb. Pole vajalik aga väga mugav abiline.