// let form = document.getElementById('subscribe-form')

// form.addEventListener('submit', function (e) {
//     e.preventDefault();
//     let form_data = {
//         'email':form.email.value,
//     }
//     let res = await fetch('http://localhost:8000/api/subscribe/',{
//         headers: {
//             'content-type': 'application/json',
//             'X-CSRFToken': form.csrfmiddlewaretoken.value
//         },
//         method: 'POST',
//         body: JSON.stringify(form_data)
//     })
//     let response_data = await response.json();
//     let status = await response.ok
//     console.log(response_data);
//     if(status === true){
//         alert('Abune oldun gaga')
//     }
//     else{
//         alert('Duzgun daxil et gaga')
//     }
// })




let form = document.getElementById('subscribe-form');
let error_section =  document.getElementById('error-list');
form.addEventListener('submit', async function (e) {
    e.preventDefault();
    error_section.innerText = '';
    let form_data = {
        'email': form.email.value
    }
    let response = await fetch('http://localhost:8000/api/subscribe/', {
        headers: {
            'content-type': 'application/json',
            "X-CSRFToken": form.csrfmiddlewaretoken.value
        },
        method: 'POST',
        body: JSON.stringify(form_data)
    })
    let response_data = await response.json();
    let status = await response.ok;
    
    if(status === true){
        alert('Ugurla abone oldunuz');
        document.getElementById('mce-EMAIL').value = ''
    }
    else{
        for(let error of response_data.email) {
           error_section.innerHTML += `<li class="text-danger">${error}</li>`  
        }
    }


}) 








let star = document.querySelectorAll("#ratingstar");
// console.log(star,"test");


star.forEach(e => {
    console.log(e.innerText)
    // e.innerText += '<i class="reviewstar fa fa-star"></i>'

})




