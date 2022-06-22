# jarvis

## Domain Model
```mermaid
graph TD
    A[Admin] --- B[User]
    B --- D[Routine]
    B --- P
    D --- E[Room]
    D --- F[Light Routine Setting]
    D --- G[Media Routine Setting]
    D --- H[TRV Routine Setting]
    F --- I[Light]
    G --- J[Media]
    H --- K[TRV]
    E --- L[Camera]
    M[Home] --- E
    L --- N[Alert]
    N --- O[Notifications]
    O --- B
    B --- M
    P[User Room Hierarchy] --- E
    Q[Routine Time Entries] --- D
```

  ## ERD
```mermaid
erDiagram
    USER {
        int user_id PK
        string first_name
        string last_name
        string email
        string password
    }
    HOME {
        int home_id PK
        string home_name
    }
    HOME_USER {
        int home_user_id PK
        int home_id FK
        int user_id FK
        boolean is_admin
    }
    USER_HIERARCHY {
        int user_hierarchy_id PK
        int room_id FK
        int user_id FK
        int user_order
    }
    ROOM {
        int room_id PK
        string room_name
        int home_id FK
        int camera_id FK
    }
    
    ROUTINE {
        int routine_id PK
        int room_id FK
        int user_id FK
        time start_time
        time end_time
    }
    MEDIA_ROUTINE_SETTING {
        int media_routine_id PK
        int media_id FK
        int routine_id FK
        string media_url
        boolean is_active
        boolean is_playing
    }
    TRV_ROUTINE_SETTING {
        int trv_routine_id PK
        int trv_id FK
        int routine_id FK
        double temperature
        boolean is_active
    }
    LIGHT_ROUTINE_SETTING {
        int light_routine_id PK
        int light_id FK
        int routine_id FK
        int brightness
        boolean is_active
    }
    MEDIA {
        int media_id PK
        string ip_address
    }
    TRV {
        int trv_id PK
        string ip_address
    }
    LIGHT {
        int light_id PK
        string ip_address
    }
    CAMERA {
        int camera_id PK
        string ip_address
    }
    ROUTINE_TIME_ENTRIES {
        int routine_time_entry_id PK
        int routine_id FK
        timestamp time_entry
    }
    ROUTINE_ALERT {
        int alert_id PK
        string message
        int routine_id FK
    }
    HOME ||--|{ HOME_USER : has
    ROOM ||--|| CAMERA : has
    HOME_USER }|--|| USER : has
    USER ||--|{ USER_HIERARCHY : has
    
    ROOM ||--|{ USER_HIERARCHY : contains
    HOME ||--|{ ROOM : contains 
    
    ROUTINE }|--|| ROOM : partOf
    ROUTINE ||--|| MEDIA_ROUTINE_SETTING : has 
    ROUTINE ||--|| TRV_ROUTINE_SETTING : has  
    ROUTINE ||--|| LIGHT_ROUTINE_SETTING : has  
    ROUTINE }|--|| USER : has
    
    MEDIA_ROUTINE_SETTING }|--|| MEDIA : controls  
    TRV_ROUTINE_SETTING }|--|| TRV : controls  
    LIGHT_ROUTINE_SETTING }|--|| LIGHT : controls  
      
    ROUTINE ||--|{ ROUTINE_TIME_ENTRIES : logs 
    ROUTINE ||--|{ ROUTINE_ALERT : creates
    
```
