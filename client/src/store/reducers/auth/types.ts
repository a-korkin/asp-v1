import { IUser } from "../../../models/user";

export interface IAuthState {
    isAuth: boolean;
    isLoading: boolean;
    error: string;
    user: IUser;
}

export enum AuthActionEnum {
    SET_LOADING = "SET_LOADING",
    SET_AUTH = "SET_AUTH",
    SET_ERROR = "SET_ERROR",
    SET_USER = "SET_USER"
}

export interface SetIsLoadingAction {
    type: AuthActionEnum.SET_LOADING;
    payload: boolean;
}

export interface SetIsAuthAction {
    type: AuthActionEnum.SET_AUTH;
    payload: boolean;
}

export interface SetUserAction {
    type: AuthActionEnum.SET_USER;
    payload: IUser;
}

export interface SetErrorAction {
    type: AuthActionEnum.SET_ERROR;
    payload: string;
}

export type AuthAction = SetIsLoadingAction | SetIsAuthAction | SetUserAction | SetErrorAction;