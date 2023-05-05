/* eslint-disable prettier/prettier */
import axiosInstance from "@/api/api.config";
import { clearCart } from "./cart";

export const makeOrder = async (data) => {
  try {
    const response = await axiosInstance.post("/order/new/", data);
    await clearCart()
    return response.data.order;
  } catch (error) {
    console.log(error.response.data);
  }
};

export const getOrders = async () => {
  try {
    const response = await axiosInstance.get("/order/");
    return response.data.order;
  } catch (error) {
    console.log(error.response.data);
  }
};

export const patchCancelOrder = async (data) => {
  try {
    const response = await axiosInstance.patch("/order/cancel/", data);
    return response.data.order;
  } catch (error) {
    console.log(error.response.data);
  }
};
