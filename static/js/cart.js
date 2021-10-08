let add = document.getElementById('addtocart');

add.addEventListener('submit',async function(e){

	e.preventDefault();
	let csrf = form.csrfmiddlewaretoken.value
	console.log(form);
	let product = document.getElementById('addtocart').getAttribute('data-product')
	let quantity = document.getElementById('product-quantity').value
	let data = {
		'product': product,
		'quantity': quantity
	}

	let response = await fetch('http://localhost:8000/api/order/productcart/', {
		headers:{
			'content-type': 'application/json',
			"X-CSRFToken": csrf
		},
		method: 'POST',
		body: JSON.stringify(data)
	})
	let post_response = await response.json()
	console.log(post_response);
	
 	await getbasket()
})


async function getbasket() {

	let basket = document.getElementById('basket');

	let response_data = await fetch ('http://localhost:8000/api/order/productcart/')

	
	let post_response = await response_data.json()
	basket.innerHTML = ''
	for (let data of post_response) {
		basket.innerHTML += ` 
		<li>
		<div class="media">
			<a href="${data['product']['get_absolute_url']}"><img class="mr-3"
					src="${data['product']['image']}"
					alt="Generic placeholder image"></a>
			<div class="media-body">
				<a href="${data['product']['get_absolute_url']}">
					<h4>${data['product']['title']}</h4>
				</a>
				<h4><span>${data['quantity']} x $ ${data['product']['get_sale_price']}</span></h4>
			</div>
		</div>
		<div data-item ='${data['id']}'class="close-circle"><a href="#"><i  class="fa fa-times target"
					aria-hidden="true"></i></a></div>
		</li>` 
  	
	}
	
}







let wishlist = document.getElementById('addtowishlist');

wishlist.addEventListener('submit',async function(e){
	e.preventDefault();
	hrt = document.getElementById('heart');
	let csrf = form.csrfmiddlewaretoken.value
	if(!hrt.classList.contains('liked')){
		document.getElementById('heart').classList.add('liked')
	
	let product = document.getElementById('addtowishlist').getAttribute('data-product')

	let data = {
		'product': product,

	}
	let response = await fetch('http://localhost:8000/api/order/productwishlist/', {
				headers:{
					'content-type': 'application/json',
					"X-CSRFToken": csrf
				},
				method: 'POST',
				body: JSON.stringify(data)
			})

		let post_response = await response.json()
		wishlist.setAttribute('data-item',post_response['id']);
		console.log(post_response);
	}
	else{

		let wishlist_id = wishlist.getAttribute('data-item');
		let response = await fetch(`http://localhost:8000/api/order/productwishlist/${wishlist_id}`, {
				headers:{
					'content-type': 'application/json',
					"X-CSRFToken": csrf
				},
				method: 'DELETE',
			})

		hrt.classList.remove('liked')


	}
	
	


})


$( "#basket" ).click( async function(e){
	console.log(e.target);
	if(e.target.classList.contains('target')){
		$(e.target).parent().parent().parent().remove()
		let csrf = form.csrfmiddlewaretoken.value
		let cart_id = e.target.getAttribute('data-item');
		let response = await fetch(`http://localhost:8000/api/order/productcart/${cart_id}`, {
				headers:{
					'content-type':'application/json',
					"X-CSRFToken": csrf
				},
				method: 'DELETE',
			})

	}
	
		

});


