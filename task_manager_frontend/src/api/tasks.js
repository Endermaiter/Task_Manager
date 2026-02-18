import axios from "axios";

const API_URL = "http://localhost:8000/api";

export const getFamilies = async () => {
  const response = await axios.get(`${API_URL}/families/`);
  return response.data;
};

export const getTasks = async () => {
  const response = await axios.get(`${API_URL}/tasks/`);
  return response.data;
};

export const createTask = async (task) => {
  const response = await axios.post(`${API_URL}/tasks/`, task);
  return response.data;
};

export const updateTask = async (taskId, task) => {
  const response = await axios.patch(`${API_URL}/tasks/${taskId}/`, task);
  return response.data;
};

export const deleteTask = async (taskId) => {
  const response = await axios.delete(`${API_URL}/tasks/${taskId}/`);
  return response.data;
};
