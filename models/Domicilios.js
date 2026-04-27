const mongoose = require('mongoose');

const domiciliosSchema = new mongoose.Schema({
    calle: { type: String, required: true },
    numero_exterior: { type: String, required: true },
    numero_interior: { type: String },
    colonia: { type: String, required: true },
    codigo_postal: { type: String, required: true },
    municipio: { type: String, required: true },
    estado: { type: String, required: true },
    pais: { type: String, default: 'México' }
}, { collection: 'md_domicilios', timestamps: true });

module.exports = mongoose.model('Domicilios', domiciliosSchema);
