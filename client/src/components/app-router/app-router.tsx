import React, { FC } from "react";
import { Switch, Route, Redirect } from "react-router-dom";
import { privateRoutes, publicRoutes, RouteNames } from "../../routes";

const AppRouter: FC = () => {
    const isAuth: boolean = false;
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
