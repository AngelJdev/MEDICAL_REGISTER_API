const mongoose = require('mongoose');

const tratamientosSchema = new mongoose.Schema({
    diagnostico_id: { type: mongoose.Schema.Types.ObjectId, ref: 'Diagnostico', required: true },
    medicamento: { type: String, required: true },
    dosis: { type: String, required: true },
    frecuencia: { type: String, required: true },
    duracion: { type: String, required: true },
    indicaciones_adicionales: { type: String },
    fecha_inicio: { type: Date, default: Date.now }
}, { collection: 'md_tratamientos', timestamps: true });

module.exports = mongoose.model('Tratamientos', tratamientosSchema);
