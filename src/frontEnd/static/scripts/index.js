const razaoSocial = document.querySelector('.input')
const button = document.querySelector('#button')


button.addEventListener('click', () => {
    const razaoSocialValor = razaoSocial.value;
    console.log(razaoSocialValor)
    fetch('http://localhost:5000/gerar_certidao', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(razaoSocialValor)
    }).then(response => {})

})

