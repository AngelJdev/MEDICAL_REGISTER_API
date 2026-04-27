const mongoose = require('mongoose');

const documentosOficialesSchema = new mongoose.Schema({
    persona_id: { type: String, required: true },
    tipo_documento: { type: String, enum: ['CURP', 'INE', 'Pasaporte', 'Acta de Nacimiento'], required: true },
    numero_documento: { type: String, required: true, unique: true },
    fecha_expedicion: { type: Date },
    fecha_vencimiento: { type: Date },
    archivo_url: { type: String }
}, { collection: 'md_documentos_oficiales', timestamps: true });

module.exports = mongoose.model('DocumentosOficiales', documentosOficialesSchema);
