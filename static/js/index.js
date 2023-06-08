var modal = document.getElementsByClassName("modal")[0];
method = localStorage.getItem("method");
console.log(method);
if(method === null) {
    modal.style.display = 'block';
    console.log(method);
}

function selectMethod(method){
    localStorage.setItem("method", method);
    modal.style.display = 'none';
    method = localStorage.getItem("method");
    console.log(method);
}
