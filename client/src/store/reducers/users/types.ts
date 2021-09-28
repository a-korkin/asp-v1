import { IUser } from "../../../models/user";

export interface IUserState {
    users: IUser[]
}

export enum UserActionsEnum {
    GET_USERS = "GET_USERS"
}

export interface GetUserAction {
    type: UserActionsEnum.GET_USERS,
    payload: IUser[]
}

export type UserAction = GetUserAction;
