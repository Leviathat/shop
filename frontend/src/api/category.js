/* eslint-disable prettier/prettier */
import axiosInstance from "@/api/api.config";

export const categoryList = async () => {
  try {
    const response = await axiosInstance.get("/products/categories/");
    return response.data.category;
  } catch (error) {
    console.log(error.response.data);
  }
};