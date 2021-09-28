import { IUserState, UserAction, UserActionsEnum } from "./types"

const initialState: IUserState = {
    users: []
}

export const usersReducer = (state: IUserState = initialState, action: UserAction): IUserState => {
    switch (action.type) {
        case UserActionsEnum.GET_USERS:
            return { users: action.payload };
        default:
            return state;
    }
}
