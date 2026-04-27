const mongoose = require('mongoose');

const nacimientosSchema = new mongoose.Schema({
    madre_id: { type: String, required: true },
    padre_id: { type: String },
    fecha_nacimiento: { type: Date, required: true },
    hora_nacimiento: { type: String },
    peso_kg: { type: Number, required: true },
    talla_cm: { type: Number, required: true },
    sexo: { type: String, enum: ['M', 'F', 'Indeterminado'], required: true },
    lugar_nacimiento: { type: String, required: true },
    certificado_nacimiento: { type: String, unique: true }
}, { collection: 'md_nacimientos', timestamps: true });

module.exports = mongoose.model('Nacimientos', nacimientosSchema);
