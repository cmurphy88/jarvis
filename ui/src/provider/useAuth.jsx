import React, {
    createContext,
    useContext,
    useEffect,
    useMemo,
    useState,
    useCallback
} from "react";
import * as sessionsApi from "./auth";
import * as usersApi from "../shared/api/usersAPI";
import storage from "../utils/storage"

const AuthContext = createContext({});

function handleUserResponse({ access_token }) {
    storage.setAccessToken(access_token);

}

export function AuthProvider({
    children,
}
) {
    const [user, setUser] = useState();
    const [error, setError] = useState();
    const [loading, setLoading] = useState(false);
    const [loadingInitial, setLoadingInitial] = useState(true);

    function getLoggedInUser() {
        sessionsApi.getCurrentUser()
            .then((user) => {
                setUser(user)

            })
            .catch((_error) => { })
            .finally(() => setLoadingInitial(false));
    }
    useEffect(() => {
        getLoggedInUser()
    }, []);

    const login = useCallback((formData) => {
        setLoading(true);

        sessionsApi.login(formData)
            .then((user) => {
                setError(null);
                handleUserResponse(user);
                getLoggedInUser();
            })
            .catch((error) => setError(error))
            .finally(() => setLoading(false));
    }, [])

    function signUp(username, first_name, last_name, password) {
        setLoading(true);

        usersApi.signUp({ username, first_name, last_name, password })
            .then((user) => {
                setUser(user);
                // history.push("/")
            })
            .catch((error) => setError(error))
            .finally(() => setLoading(false));
    }

    function logout() {
        sessionsApi.logout().then(() => setUser(undefined));
    }

    const memoedValue = useMemo(
        () => ({
            user,
            loading,
            error,
            login,
            signUp,
            logout,
        }),
        [user, login, loading, error]
    );

    return (
        <AuthContext.Provider value={memoedValue}>
            {!loadingInitial && children}
        </AuthContext.Provider>
    );
}

export default function useAuth() {
    return useContext(AuthContext);
}
