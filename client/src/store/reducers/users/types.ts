import { IUser } from "../../../models/user";
import { ICommonState } from "../common/types";

// export interface IUserState extends ICommonState {
export interface IUserState extends ICommonState {
    isLoading: boolean;
    error: string;
    users: IUser[]
}

export enum UserActionsEnum {
    SET_LOADING = "SET_LOADING",
    SET_ERROR = "SET_ERROR",
    GET_USERS = "GET_USERS",
}

export interface GetUsersAction {
    type: UserActionsEnum.GET_USERS;
    payload: IUser[];
}

export interface SetIsLoadingAction {
    type: UserActionsEnum.SET_LOADING;
    payload: boolean;
}

export interface SetErrorAction {
    type: UserActionsEnum.SET_ERROR;
    payload: string;
}

export type UserAction = GetUsersAction | SetIsLoadingAction | SetErrorAction;
