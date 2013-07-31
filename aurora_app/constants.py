ROLES = {
    "USER": 1,
    "ADMIN": 2
}

# Permissons
PERMISSIONS = {
    ROLES["ADMIN"]: [
        # Projects
        "create_project", "edit_project", "delete_project",
        # Repositories
        "clone_repository", "remove_repository",
        # Stages
        "create_stage", "edit_stage", "delete_stage",
        # Deploments
        "create_deployment", "cancel_deployment",
        # Tasks
        "create_task", "edit_task", "delete_task",
        # Users
        "create_user", "edit_user", "delete_user"
    ],
    ROLES["USER"]: []
}

# Deployment's statuses
STATUSES = {
    "READY": 1,
    "RUNNING": 2,
    "COMPLETED": 3,
    "CANCELED": 4,
    "FAILED": 5,
}

BOOTSTRAP_ALERTS = {
    STATUSES['COMPLETED']: 'success',
    STATUSES['FAILED']: 'error',
    STATUSES['READY']: 'info',
    STATUSES['RUNNING']: 'info',
    STATUSES['CANCELED']: 'error'
}
