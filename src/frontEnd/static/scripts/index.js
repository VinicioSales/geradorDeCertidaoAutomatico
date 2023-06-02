const razaoSocial = document.querySelector('.input')
const button = document.querySelector('#button')
const leftFeame = document.querySelector('.flashMessages')


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

