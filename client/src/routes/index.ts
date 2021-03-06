import React from "react";
import Login from "../pages/login";
import PrivatePage from "../pages/private-page";
import PublicPage from "../pages/public-page";
import UserList from "../pages/user-list";

export interface IRoute {
    path: string;
    component: React.ComponentType;
    exact?: boolean;
}

export enum RouteNames {
    LOGIN = "/login",
    PRIVATE_PAGE = "/private_page",
    PUBLIC_PAGE = "/public_page",
    USER_LIST = "/users"
}

export const privateRoutes: IRoute[] = [
    { path: RouteNames.PRIVATE_PAGE, component: PrivatePage, exact: true },
    { path: RouteNames.USER_LIST, component: UserList, exact: true}
]

export const publicRoutes: IRoute[] = [
    { path: RouteNames.LOGIN, component: Login, exact: true },
    { path: RouteNames.PUBLIC_PAGE, component: PublicPage, exact: true }
]
