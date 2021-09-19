import { IUser } from "../../../models/user";
import { AuthAction, AuthActionEnum, IAuthState } from "./types";

const initialState: IAuthState = {
    isAuth: false,
    isLoading: false,
    error: "",
    user: {} as IUser
}

export const authReducer = (state: IAuthState = initialState, action: AuthAction): IAuthState => {
    switch (action.type) {
        case AuthActionEnum.SET_LOADING:
            return { ...state, isLoading: action.payload };
        case AuthActionEnum.SET_ERROR:
            return { ...state, error: action.payload, isLoading: false };
        case AuthActionEnum.SET_AUTH:
            return { ...state, isAuth: action.payload, isLoading: false };
        case AuthActionEnum.SET_USER:
            return { ...state, user: action.payload }            
        default:
            return state;
    }
}
