import { login } from "./api.js";

document.getElementById("loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const nik = document.getElementById("nik").value;

    const res = await login({ nik });

    localStorage.setItem("user", JSON.stringify(res));

    window.location.href = "dashboard.html";
});