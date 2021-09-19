import React, { FC, useState } from "react";
import { useActions } from "../../hooks/use-actions";
import { useTypedSelector } from "../../hooks/use-typed-selector";
import "./style.css";

const LoginForm: FC = () => {
    const { error, isLoading } = useTypedSelector(state => state.auth);
    const [username, setUsername] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const { login } = useActions()

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        login(username, password);
    }

    return (
        <div className="ui card login_form">
            {error && <div className="ui red message">{error}</div>}
            <form className="ui form" onSubmit={handleSubmit}>
                <div className="field">
                    <label htmlFor="username">Имя пользователя</label>
                    <input type="text" name="username" id="username" placeholder="имя пользователя" value={username} onChange={(e) => setUsername(e.target.value)} />
                </div>
                <div className="field">
                    <label htmlFor="password">Пароль</label>
                    <input type="password" name="password" id="password" placeholder="пароль" value={password} onChange={(e) => setPassword(e.target.value)} />
                </div>
                <button className={isLoading ? "ui primary button loading" : "ui primary button"} type="submit">Войти</button>
            </form>
        </div>
    );
}

export default LoginForm;
