import React, {
    createContext,
    useContext,
    useEffect,
    useMemo,
    useState,
    useCallback
} from "react";
// import { useHistory, useLocation } from "react-router-dom";
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

    // Make the provider update only when it should.
    // We only want to force re-renders if the user,
    // loading or error states change.
    //
    // Whenever the `value` passed into a provider changes,
    // the whole tree under the provider re-renders, and
    // that can be very costly! Even in this case, where
    // you only get re-renders when logging in and out
    // we want to keep things very performant.
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

    // We only want to render the underlying app after we
    // assert for the presence of a current user.
    return (
        <AuthContext.Provider value={memoedValue}>
            {!loadingInitial && children}
        </AuthContext.Provider>
    );
}

// Let's only export the `useAuth` hook instead of the context.
// We only want to use the hook directly and never the context component.
export default function useAuth() {
    return useContext(AuthContext);
}
