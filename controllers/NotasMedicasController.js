const NotasMedicas = require('../models/NotasMedicas');
const factory = require('../utils/factory');

/**
 * Operaciones CRUD para Notas Médicas (md_notas_medicas)
 */

exports.getNotasMedicas = factory.getAll(NotasMedicas);
exports.getNotaMedica = factory.getOne(NotasMedicas);
exports.createNotaMedica = factory.createOne(NotasMedicas);
exports.updateNotaMedica = factory.updateOne(NotasMedicas);
exports.deleteNotaMedica = factory.deleteOne(NotasMedicas);
