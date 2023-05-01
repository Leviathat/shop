/* eslint-disable prettier/prettier */
import axiosInstance from "@/api/api.config";
import router from "@/router";

export const registerUser = async (user) => {
  const data = {
    user: user,
  };
  try {
    const response = await axiosInstance.post("/users/register/", data);
    router.push("/login");
    setToken(response.data.user.token);
    return response.data.user;
  } catch (error) {
    console.log(error.response.data);
  }
};

export const loginUser = async (user) => {
  try {
    const response = await axiosInstance.post("/users/login/", user);
    setToken(response.data.user.token);
    return response.data.user;
  } catch (error) {
    console.log(error);
  }
};

export const userInfo = async () => {
  try {
    const response = await axiosInstance.get("/users/info/");
    return response.data;
  } catch (error) {
    console.log(error.response.data);
  }
};

export const logoutUser = async () => {
  try {
    document.cookie = 'auth_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
    router.push("/login");
  } catch (error) {
    console.log(error.response.data);
  }
};

const setToken = async (new_token) => {
  const token = new_token;
  const expirationDate = new Date(new Date().getTime() + 7 * 24 * 60 * 60 * 1000);
  document.cookie = `auth_token=${token}; expires=${expirationDate.toUTCString()}; path=/`;
}