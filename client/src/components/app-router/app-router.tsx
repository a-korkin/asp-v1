import React, { FC, useEffect } from "react";
import { Switch, Route, Redirect } from "react-router-dom";
import { useActions } from "../../hooks/use-actions";
import { useTypedSelector } from "../../hooks/use-typed-selector";
import { privateRoutes, publicRoutes, RouteNames } from "../../routes";

const AppRouter: FC = () => {
    const { checkAuth } = useActions();
    const { user } = useTypedSelector(state => state.auth);
    useEffect(() => {
        if (localStorage.getItem("token")) {
            console.log(user.username);
            checkAuth(user.username);
        }
    }, []);

    const {isAuth} = useTypedSelector(state => state.auth);
    return (
        isAuth
        ?
        <Switch>
            {privateRoutes.map(route => 
                <Route key={route.path} path={route.path} component={route.component} exact={route.exact} />)}
            <Redirect to={RouteNames.PRIVATE_PAGE} />
        </Switch>
        :
        <Switch>
            {publicRoutes.map(route => 
                <Route key={route.path} path={route.path} component={route.component} exact={route.exact} />)}
            <Redirect to={RouteNames.LOGIN} />
        </Switch>
        
    );
}

export default AppRouter;
