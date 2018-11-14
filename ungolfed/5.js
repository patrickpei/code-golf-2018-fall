const cheerio = require('cheerio');
const fetch = require('node-fetch');

async function main() {
    let increment = 1;
    while (increment < 82) {
        const base = 'https://www.collegesimply.com/colleges/search?sort=largest&place=&sat=&act=&major=&radius=300&zip=&state=tennessee&size=&tuition-fees=&net-price=&start=';
        const url = `${base}${increment.toString().padStart(2, '0')}`;
        const response = await fetch(url);
        
        const text = await response.text();
        const $ = cheerio.load(text);
        const cards = $('.search-result-card-title');
        cards.map(i => {
            console.log(cards[i].children[0].data);
        });

        increment += 10;
    }
}

main();

