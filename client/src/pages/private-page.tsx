import React, { FC } from "react";
import { useActions } from "../hooks/use-actions";

const PrivatePage: FC = () => {
    const {logout} = useActions();
    return (
        <div>
            <h1>Private page</h1>
            <button onClick={logout}>logout</button>
        </div>
    );
}

export default PrivatePage;
