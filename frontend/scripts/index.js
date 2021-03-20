window.onload = async () => {
    await loadUsers();
    setButtonEvents();
}

async function fetchUsers() {
    const response = await fetch('http://localhost:5000/api/v1/users', {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json'
        })
    });
    const data = await response.json();
    return data;
}

async function deleteUser(id) {
    await fetch(`http://localhost:5000/api/v1/users/${id}`, { method: 'DELETE' });
}

async function loadUsers() {
    const users = await fetchUsers();
    const usersList = document.querySelector('.users-list');
    usersList.innerHTML = '';

    users.forEach(user => {
        usersList.insertAdjacentHTML('beforeend',
            '<div class="users-list__item">' +
                '<div class="item__left">' +
                    `<span>Name: ${user.name}</span>` +
                    `<span>Idade: ${user.age}</span>` +
                    '<address>' +
                        `${user.address.street}, ${user.address.number} - ${user.address.city}, ${user.address.state}` +
                    '</address>' +
                '</div>' +
                '<div class="item__right">' +
                    `<a data-id=${user.id} href="update-user.html?id=${user.id}" class="btn btn--update">Editar</a>` +
                    `<button data-id=${user.id} class="btn btn--remove">Remover</button>` +
                '</div>' +
            '</div>'
        );
    });
}

function setButtonEvents() {
    const btnNo = document.getElementById('btnNo');
    const btnYes = document.getElementById('btnYes');
    const btnRemove = document.querySelectorAll('.btn--remove');
    const modal = document.getElementById('modal');

    btnNo.addEventListener('click', closeModal);

    btnYes.addEventListener('click', yesBtnListener);

    btnRemove.forEach(btn => btn.addEventListener('click', e => {
        modal.setAttribute('userid', e.target.dataset.id);
        openModal();
    }));
}

async function yesBtnListener() {
    const id = modal.getAttribute('userid');
    await deleteUser(id);
    closeModal();
    updateEvents();
}

async function updateEvents() {
    await loadUsers();
    setButtonEvents();
}

function closeModal() {
    document.querySelector('.overlay').style.display = 'none';
}

function openModal() {
    document.querySelector('.overlay').style.display = 'flex';
}
