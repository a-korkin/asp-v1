import { AppDispatch } from "../.."
import { IUser } from "../../../models/user";
import UserService from "../../../services/user-service";
import { GetUserAction, UserActionsEnum } from "./types"

export const UsersActionCreators = {
    setUsers: (users: IUser[]): GetUserAction => ({ type: UserActionsEnum.GET_USERS, payload: users}),
    fetchUsers: () => async (dispatch: AppDispatch) => {
        try {
            const response = await UserService.fetchUsers();
            dispatch(UsersActionCreators.setUsers(response.data));
        } catch (e) {
            console.log(e);
        }
    }
}