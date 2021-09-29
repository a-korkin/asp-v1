import { IUserState, UserAction, UserActionsEnum } from "./types"

const initialState: IUserState = {
    isLoading: false,
    error: "",
    users: []
}

export const usersReducer = (state: IUserState = initialState, action: UserAction): IUserState => {
    switch (action.type) {
        case UserActionsEnum.SET_LOADING:
            return { ...state, isLoading: action.payload };
        case UserActionsEnum.SET_ERROR:
            return { ...state, error: action.payload };
        case UserActionsEnum.GET_USERS:
            return { ...state, users: action.payload };
        default:
            return state;
    }
}
