import { AppDispatch } from "../..";
import AuthService from "../../../services/auth-service";
import { AuthActionEnum, SetErrorAction, SetIsAuthAction, SetIsLoadingAction } from "./types";

export const AuthActionCreators = {
    setIsLoading: (loading: boolean): SetIsLoadingAction => ({ type: AuthActionEnum.SET_LOADING, payload: loading }),
    setIsAuth: (auth: boolean): SetIsAuthAction => ({ type: AuthActionEnum.SET_AUTH, payload: auth }),
    setError: (error: string): SetErrorAction => ({ type: AuthActionEnum.SET_ERROR, payload: error }),
    login: (username: string, password: string) => async (dispatch: AppDispatch) => {
        try {
            dispatch(AuthActionCreators.setIsLoading(true));
            dispatch(AuthActionCreators.setIsLoading(false));

            const response = await AuthService.login(username, password);
            localStorage.setItem("token", response.data.accessToken);
            dispatch(AuthActionCreators.setIsAuth(true));
        } catch (e) {
            dispatch(AuthActionCreators.setError("Произошла ошибка при авторизации"));
        }
    }
}
