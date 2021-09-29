import React, { FC, useEffect } from "react";
import { useActions } from "../hooks/use-actions";
import { useTypedSelector } from "../hooks/use-typed-selector";

const UserList: FC = () => {
    const { fetchUsers } = useActions();
    useEffect(() => {
        fetchUsers();
    }, []);

    const { users } = useTypedSelector(state => state.users);

    return (
        <div>
            {users.map((user, index) => <div key={index}>{user.username}</div>)}
        </div>
    );
}

export default UserList;
