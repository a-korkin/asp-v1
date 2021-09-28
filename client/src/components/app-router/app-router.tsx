import React, { FC, useEffect } from "react";
import { Switch, Route, Redirect } from "react-router-dom";
import { useActions } from "../../hooks/use-actions";
import { useTypedSelector } from "../../hooks/use-typed-selector";
import { privateRoutes, publicRoutes, RouteNames } from "../../routes";

const AppRouter: FC = () => {
    const { checkAuth, fetchUsers } = useActions();
    useEffect(() => {
        if (localStorage.getItem("token")) {
            checkAuth();
            fetchUsers();
        }
    }, []);
    
    const {isAuth} = useTypedSelector(state => state.auth);
    
    return (
        isAuth
        ?
        <Switch>
            {privateRoutes.map(route => 
                <Route key={route.path} path={route.path} component={route.component} exact={route.exact} />
            )}
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
