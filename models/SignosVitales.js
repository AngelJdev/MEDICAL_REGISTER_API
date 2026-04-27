const mongoose = require('mongoose');

const signosVitalesSchema = new mongoose.Schema({
    paciente_id: { type: String, required: true },
    tension_arterial: { type: String, required: true }, // e.g., "120/80"
    frecuencia_cardiaca: { type: Number, required: true },
    frecuencia_respiratoria: { type: Number },
    temperatura: { type: Number, required: true },
    saturacion_oxigeno: { type: Number },
    peso: { type: Number },
    talla: { type: Number },
    fecha: { type: Date, default: Date.now }
}, { collection: 'md_signos_vitales', timestamps: true });

module.exports = mongoose.model('SignosVitales', signosVitalesSchema);
