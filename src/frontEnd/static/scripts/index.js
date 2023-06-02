const razaoSocial = document.querySelector('.input')
const button = document.querySelector('#button')
const leftFeame = document.querySelector('.flashMessages')
const dropdownContent = document.querySelector('.dropdown-content')

let nomeClientes = [];

// Get the list of client names when the page loads
fetch('http://localhost:5000/get_nome_clientes')
    .then(response => response.json())
    .then(data => nomeClientes = data);

razaoSocial.addEventListener('input', () => {
    const searchTerm = razaoSocial.value.toLowerCase();

    // Filter the list of client names based on the search term
    const filteredClientes = nomeClientes.filter(cliente =>
        cliente.toLowerCase().includes(searchTerm)
    );

    dropdownContent.innerHTML = '';

    for (let i=0; i<filteredClientes.length; i++) {
        const div = document.createElement('div');
        div.innerHTML = filteredClientes[i];
        dropdownContent.appendChild(div);
    }
});

button.addEventListener('click', () => {
    event.preventDefault();
    
    const razaoSocialValor = razaoSocial.value;
    fetch('http://localhost:5000/gerar_certidao', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(razaoSocialValor)
    }).then(response => response.json())
    .then(data => {
        console.log(data.message)
        leftFeame.innerHTML = data.message;
    })
    .catch(error => {
        console.log(error)
    });
});
