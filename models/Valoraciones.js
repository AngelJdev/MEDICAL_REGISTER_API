const mongoose = require('mongoose');

const valoracionesSchema = new mongoose.Schema({
    paciente_id: { type: String, required: true },
    medico_id: { type: String, required: true },
    tipo_valoracion: { type: String, required: true }, // e.g., "Nutricional", "Psicológica"
    escala_utilizada: { type: String }, // e.g., "Glasgow", "Apgar"
    resultado_valoracion: { type: String, required: true },
    observaciones: { type: String },
    fecha: { type: Date, default: Date.now }
}, { collection: 'md_valoraciones', timestamps: true });

module.exports = mongoose.model('Valoraciones', valoracionesSchema);
