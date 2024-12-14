
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
                        <button onClick="editFilm(${i})">Редактировать</button>
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

function showModal(){
    document.querySelector('div.modal').style.display = 'block'
}

function hideModal(){
    document.querySelector('div.modal').style.display = 'none'
}

function cancel(){
    hideModal()
}

function addFilm() {
    showModal()
}

function sendFilm() {
    const id = document.getElementById('id').value
    const film = {
        title: document.getElementById('title').value,
        title_ru: document.getElementById('title-ru').value,
        year: document.getElementById('year').value,
        description: document.getElementById('description').value
    }

    fetch(`/lab7/rest-api/films/${id}`, {
    method: id === '' ? 'POST' : 'PUT',
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify(film)
    })
    .then(function () {
    fillFilmList();
    hideModal();
    })
}

function editFilm(id){
    fetch(`/lab7/rest-api/films/${id}`)
    .then(function (data){
        return data.json()
    })
    .then(function (film){
        document.getElementById('id').value = id;
        document.getElementById('title').value = film.title;
        document.getElementById('title-ru').value = film.title_ru;
        document.getElementById('year').value = film.year;
        document.getElementById('description').value = film.description;
        showModal();

    })
}
