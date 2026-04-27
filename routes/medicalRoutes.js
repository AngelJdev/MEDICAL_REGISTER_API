const express = require('express');
const router = express.Router();
const { protect } = require('../middlewares/auth');

// Import Controllers
const NotasMedicas = require('../controllers/NotasMedicasController');
const SignosVitales = require('../controllers/SignosVitalesController');
const Diagnostico = require('../controllers/DiagnosticoController');
const Tratamientos = require('../controllers/TratamientosController');
const Nacimientos = require('../controllers/NacimientosController');
const Defunciones = require('../controllers/DefuncionesController');
const DocumentosOficiales = require('../controllers/DocumentosOficialesController');
const Domicilios = require('../controllers/DomiciliosController');
const PersonasDomicilio = require('../controllers/PersonasDomicilioController');
const Valoraciones = require('../controllers/ValoracionesController');

// Helper to apply CRUD routes to a specific path
const applyRoutes = (path, controller) => {
    router.route(`/${path}`)
        .get(protect, controller.getAll || controller.getNotasMedicas)
        .post(protect, controller.createOne || controller.createNotaMedica);
    
    router.route(`/${path}/:id`)
        .get(protect, controller.getOne || controller.getNotaMedica)
        .put(protect, controller.updateOne || controller.updateNotaMedica)
        .delete(protect, controller.deleteOne || controller.deleteNotaMedica);
};

// Map each model to its route
applyRoutes('notas-medicas', NotasMedicas);
applyRoutes('signos-vitales', SignosVitales);
applyRoutes('diagnostico', Diagnostico);
applyRoutes('tratamientos', Tratamientos);
applyRoutes('nacimientos', Nacimientos);
applyRoutes('defunciones', Defunciones);
applyRoutes('documentos-oficiales', DocumentosOficiales);
applyRoutes('domicilios', Domicilios);
applyRoutes('personas-domicilio', PersonasDomicilio);
applyRoutes('valoraciones', Valoraciones);

module.exports = router;
