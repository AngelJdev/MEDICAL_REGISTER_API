const mongoose = require('mongoose');

const notasMedicasSchema = new mongoose.Schema({
    paciente_id: { type: String, required: true },
    medico_id: { type: String, required: true },
    contenido: { type: String, required: true },
    fecha: { type: Date, default: Date.now },
    tipo_nota: { type: String, enum: ['Consulta', 'Evolución', 'Interconsulta'], default: 'Consulta' }
}, { collection: 'md_notas_medicas', timestamps: true });

module.exports = mongoose.model('NotasMedicas', notasMedicasSchema);
