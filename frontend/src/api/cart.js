/* eslint-disable prettier/prettier */
import Cookies from "js-cookie";
import router from "@/router";

export const getCart = async () => {
  const cart = Cookies.get("cart");
  return cart ? JSON.parse(cart) : [];
};

async function setCartCookie(products) {
  const cart = JSON.stringify(products);
  const expirationDate = new Date(new Date().getTime() + 24 * 60 * 60 * 1000);
  Cookies.set("cart", cart, {
    expires: expirationDate,
    path: "/",
    sameSite: "strict",
  });
}

export const addToCart = async (productObj) => {
  let cart = await getCart();
  const existingProduct = cart.find((product) => product.id === productObj.id);
  if (existingProduct) {
    existingProduct.quantity++;
  } else {
    cart.push({
      id: productObj.id,
      quantity: 1,
      name: productObj.name,
      price: productObj.price,
      image: productObj.images[0] ? productObj.images[0].image : null,
    });
  }
  await setCartCookie(cart);
  console.log(productObj.id, "ADDED");
  return getCart();
};

export const removeFromCart = async (productId) => {
  let cart = await getCart();
  console.log(productId)
  const productIndex = cart.findIndex((product) => product.id === productId);
  console.log(productIndex);
  if (cart[productIndex].quantity > 1) {
    cart[productIndex].quantity--;
  } else {
    cart.splice(productIndex, 1);
  }
  await setCartCookie(cart);
  console.log(productId, "DECREASED");

  return getCart();
};

export const getCartCount = async () => {
  const cart = await getCart();
  let count = 0;
  for (const product of cart) {
    count += product.quantity;
  }
  return count;
};

export const clearCart = async () => {
  try {
    document.cookie = "cart=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    router.push("/");
  } catch (error) {
    console.log(error.response.data);
  }
};
