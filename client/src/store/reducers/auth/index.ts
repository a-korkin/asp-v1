
interface IAuthState {
    isAuth: boolean;
    isLoading: boolean;
    error: string;
}

const initialState: IAuthState = {
    isAuth: false,
    isLoading: false,
    error: ""
}

enum AuthActionEnum {
    SET_AUTH = "SET_AUTH",
    SET_ERROR = "SET_ERROR"
}
interface SetAuthAction {
    type: AuthActionEnum.SET_AUTH;
    payload: boolean;
}

export type AuthAction = SetAuthAction;

export const authReducer = (state: IAuthState = initialState, action: AuthAction): IAuthState => {
    switch (action.type) {
        default:
            return state;
    }
}
