

    const btnCart = document.getElementsByClassName('update-cart');
    for (i = 0 ; i < btnCart.length ; i++){
        btnCart[i].addEventListener('click' , async function(event) {
            const productId = this.dataset.product;
            const action = this.dataset.action;
            if (user === 'AnonymousUser'){
                console.log('not logged in')
            }
            else{
                
                const url = '/update-cart/';
                const options ={
                    method : 'POST',
                    headers : {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken,
                    },
                    body: JSON.stringify({'productId': productId , 'action':action}),
                }
                response = await fetch(url , options);
                data = await response.json()    
                const countEle = document.getElementById('count');
                countEle.textContent = data['TotalCount'] ;
                // location.reload()
            }
        });
    }

