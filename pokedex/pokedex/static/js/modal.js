/* fonction qui fetch les données d'un pokémon avec son id */
async function get_data(value) {

    modal = document.getElementById(`ModalBody${value}`);
    list = document.getElementById(`ModalList${value}`);

    const url = `https://pokeapi.co/api/v2/pokemon/${value}/`;

    let resp = await fetch(url,
        { headers: { 'Content-Type': 'application/json' } });
    let data = await resp.json();

    modal.innerHTML = `<p>weight: ${data.weight} <br> height: ${data.height}</p>`;
    html = [];

    for (let i = 0; i < data.stats.length; i++) {

        html += `<ul><li>${data.stats[i].stat.name}: ${data.stats[i].base_stat}</li><li>effort: ${data.stats[i].effort}</li></ul>`
    }
    list.innerHTML = html;
}