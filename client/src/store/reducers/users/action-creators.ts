import { AppDispatch } from "../.."
import { IUser } from "../../../models/user";
import UserService from "../../../services/user-service";
import { GetUsersAction, UserActionsEnum, SetIsLoadingAction, SetErrorAction } from "./types"

export const UsersActionCreators = {
    setIsLoading: (loading: boolean): SetIsLoadingAction => ({ type: UserActionsEnum.SET_LOADING, payload: loading }),
    setError: (error: string): SetErrorAction => ({ type: UserActionsEnum.SET_ERROR, payload: error }),
    setUsers: (users: IUser[]): GetUsersAction => ({ type: UserActionsEnum.GET_USERS, payload: users}),
    fetchUsers: () => async (dispatch: AppDispatch) => {
        try {
            dispatch(UsersActionCreators.setIsLoading(true));
            setTimeout(async () => {
                const response = await UserService.fetchUsers();
                dispatch(UsersActionCreators.setUsers(response.data));
            }, 5000);
        } catch (e) {
            dispatch(UsersActionCreators.setError("Произошла ошибка загрузки пользователей"));
        } finally {
            dispatch(UsersActionCreators.setIsLoading(false));
        }
    }
}