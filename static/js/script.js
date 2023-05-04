var cartProducts = []
var cartQuantity = document.getElementsByClassName("cart-quantity")[0];
var cartBox = document.getElementsByClassName("cart")[0];
if(localStorage.getItem("cartProducts")) {
    cartProducts = JSON.parse(localStorage.getItem("cartProducts"));
    cartQuantity.textContent = cartProducts.length;
    cartBox.style.display = "block";
}

function clickProduct(productId) {
    return function() {
        cartProducts.push(productId);
        localStorage.setItem("cartProducts", JSON.stringify(cartProducts));
        cartQuantity.textContent = cartProducts.length;
        cartBox.style.display = "block";
    }
}

function getCartProducts() {
    if(localStorage.getItem("cartProducts")) {
        cartProducts = localStorage.getItem("cartProducts");
    }
    return cartProducts
}

function openCart() {
    let data = getCartProducts();
    data2 = JSON.parse(localStorage.getItem("cartProducts"));
    let url = '/cart?' + encodeURIComponent(data2);
    window.location.href = url;
}

window.onload = function() {
  var products = document.getElementsByClassName("products");
  for(let product of products) {
        let productId = product.querySelector(".single_menu").id;
        product.addEventListener("click", clickProduct(productId));
  }
  cartBox.addEventListener("click", openCart);
};