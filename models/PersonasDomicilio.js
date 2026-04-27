const mongoose = require('mongoose');

const personasDomicilioSchema = new mongoose.Schema({
    persona_id: { type: String, required: true },
    domicilio_id: { type: mongoose.Schema.Types.ObjectId, ref: 'Domicilios', required: true },
    tipo_domicilio: { type: String, enum: ['Residencial', 'Trabajo', 'Notificación'], default: 'Residencial' },
    es_principal: { type: Boolean, default: true }
}, { collection: 'md_personas_tiene_domicilio', timestamps: true });

module.exports = mongoose.model('PersonasDomicilio', personasDomicilioSchema);
