document.addEventListener('DOMContentLoaded', function() {
    fetchPatients();
    document.getElementById('addForm').onsubmit = async function(e) {
        e.preventDefault();
        const patient = {
            id: document.getElementById('id').value,
            name: document.getElementById('name').value,
            age: document.getElementById('age').value,
            gender: document.getElementById('gender').value
        };
        await fetch('/api/patients', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(patient)
        });
        fetchPatients();
        this.reset();
    };
});

function fetchPatients() {
    fetch('/api/patients')
        .then(res => res.json())
        .then(data => {
            const table = document.getElementById('patientsTable');
            table.innerHTML = '';
            data.forEach(p => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${p.id}</td>
                    <td>${p.name}</td>
                    <td>${p.age}</td>
                    <td>${p.gender}</td>
                    <td>
                        <button onclick="deletePatient('${p.id}')">Delete</button>
                    </td>
                `;
                table.appendChild(row);
            });
        });
}

function deletePatient(id) {
    fetch(`/api/patients/${id}`, { method: 'DELETE' })
        .then(() => fetchPatients());
}
