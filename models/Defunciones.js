const mongoose = require('mongoose');

const defuncionesSchema = new mongoose.Schema({
    persona_id: { type: String, required: true },
    fecha_defuncion: { type: Date, required: true },
    hora_defuncion: { type: String },
    causa_defuncion: { type: String, required: true },
    lugar_defuncion: { type: String },
    certificado_defuncion: { type: String, unique: true, required: true },
    medico_certificante: { type: String }
}, { collection: 'md_defunciones', timestamps: true });

module.exports = mongoose.model('Defunciones', defuncionesSchema);
