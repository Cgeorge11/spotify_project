
    //toggle burger menu

    let menu = document.querySelector("#burger");
    let navbar = document.querySelector(".navbar");

    menu.onclick =() =>{
        menu.classList.toggle("fa fa-smile-o"); //overrides css
        navbar.classList.toggle("active")
    }
    
    // Get the modal
    var modal = document.getElementById('id01');
    
    // clicks anywhere out to close
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }
  