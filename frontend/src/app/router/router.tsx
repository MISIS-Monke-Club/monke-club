import { createBrowserRouter, Link, Outlet } from "react-router-dom"
import { Layout } from "../layout"
import { AuthProvider } from "../providers/auth-provider"
import { LoginPage } from "@pages/login"
import { Homepage } from "@pages/home-page"
import { MentorsPage } from "@pages/mentors/mentors"
import { MentorPage } from "@pages/mentor-page/mentor-page"
import { RequestsPage } from "@pages/requests-page"
import { RequestDetail } from "@pages/detailed-request-page"
import { FirstMentors } from "@pages/first-mentors-page"
import { VacationPage } from "@pages/vacation-page"
import { EventsPage } from "@pages/events-page"

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
                                <div>
                                    <Link to='mentors'>Mentors</Link>welcome to
                                    the marketplace service!
                                    <Outlet />
                                </div>
                            ),
                            errorElement: (
                                <div>
                                    Что-то пошло не так в сервисе маркетплейса(
                                </div>
                            ),
                            children: [
                                {
                                    path: "",
                                    element: <FirstMentors />,
                                },
                                {
                                    path: "mentors",
                                    element: <MentorsPage />,
                                },
                                {
                                    path: "mentors/:mentorId",
                                    element: <MentorPage />,
                                },
                            ],
                        },
                        {
                            path: "request",
                            element: <RequestsPage />,
                        },
                        {
                            path: "request/:slug",
                            element: <RequestDetail />,
                        },
                        {
                            path: "vacations",
                            element: <VacationPage />,
                        },
                        {
                            path: "events",
                            element: <EventsPage />,
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
