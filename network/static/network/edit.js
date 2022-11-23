


document.addEventListener('DOMContentLoaded', function() {

        document.querySelectorAll('.edit_post').forEach(button => {
            button.onclick = function(event) {
                let element = event.target;
                var postId = element.dataset.editpostid;
                let content = element.parentNode.parentNode.querySelector('.post_content').innerHTML;
                if (content){
                    document.querySelector('#id_content').value = content;
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }
                if (!document.querySelector('#save_editPost')) {
                    create_tagEdit(postId);
                }

                else{
                    input = document.querySelector('#save_editPost');
                    let onclickfunc = `edit_post(${postId})`;
                    input.setAttribute("onclick", onclickfunc);
                }
            };
        });

      });

      function edit_post(postId) {

        const csrftoken = getCookie('csrftoken');
        let content = document.querySelector('#id_content').value;

        fetch(`/edit_post`,{
            method: 'POST',
            headers:{
              'Accept': 'application/json',
              'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
              'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({'post_id':postId,'content':content})
        }).then(response => response.json())
        .then(data =>{
            
            if(data.status === 200)
            {
                document.querySelector('#id_content').value = '';
                document.getElementById(`post_${postId}`).innerHTML = content;
                create_tagPost();
            }
            else
            {
               alert(data.message);    
            }
           
        })
    };


    function create_tagPost(){
        var input = document.createElement("INPUT");
        input.setAttribute("type", "submit");
        input.setAttribute("class", "btn btn-primary mt-3");
        input.setAttribute("id", "save_createPost");
        input.value = "Post";
        document.querySelector('#form_newPost').appendChild(input);
        document.querySelector('#save_editPost').remove();
    }

    function create_tagEdit(postId){
        var input = document.createElement("INPUT");
        input.setAttribute("type", "button");
        input.setAttribute("class", "btn btn-primary mt-3");
        input.setAttribute("id", "save_editPost");
        input.value = "Edit";
        let onclickfunc = `edit_post(${postId})`;
        input.setAttribute("onclick", onclickfunc);
        document.querySelector('#form_newPost').appendChild(input);
        document.querySelector('#save_createPost').remove();
    }