import { IUser } from "../user";

export interface AuthResponse {
    access_token: string;
    user: IUser;
}