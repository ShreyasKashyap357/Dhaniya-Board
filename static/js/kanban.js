
const name = document.getElementById('column-name').value;
        const status = document.getElementById('column-status').value;
        
        if (!name || !status) {
            toastManager.show('Please fill all fields', 'warning', 2000);
            return;
        }

        try {
            const response = await fetch(`/api/projects/${this.projectId}/columns`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, status })
            });

            if (response.ok) {
                location.reload(); // Refresh to show new column
            } else {
                toastManager.show('Failed to add column', 'error', 3000);
            }
        } catch (error) {
            console.error('Error adding column:', error);
            toastManager.show('Error adding column', 'error', 3000);
        }
    }

    getCSRFToken() {
        const token = document.querySelector('meta[name="csrf-token"]');
        return token ? token.getAttribute('content') : '';
    }
}

// Initialize Kanban board when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const projectBoard = document.getElementById('kanban-board');
    if (projectBoard) {
        const projectId = projectBoard.dataset.projectId;
        window.kanbanBoard = new KanbanBoard(projectId);
    }
});
