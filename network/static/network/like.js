


document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.likes').forEach(button => {
            button.onclick = function(event) {

                let element = event.target;
                let post_id = element.dataset.postid;
                const csrftoken = getCookie('csrftoken');

                fetch(`/like_post/${post_id}`, {
                    method: 'POST',
                    headers:{
                        'Accept': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
                        'X-CSRFToken': csrftoken,
                      }
                }).then(response => response.json())
                .then(data => {
                    
                    if(data.status === 200)
                    {
                        if(element.classList.contains('press'))
                        {
                            element.classList.remove( "press", 1000 );
                        }
                        else{
                            element.classList.toggle( "press", 1000 );
                        }
                        element.parentNode.querySelector('span').innerHTML = data.likes;
                    }
                    else
                    {
                       alert(data.message);    
                    }
                    
                })

               
            };
        });


      });

     