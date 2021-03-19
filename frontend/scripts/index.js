window.onload = () => {
    loadUsers();
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

async function loadUsers() {
    const users = await fetchUsers();
    const usersList = document.querySelector('.users-list');

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
                    '<button class="btn btn--update">Editar</button>' +
                    '<button class="btn btn--remove">Remover</button>' +
                '</div>' +
            '</div>'
        );
    });
}