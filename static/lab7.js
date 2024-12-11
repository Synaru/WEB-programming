
function fillFilmList() {
    fetch('/lab7/rest-api/films/')
    .then(function (data) {
        return data.json()
    })
    .then(function (films) {
        let tbody = document.getElementById('film-list');
        let content = ''
        let i = 0
        for(let film of films){
            content += `
                <tr>
                    <td>${film.title}</td>
                    <td>${film.title_ru}</td>
                    <td>${film.year}</td>
                    <td>${film.description}</td>
                    <td>
                        <button >Редактировать</button>
                        <button onClick="deleteFilm(${i})">Удалить</button>
                    </td>
                </tr>
            `
            i++
        }
        tbody.innerHTML = content
    })
}

function deleteFilm(id){
    if(!window.confirm(`Удалить фильм ?`)){
        return;
    }
    fetch(`/lab7/rest-api/films/${id}`, {
        method: 'DELETE'
    })
    .then(function (data) {
        fillFilmList()
    })
}