import React, { FC, useEffect } from "react";
import { useActions } from "../hooks/use-actions";
import { useTypedSelector } from "../hooks/use-typed-selector";

const UserList: FC = () => {
    const { fetchUsers } = useActions();
    useEffect(() => {
        if (localStorage.getItem("token")) {
            fetchUsers();
        }
    }, []);

    const { users } = useTypedSelector(state => state.users);
    return (
        <div>
            <div>list of users</div>
            {
                users.map((user) => 
                    <div key={user.username}>{user.username}</div>)
            }
        </div>
    );
}

export default UserList;
