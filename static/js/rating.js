document.querySelectorAll(".rating").forEach(function(container){

    const fieldName = container.dataset.name;

    const hiddenInput = document.getElementById(fieldName);

    for(let i=1;i<=5;i++){

        let star=document.createElement("span");

        star.innerHTML="★";

        star.dataset.value=i;

        container.appendChild(star);

    }

    const stars=container.querySelectorAll("span");

    stars.forEach(function(star){

        star.addEventListener("click",function(){

            hiddenInput.value=this.dataset.value;

            stars.forEach(function(s){

                s.classList.remove("active");

            });

            for(let i=0;i<this.dataset.value;i++){

                stars[i].classList.add("active");

            }

        });

    });

});