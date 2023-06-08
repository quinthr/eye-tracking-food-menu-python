/* Set rates + misc */
var taxRate = 0.00;
var shippingRate = 0;
var fadeTime = 300;
var cartProducts = []
if(localStorage.getItem("cartProducts")) {
    cartProducts = JSON.parse(localStorage.getItem("cartProducts"));
}


/* Assign actions */
$('.product-quantity input').change( function() {
  updateQuantity(this);
});

$('.product-removal button').click( function() {
  removeItem(this);
});


/* Recalculate cart */
function recalculateCart()
{
  total = document.getElementById('cart-total').textContent;
  localStorage.setItem("total", total);
  console.log(localStorage.getItem("total"));
}


/* Update quantity */
function updateQuantity(quantityInput)
{
  /* Calculate line price */
  var productRow = $(quantityInput).parent().parent();
  var price = parseFloat(productRow.children('.product-price').text());
  var quantity = $(quantityInput).val();
  var linePrice = price * quantity;

  /* Update line price display and recalc cart totals */
  productRow.children('.product-line-price').each(function () {
    $(this).fadeOut(fadeTime, function() {
      $(this).text(linePrice.toFixed(2));
      recalculateCart();
      $(this).fadeIn(fadeTime);
    });
  });
}

function removeProduct(productId) {
    console.log(productId);
    cartProducts = cartProducts.filter(string => string !== productId);
    console.log(cartProducts);
    console.log(cartProducts.length)
    if(cartProducts.length == 0) {
        localStorage.removeItem('cartProducts');
    }
    else {
        localStorage.setItem("cartProducts", JSON.stringify(cartProducts));
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
    let url = '/';
    if (localStorage.getItem("cartProducts")) {
        data2 = JSON.parse(localStorage.getItem("cartProducts"));
        url = '/cart?' + encodeURIComponent(data2);
    }
    window.location.href = url;
}


/* Remove item from cart */
function removeItem(removeButton)
{
  /* Remove row from DOM and recalc cart total */
  var productRow = $(removeButton).parent().parent();
  var productId = $(removeButton).attr('id');
  productRow.slideUp(fadeTime, function() {
    productRow.remove();
    recalculateCart();
    removeProduct(productId);
    openCart();
  });
}