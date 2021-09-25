import $api from "../http";
import { AxiosResponse } from "axios";
import { AuthResponse } from "../models/response/auth-response";

export default class AuthService {
    static async login(username: string, password: string): Promise<AxiosResponse<AuthResponse>> {
        return $api.post<AuthResponse>("/login", {username, password});
    }

    static async logout(username: string): Promise<void> {
        return $api.post("/logout", {username});
    }
}