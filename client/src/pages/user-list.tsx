import React, { FC, useEffect } from "react";
import { useActions } from "../hooks/use-actions";
import { useTypedSelector } from "../hooks/use-typed-selector";

const UserList: FC = () => {
    const { fetchUsers } = useActions();
    const { users, isLoading } = useTypedSelector(state => state.users);
    useEffect(() => {
        fetchUsers();
    }, []); // eslint-disable-line react-hooks/exhaustive-deps

    console.log(users);
    console.log(isLoading);

    return (
        isLoading 
        ?
        <div>Загрузка...</div>
        :
        <div>
            <div>user list</div>
            {users.map((user, index) => <div key={index}>{user.username}</div>)}
        </div>
    );
}

export default UserList;
