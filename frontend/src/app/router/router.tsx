import { createBrowserRouter } from "react-router-dom"
import { LoginPage } from "@pages/login"
import { Layout } from "../layout"
import { AuthProvider } from "../providers/auth-provider"
import { Homepage } from "@pages/home-page"

export const router = createBrowserRouter(
    [
        {
            path: "/",
            element: <Layout />,
            errorElement: (
                <div>Oups... Cant find that page or something is broken</div>
            ),
            children: [
                {
                    path: "/",
                    element: <Homepage />,
                },
                {
                    path: "login",
                    element: <LoginPage />,
                },
                {
                    element: <AuthProvider />,
                    children: [
                        {
                            path: "marketplace",
                            element: (
                                <div>welcome to the marketplace service!</div>
                            ),
                            children: [],
                        },
                        {
                            path: "share-items",
                            element: (
                                <div>welcome to the share-items service!</div>
                            ),
                            children: [],
                        },
                    ],
                },
            ],
        },
    ],
    {
        future: {
            v7_relativeSplatPath: true,
        },
    }
)
