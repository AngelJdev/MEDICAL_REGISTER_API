const mongoose = require('mongoose');

const diagnosticoSchema = new mongoose.Schema({
    paciente_id: { type: String, required: true },
    nota_id: { type: mongoose.Schema.Types.ObjectId, ref: 'NotasMedicas' },
    descripcion: { type: String, required: true },
    codigo_cie: { type: String, required: true }, // International Classification of Diseases
    tipo: { type: String, enum: ['Presuntivo', 'Definitivo'], default: 'Presuntivo' },
    fecha: { type: Date, default: Date.now }
}, { collection: 'md_diagnostico', timestamps: true });

module.exports = mongoose.model('Diagnostico', diagnosticoSchema);
