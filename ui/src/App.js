import "./App.css";
import { AuthProvider } from "./provider/useAuth";
import { BrowserRouter } from "react-router-dom";
import { AppRoutes } from './routes/Routes'
import ResponsiveAppBar from "./features/Navigation/navbar";

// function InnerApp() {
//     const { user, loading, error, login, signUp, logout } = useAuth();
// }

function App() {

    return (
        <div className="App">
            <AuthProvider>
            <ResponsiveAppBar />
                <BrowserRouter>
                    <AppRoutes />
                </BrowserRouter>
            </AuthProvider>
        </div>
    );
}

export default App;
