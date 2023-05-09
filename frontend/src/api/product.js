/* eslint-disable prettier/prettier */
// import router from "@/router";
import axiosInstance from "@/api/api.config";
import Cookies from 'js-cookie';


export const productList = async (filters, page) => {
  try {
    const response = await axiosInstance.get("/products/", { params: { categories: filters, page: page } });
    return response.data;
  } catch (error) {
    console.log(error.response.data);
  }
};

export const productArticle = async (id) => {
  try {
    const response = await axiosInstance.get(`/products/${id}/`)
    return response.data;
  } catch (error) {
    console.log(error.response.data);
  }
}

export function getCartProductsFromCookie() {
  const cartProducts = Cookies.get('cartProducts');
  return cartProducts ? JSON.parse(cartProducts) : [];
};
