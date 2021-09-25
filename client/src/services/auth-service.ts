import $api from "../http";
import { AxiosResponse } from "axios";
import { AuthResponse } from "../models/response/auth-response";

export default class AuthService {
    static async login(username: string, password: string): Promise<AxiosResponse<AuthResponse>> {
        return $api.post<AuthResponse>("/login", {username: username, password: password});
        // return $api.post<AuthResponse>("/login", {username: username, password: password}, {withCredentials: true});
    }

    static async logout(): Promise<void> {
        console.log("logout");
        return $api.post("/logout");
    }
}