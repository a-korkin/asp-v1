import { AuthActionCreators } from "./auth/action-creators";
import { UsersActionCreators } from "./users/action-creators";

export const actionCreators = {
    ...AuthActionCreators,
    ...UsersActionCreators
}
