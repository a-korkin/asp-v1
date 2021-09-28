import React, { FC } from "react";
import { useActions } from "../hooks/use-actions";
import { useTypedSelector } from "../hooks/use-typed-selector";

const PrivatePage: FC = () => {
    const { logout } = useActions();
    const { user, isAuth } = useTypedSelector(state => state.auth);
    return (
        <div>
            <h1>Private page</h1>
            <p>{isAuth}</p>
            <h2>user: {user.username}</h2>
            <button onClick={logout}>logout</button>
        </div>
    );
}

export default PrivatePage;
