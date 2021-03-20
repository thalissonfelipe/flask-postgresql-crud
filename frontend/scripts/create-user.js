const completeName = document.getElementById('name');
const age = document.getElementById('age');
const street = document.getElementById('street');
const number = document.getElementById('number');
const city = document.getElementById('city');
const state = document.getElementById('state');
const btnCreate = document.getElementById('btnCreate');

btnCreate.addEventListener('click', async e => {
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

    const response = await createUser(body);
    if (response.status === 201) {
        alert('Usuário criado!');
    } else {
        alert(response.statusText);
    }
});

async function createUser(body) {
    const response = await fetch('http://localhost:5000/api/v1/users', {
        method: 'POST',
        headers: new Headers({
            'Content-Type': 'application/json'
        }),
        body: JSON.stringify(body)
    });

    return response;
}
