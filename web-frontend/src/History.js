import React, { useEffect, useState } from 'react';
import { getRecentUploads } from './api';

const History = () => {
    const [history, setHistory] = useState([]);

    useEffect(() => {
        const fetchHistory = async () => {
            try {
                const response = await getRecentUploads();
                setHistory(response.data);
            } catch (error) {
                console.error("Error fetching history:", error);
            }
        };

        fetchHistory();
        
        // Poll every 5 seconds to keep updated (optional but good for UX)
        const interval = setInterval(fetchHistory, 5000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div style={{ marginTop: '30px', textAlign: 'left', maxWidth: '600px', margin: '30px auto' }}>
            <h3>Recent Uploads</h3>
            {history.length === 0 ? (
                <p>No uploads yet.</p>
            ) : (
                <ul>
                    {history.map((item) => (
                        <li key={item.id}>
                            <strong>{item.file_name}</strong> - {new Date(item.uploaded_at).toLocaleString()}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default History;
