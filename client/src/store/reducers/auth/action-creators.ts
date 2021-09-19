import { AppDispatch } from "../..";
import { AuthActionEnum, SetErrorAction, SetIsAuthAction, SetIsLoadingAction } from "./types";

export const AuthActionCreators = {
    setIsLoading: (loading: boolean): SetIsLoadingAction => ({ type: AuthActionEnum.SET_LOADING, payload: loading }),
    setIsAuth: (auth: boolean): SetIsAuthAction => ({ type: AuthActionEnum.SET_AUTH, payload: auth }),
    setError: (error: string): SetErrorAction => ({ type: AuthActionEnum.SET_ERROR, payload: error }),
    login: (username: string, password: string) => async (dispatch: AppDispatch) => {
        try {
            dispatch(AuthActionCreators.setIsLoading(true));
            setTimeout(() => {
                dispatch(AuthActionCreators.setIsLoading(false));
                // dispatch(AuthActionCreators.setError("ошибка блять"));
                dispatch(AuthActionCreators.setIsAuth(true));
            }, 1000);
        } catch (e) {
            dispatch(AuthActionCreators.setError("Произошла ошибка при авторизации"));
        }
    }
}
