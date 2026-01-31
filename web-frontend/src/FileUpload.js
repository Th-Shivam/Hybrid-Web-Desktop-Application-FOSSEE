import React, { useState } from 'react';
import { uploadCSV } from './api';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const FileUpload = () => {
    const [file, setFile] = useState(null);
    const [data, setData] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        if (!file) {
            console.log("No file selected");
            return;
        }

        try {
            const response = await uploadCSV(file);
            console.log("Upload Success:", response.data);
            setData(response.data);
        } catch (error) {
            console.log("Upload Error:", error);
        }
    };

    // Prepare chart data
    const chartData = data ? {
        labels: Object.keys(data.equipment_type_counts),
        datasets: [
            {
                label: 'Equipment Count',
                data: Object.values(data.equipment_type_counts),
                backgroundColor: 'rgba(75, 192, 192, 0.5)',
            },
        ],
    } : null;

    return (
        <div>
            <h2>Upload CSV</h2>
            <input type="file" onChange={handleFileChange} accept=".csv" />
            <button onClick={handleUpload}>Upload</button>

            {data && (
                <div style={{ marginTop: '20px' }}>
                    <h3>Analysis Result</h3>
                    <p>Total Rows: {data.total_rows}</p>
                    <p>Avg Flowrate: {data.average_metrics.flowrate}</p>
                    <p>Avg Pressure: {data.average_metrics.pressure}</p>
                    <p>Avg Temperature: {data.average_metrics.temperature}</p>
                    
                    <div style={{ maxWidth: '600px', margin: '20px auto' }}>
                        <Bar data={chartData} />
                    </div>

                    {data.data && data.data.length > 0 && (
                        <table border="1" style={{ marginTop: '20px', width: '100%', borderCollapse: 'collapse' }}>
                            <thead>
                                <tr>
                                    {Object.keys(data.data[0]).map((key) => (
                                        <th key={key} style={{ padding: '8px' }}>{key}</th>
                                    ))}
                                </tr>
                            </thead>
                            <tbody>
                                {data.data.map((row, index) => (
                                    <tr key={index}>
                                        {Object.values(row).map((val, i) => (
                                            <td key={i} style={{ padding: '8px' }}>{val}</td>
                                        ))}
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    )}
                </div>
            )}
        </div>
    );
};

export default FileUpload;
