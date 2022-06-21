# jarvis

## Domain Model
```mermaid
graph TD
    A[Admin] ---B[User]
    B --- C[User Profile]
    B --- D[Routine]
    D --- E[Room]
    D --- P[User Hierarchy]
    E --- F[Light Routine Setting]
    E --- G[Speaker Routine Setting]
    E --- H[TRV Routine Setting]
    F --- I[Light]
    G --- J[Speaker]
    H --- K[TRV]
    E --- L[Camera]
    M[Home] --- E
    N[Alert] --- L
    N --- O[Notifications]
    O --- B
    B --- M
```
