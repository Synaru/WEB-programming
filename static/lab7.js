
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
        let rowTag = (i % 2 === 0) ? '' : 'highlighted'
            content += `
                <tr class="${rowTag}">
                    <td>${film.title_ru}</td>
                    <td class="lower-value">(${film.title})</td>
                    <td>${film.year}</td>
                    <td>${film.description}</td>
                    <td>
                        <button onClick="editFilm(${i})">Редактировать</button>
                        <button class="danger" onClick="deleteFilm(${i})">Удалить</button>
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
    document.getElementById('description-error').innerText = '';
    document.querySelector('div.modal').style.display = 'block'
}
function hideModal(){
    document.querySelector('div.modal').style.display = 'none'
}
function cancel(){
    hideModal()
}
function addFilm() {
    document.getElementById('id').value = '';
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
    .then(function (resp) {
        if(resp.ok){
            fillFilmList();
            hideModal();
            return {}
        }
        return resp.json()
    })
    .then(function (errors) {
        if(errors.description){
            document.getElementById('description-error').innerText = errors.description;
        }
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
