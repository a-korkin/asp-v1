import { IUser } from "../../../models/user";
import { ICommonState } from "../common/types";

export interface IUserState extends ICommonState {
    users: IUser[]
}

export enum UserActionsEnum {
    SET_LOADING = "SET_LOADING",
    SET_ERROR = "SET_ERROR",
    GET_USERS = "GET_USERS",
}

export interface GetUserAction {
    type: UserActionsEnum.GET_USERS;
    payload: IUser[];
}

export interface SetLoadingAction {
    type: UserActionsEnum.SET_LOADING;
    payload: boolean;
}

export interface SetErrorAction {
    type: UserActionsEnum.SET_ERROR;
    payload: string;
}

export type UserAction = GetUserAction | SetLoadingAction | SetErrorAction;
