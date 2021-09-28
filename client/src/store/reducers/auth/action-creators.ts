import axios from "axios";
import { AppDispatch } from "../..";
import { API_URL } from "../../../http";
import { AuthResponse } from "../../../models/response/auth-response";
import { IUser } from "../../../models/user";
import AuthService from "../../../services/auth-service";
import { AuthActionEnum, SetErrorAction, SetIsAuthAction, SetIsLoadingAction, SetUserAction } from "./types";

export const AuthActionCreators = {
    setIsLoading: (loading: boolean): SetIsLoadingAction => ({ type: AuthActionEnum.SET_LOADING, payload: loading }),
    setIsAuth: (auth: boolean): SetIsAuthAction => ({ type: AuthActionEnum.SET_AUTH, payload: auth }),
    setError: (error: string): SetErrorAction => ({ type: AuthActionEnum.SET_ERROR, payload: error }),
    setUser: (user: IUser): SetUserAction => ({ type: AuthActionEnum.SET_USER, payload: user}),
    login: (username: string, password: string) => async (dispatch: AppDispatch) => {
        try {
            dispatch(AuthActionCreators.setIsLoading(true));
            const response = await AuthService.login(username, password);
            localStorage.setItem("token", response.data.accessToken);
            dispatch(AuthActionCreators.setIsAuth(true));
            dispatch(AuthActionCreators.setUser(response.data.user))
        } catch (e) {
            dispatch(AuthActionCreators.setError("Произошла ошибка при авторизации"));
        } finally {
            dispatch(AuthActionCreators.setIsLoading(false));
        }
    },
    logout: () => async (dispatch: AppDispatch) => {
        await AuthService.logout();
        localStorage.removeItem("token");
        dispatch(AuthActionCreators.setIsAuth(false));
        dispatch(AuthActionCreators.setUser({} as IUser));
    },
    checkAuth: () => async (dispatch: AppDispatch) => {
        try {
            dispatch(AuthActionCreators.setIsLoading(true));
            const response = await axios.get<AuthResponse>(`${API_URL}/refresh`, {withCredentials: true});
            localStorage.setItem("token", response.data.accessToken);
            dispatch(AuthActionCreators.setIsAuth(true));
            dispatch(AuthActionCreators.setUser(response.data.user));
        } catch (e) {
            dispatch(AuthActionCreators.setError("Произошла ошибка при авторизации"));
        } finally {
            dispatch(AuthActionCreators.setIsLoading(false));
        }
    }
}
