window.onload = () => loadUser();

const completeName = document.getElementById('name');
const age = document.getElementById('age');
const street = document.getElementById('street');
const number = document.getElementById('number');
const city = document.getElementById('city');
const state = document.getElementById('state');
const btnUpdate = document.getElementById('btnUpdate');

async function fetchUser() {
    const id = getQueryParameter('id');
    const response = await fetch(`http://localhost:5000/api/v1/users/${id}`, {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json'
        })
    });
    const data = await response.json();
    return data;
}

async function loadUser() {
    const user = await fetchUser();
    completeName.value = user.name;
    age.value = user.age;
    street.value = user.address.street;
    number.value = user.address.number;
    city.value = user.address.city;
    state.value = user.address.state;
}

function getQueryParameter(variable) {
    let query = decodeURIComponent(window.location.search.substring(1));
    let vars = query.split('&');

    for (let i = 0; i < vars.length; i++) {
        let pair = vars[i].split('=');
        if (pair[0] === variable) {
            return pair[1];
        }
    }
}

btnUpdate.addEventListener('click', async e => {
    e.preventDefault();
    const fields = [completeName, age, street, number, city, state];
    for (let index = 0; index < fields.length; index++) {
        if (!fields[index].value) return;
    }

    const body = {
        name: completeName.value,
        age: parseInt(age.value),
        address: {
            street: street.value,
            number: parseInt(number.value),
            city: city.value,
            state: state.value
        }
    };

    const response = await updateUser(body);
    if (response.status === 204) {
        alert('Usuário atualizado!');
        loadUser();
    } else {
        alert(response.statusText);
    }
});

async function updateUser(body) {
    const id = getQueryParameter('id');
    const response = await fetch(`http://localhost:5000/api/v1/users/${id}`, {
        method: 'PUT',
        headers: new Headers({
            'Content-Type': 'application/json'
        }),
        body: JSON.stringify(body)
    });

    return response;
}