import {
    Route,
    Routes,
    Navigate
} from "react-router-dom";
import useAuth from "../provider/useAuth";
import { HomePage } from "../features/Home";
import { LoginForm } from "../features/auth";
import { RoomPage } from "../features/Room/room";
import { JoinHome } from "../features/Home/JoinHome";
import CreateHome from "../features/Home/CreateHome";
import { UserProfile } from "../features/User/Profile";
import RoutineModal from "../features/Routine/RoutineModal";

const AppRoutes = () => {
    const { user } = useAuth();
    return user ? getAuthRoutes() : getLoginRoute()
}

function getAuthRoutes() {
    return (
        <Routes>
            <Route
                exact
                path="/"
                element={<Navigate to="/home" replace />}
            />
            <Route
                exact
                path="/home"
                element={<HomePage />}
            />
            <Route
                exact
                path="/room"
                element={<RoomPage />}
            />
            <Route
                exact
                path="/joinhome"
                element={<JoinHome />}
            />
            <Route
                exact
                path="/createhome"
                element={<CreateHome />}
            />
            <Route
                exact
                path="/user"
                element={<UserProfile />}
            />
            <Route
                exact
                path="/create-routine"
                element={<RoutineModal />}
            />
            <Route
                exact
                path="/rooms/:id"
                element={<RoomPage />}
            />
        </Routes>
    )
}

function getLoginRoute() {
    return (
        <Routes>
            <Route
                exact
                path="*"
                element={<LoginForm />}
            />
        </Routes>
    )
}
// function AuthenticatedRoute({ roles, ...props }) {
//     const { user } = useAuth();

//     if (!user) return <Routes to="/login" />;

//     return <Route {...props} />;
// }

// function Router() {
//     return (
//         <Routes>
//             <AuthenticatedRoute
//                 exact
//                 path="/home"
//                 component={HomePage}
//             />
//             <Route
//                 exact
//                 path="/login"
//                 component={LoginForm}
//             />
//         </Routes>
//     );
// }

export { AppRoutes };
